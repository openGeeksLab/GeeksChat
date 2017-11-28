import graphene

import apps.chat.schema


class Query(apps.chat.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
