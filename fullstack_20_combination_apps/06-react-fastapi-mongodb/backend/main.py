import os
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

def check_db():
    client = MongoClient(os.environ["MONGODB_URI"], serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    client.close()
    return

@app.get("/health")
def health():
    check_db()
    return {"status":"ok","database":"mongodb"}

@app.get("/backend/message")
def message():
    return {"message":"06-react-fastapi-mongodb is working"}
