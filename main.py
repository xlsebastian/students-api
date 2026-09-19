from fastapi import FastAPI
from config import APP_VERSION

app = FastAPI(title="students-api", version=APP_VERSION)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/students")
def list_students():
    return [{"id": "1", "name": "Ana"}, 
            {"id": "2", "name": "Luis"}]
