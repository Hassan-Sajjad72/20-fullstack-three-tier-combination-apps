import os
from fastapi import FastAPI
import psycopg

app = FastAPI()

def check_db():
    conn = psycopg.connect(os.environ["DATABASE_URL"], connect_timeout=5)
    conn.close()

@app.get("/health")
def health():
    check_db()
    return {"status":"ok","database":"postgresql"}

@app.get("/api/v1/message")
def message():
    return {"message":"18-nextjs-fastapi-postgres is working"}
