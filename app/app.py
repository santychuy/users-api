import uvicorn
from fastapi import FastAPI

from config.db import Base, engine
from config.index import Settings
from routes.user import user

Base.metadata.create_all(bind=engine)

settings = Settings()
app = FastAPI()


@app.get("/")
def root():
    return "Users API"


app.include_router(user)

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=settings.port,
        reload=True if settings.env == "development" else False,
    )
