import os
from fastapi import FastAPI
import psycopg

app = FastAPI()

def check_db():
    conn = psycopg.connect(
        host=os.environ["DB_HOST"], port=int(os.environ["DB_PORT"]),
        dbname=os.environ["DB_NAME"], user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"], connect_timeout=5
    )
    conn.close()

@app.get("/ready")
def health():
    check_db()
    return {"status":"ok","database":"postgresql"}

@app.get("/api/message")
def message():
    return {"message":"07-vue-fastapi-postgres is working"}
