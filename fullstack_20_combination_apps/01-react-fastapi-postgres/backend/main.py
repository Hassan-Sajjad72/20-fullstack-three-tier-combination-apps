import os
from fastapi import FastAPI
import psycopg

app = FastAPI()

def check_db():
    conn = psycopg.connect(
        host=os.environ["POSTGRES_HOST"], port=int(os.environ["POSTGRES_PORT"]),
        dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"], connect_timeout=5
    )
    conn.close()

@app.get("/health")
def health():
    check_db()
    return {"status":"ok","database":"postgresql"}

@app.get("/api/v1/message")
def message():
    return {"message":"01-react-fastapi-postgres is working"}
