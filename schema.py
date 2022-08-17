import graphene
import app.schema


class Query(app.schema.AppQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
