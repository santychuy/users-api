from fastapi import FastAPI

from config.index import Settings
from routes.user import user

settings = Settings()
app = FastAPI()


@app.get('/')
def root():
    return "Users API"


app.include_router(user, prefix="/api/v1/users")
