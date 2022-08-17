import graphene
import app.schema


class Query(app.schema.AppQuery, graphene.ObjectType):
    pass


class Mutation(app.schema.Mutate, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
