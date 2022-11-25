from sqlalchemy.orm import Session

from schemas.user import UserSchema
from models.user import User


def read_users(db: Session):
    return db.query(User).all()


def read_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def create_user(db: Session, user: UserSchema):
    new_user = User(
        id=user.id, fullname=user.fullname, username=user.username, gender=user.gender
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
