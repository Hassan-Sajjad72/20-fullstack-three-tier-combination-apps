import os
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

def check_db():
    client = MongoClient(os.environ["MONGO_URI"], serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    client.close()
    return

@app.get("/healthz")
def health():
    check_db()
    return {"status":"ok","database":"mongodb"}

@app.get("/api/message")
def message():
    return {"message":"15-svelte-fastapi-mongodb is working"}
