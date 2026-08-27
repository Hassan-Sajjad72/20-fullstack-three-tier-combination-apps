import os
from flask import Flask, jsonify
import psycopg

app = Flask(__name__)

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
    return jsonify(status="ok", database="postgresql")

@app.get("/service/message")
def message():
    return jsonify(message="10-vue-flask-postgres is working")

if __name__ == "__main__":
    app.run(host=os.getenv("HOST","0.0.0.0"), port=int(os.getenv("PORT","5000")))
