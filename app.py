from fastapi import FastAPI

from routes.user import user

app = FastAPI()


@app.get('/')
def root():
    return "User API"


app.include_router(user, prefix="/api/v1/users")
