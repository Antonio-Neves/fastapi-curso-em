from fastapi import FastAPI
from http import HTTPStatus

from fast_zero.schemas import Message, UserSchema, UserDB, UserPublic, UserList


app = FastAPI()

# database = [
#     {
#       "username": "Deus",
#       "email": "Deus@deus.com",
#       "password": "Obrigado",
#       "id": 1
#     },
#     {
#       "username": "Rui",
#       "email": "rui@rui.com",
#       "password": "ruimano",
#       "id": 2
#     },
#     {
#       "username": "Duarte",
#       "email": "duarte@duarte.com",
#       "password": "duartemano",
#       "id": 3
#     }
# ]

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Obrigado meu Deus'}


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):

    user_with_id = UserDB(
        id =len(database) + 1,
        **user.model_dump()
    )

    database.append(user_with_id)

    return user_with_id
