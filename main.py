from fastapi import FastAPI
from config import APP_VERSION

app = FastAPI(tittle="students-api", version=APP_VERSION)

@app.get("/healt")
def healt():
    return {"status":"ok"}