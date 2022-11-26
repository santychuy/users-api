from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserSchema, UserUpdateDTO
from helpers.db import get_db
from services.user import read_users, read_user, create_user

user = APIRouter(prefix="/api/v1/users")


@user.get("/")
def get_users(db: Session = Depends(get_db)):
    return read_users(db)


@user.get("/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    user = read_user(db, id)

    if user is not None:
        return user
    raise HTTPException(status_code=404, detail="User was not founded")


@user.post("/")
def add_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = create_user(db, user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=new_user)


@user.put("/{id}")
def update_user(
    id: int, user_update: UserUpdateDTO, db: Session = Depends(get_db)
):
    user_query = db.query(User).filter(User.id == id)

    if user_query.first() is not None:
        user_query.update({**user_update.dict(exclude_unset=True)})
        db.commit()
        return {"message": "User updated"}
    raise HTTPException(status_code=404, detail="User does not exists")


@user.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user_query = db.query(User).filter(User.id == id)

    if user_query.first() is not None:
        user_query.delete()
        db.commit()
        return {"message": "User deleted", "user_id": id}
    raise HTTPException(status_code=404, detail="User does not exists")
