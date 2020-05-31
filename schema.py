#%%
import json

import graphene
from datetime import  datetime
import uuid

class User(graphene.ObjectType):
    id = graphene.ID(default_value = str(uuid.uuid4()))
    username = graphene.String()
    created_at = graphene.DateTime(default_value=datetime.now())


class Query(graphene.ObjectType):
    users = graphene.List(User,limit=graphene.Int())
    hello = graphene.String()
    admin = graphene.Boolean()

    def resolve_admin(self, info):
        return False

    def resolve_hello(self, info):
        return "World" 

    def resolve_users(self, info, limit=None):
        return [
            User(id="1",username="Fred",created_at=datetime.now()),
            User(id="2", username="Tom", created_at=datetime.now()),
            User(id="3", username="Rachel", created_at=datetime.now())
        ][:limit]

class createUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        username = graphene.String()
    
    def mutate(self,info,username):
        user = User(username=username)
        return createUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = createUser.Field()

schema = graphene.Schema(query=Query)
result = schema.execute( #always in camel-case
    '''
    mutation {
        createUser (username: "Fred"){
            user {
                id
                user
                
            }
        }
    }
    '''
)
print(result)
dictResult = dict(result.data.items())
print(json.dumps(dictResult)) 



# %%
