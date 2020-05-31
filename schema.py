import json

import graphene
from datetime import  datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()

class Query(graphene.ObjectType):
    users = graphene.List(User,limit=graphene.Int())
    hello = graphene.String()
    admin = graphene.Boolean()

    def resolve_admin(self, info):
        return False

    def resolve_hello(self, info):
        return "World"

    def resolve_users(self, info, limit):
        return [
            User(id="1",username="Fred",created_at=datetime.now()),
            User(id="2", username="Tom", created_at=datetime.now()),
            User(id="3", username="Rachel", created_at=datetime.now())

        ][:limit]


schema = graphene.Schema(query=Query,auto_camelcase=False)
result = schema.execute( #always in camel-case
    '''
    {
        users (limit:1){
            id
            username
            created_at
        }
    }
    '''
)

dictResult = dict(result.data.items())
print(json.dumps(dictResult)) 
