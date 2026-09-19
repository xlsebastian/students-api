from fastapi import FastAPI
from config import APP_VERSION

app = FastAPI(title="students-api", version=APP_VERSION)

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.get("/students")
def list_students():
    return [{"id":1,"name":"John Doe","phone":"123-456-7890"},
            {"id":2,"name":"Jane Smith","phone":"098-765-4321"}]
    return {"status": "ok"}

@app.get("/students")
def list_students():
    return [{"id": "1", "name": "Ana"}, 
            {"id": "2", "name": "Luis"}]
