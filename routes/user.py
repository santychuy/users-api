from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from config.db import SessionLocal
from models.user import User
from schemas.user import UserSchema, UserUpdateDTO

user = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@user.get("/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == id).first()
    # raise HTTPException(status_code=404, detail=f"User {id} was not founded")


@user.post("/")
def add_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = User(id=user.id, fullname=user.fullname, username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Find the way to not update a value when it's not passed
@user.put("/{id}")
def update_user(id: int, user_update: UserUpdateDTO, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).update({**user_update.dict()})
    db.commit()
    return {"message": "User updated", "user": user_update}
    # raise HTTPException(status_code=404, detail=f"User {id} does not exists")


@user.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).delete()
    db.commit()
    return {"message": "User deleted", "user_id": id}
    # raise HTTPException(status_code=404, detail=f"User {id} does not exists")
