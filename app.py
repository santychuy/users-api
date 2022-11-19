from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException

from entities import Gender, User, UserUpdateDTO

app = FastAPI()

db: list[User] = [
    User(
        id=uuid4(),
        fullname="Santiago",
        username="santychuy",
        gender=Gender.male
    ),
    User(
        id=uuid4(),
        fullname="Patricia",
        username="patrick",
        gender=Gender.female
    )
]


@app.get('/')
def root():
    return "User API"


@app.get('/api/v1/users')
def get_users():
    return db


@app.get('/api/v1/users/{id}')
def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    raise HTTPException(
        status_code=404,
        detail=f"User {id} was not founded"
    )


@app.post('/api/v1/users')
def add_user(user: User):
    db.append(user)
    return {"message": "New user created!", "id": user.id}


# Hmm I think it's a better way to optimize the casting for updating the properties
@app.put('/api/v1/users/{id}')
def update_user(id: UUID, user_update: UserUpdateDTO):
    for user in db:
        if user.id == id:
            if user_update.fullname is not None:
                user.fullname = user_update.fullname
            if user_update.username is not None:
                user.username = user_update.username
            if user_update.gender is not None:
                user.gender = user_update.gender
            return {"message": "User updated!"}
    raise HTTPException(
        status_code=404,
        detail=f"User {id} does not exists"
    )


@app.delete('/api/v1/users/{id}')
def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": "User deleted!"}
    raise HTTPException(
        status_code=404,
        detail=f"User {id} does not exists"
    )
