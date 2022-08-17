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
