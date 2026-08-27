import os
from flask import Flask, jsonify
import psycopg

app = Flask(__name__)

def check_db():
    conn = psycopg.connect(
        host=os.environ["PGHOST"], port=int(os.environ["PGPORT"]),
        dbname=os.environ["PGDATABASE"], user=os.environ["PGUSER"],
        password=os.environ["PGPASSWORD"], connect_timeout=5
    )
    conn.close()

@app.get("/healthz")
def health():
    check_db()
    return jsonify(status="ok", database="postgresql")

@app.get("/v1/message")
def message():
    return jsonify(message="03-react-flask-postgres is working")

if __name__ == "__main__":
    app.run(host=os.getenv("HOST","0.0.0.0"), port=int(os.getenv("PORT","5000")))
