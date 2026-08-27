import os
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

def check_db():
    conn = pymysql.connect(
        host=os.environ["MYSQL_HOST"], port=int(os.environ["MYSQL_PORT"]),
        database=os.environ["MYSQL_DATABASE"], user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"], connect_timeout=5
    )
    conn.close()

@app.get("/ready")
def health():
    check_db()
    return jsonify(status="ok", database="mysql")

@app.get("/api/v2/message")
def message():
    return jsonify(message="17-svelte-flask-mysql is working")

if __name__ == "__main__":
    app.run(host=os.getenv("HOST","0.0.0.0"), port=int(os.getenv("PORT","5000")))
