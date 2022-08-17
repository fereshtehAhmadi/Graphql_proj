import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from app.models import Quiz, Options


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz


class OptionsType(DjangoObjectType):
    class Meta:
        model = Options


class AppQuery(ObjectType):
    quiz = graphene.List(QuizType)
    option = graphene.List(OptionsType)
    quizs = graphene.Field(QuizType, id=graphene.Int())
    options = graphene.Field(OptionsType, id=graphene.Int())
    
    def resolve_quiz(root, self, **kwargs):
        return Quiz.objects.all()
    
    def resolve_option(root, self, **kwargs):
        return Options.objects.all()
    
    def resolve_quizs(root, self, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Quiz.objects.get(id=id)
        else:
            return None
            
    def resolve_options(root, self, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Options.objects.get(id=id)
        else:
            return None


class QuizInput(graphene.InputObjectType):
    question = graphene.String()


class CreateQuiz(graphene.Mutation):
    quiz = graphene.Field(QuizType)
    ok = graphene.Boolean(default_value=False)
    
    class Arguments:
        # question = graphene.String()
        input = QuizInput(required=True)
    
    def mutate(self, info, input):
        quiz_instance = Quiz.objects.create(question=input.question)
        ok = True
        return CreateQuiz(quiz=quiz_instance, ok=ok)


class UpdateQuiz(graphene.Mutation):
    quiz = graphene.Field(QuizType)
    ok = graphene.Boolean(default_value=False)
    
    class Arguments:
        id = graphene.Int()
        input = QuizInput()
        
    def mutate(self, info, id, input):
        quiz_instance = Quiz.objects.get(id=id)
        quiz_instance.question = input.question if input.question is not None else quiz_instance.question
        quiz_instance.save()
        ok = True
        return UpdateQuiz(quiz=quiz_instance, ok=ok)


class DeleteQuiz(graphene.Mutation):
    quiz = graphene.Field(QuizType)
    ok = graphene.Boolean(default_value=False)
    
    class Arguments:
        id = graphene.Int()
        input = QuizInput()
        
    def mutate(self, info, id, input):
        quiz_instance = Quiz.objects.get(id=id)
        quiz_instance.delete()
        ok = True
        return UpdateQuiz(quiz=quiz_instance, ok=ok)


class Mutate(graphene.ObjectType):
    create_quiz = CreateQuiz.Field()
    update_quiz = UpdateQuiz.Field()
    delete_quiz = DeleteQuiz.Field()
    