from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer

from config.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    fullname = Column("fullname", String(30), nullable=False)
    username = Column("username", String(30), nullable=False)
    gender = Column("gender", String, nullable=False, default="male")
