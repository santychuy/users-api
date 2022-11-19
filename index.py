import uvicorn

from app import settings, app


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0",
                port=settings.port)
