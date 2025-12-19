import time
import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///local.db")
APP_PORT = int(os.getenv("APP_PORT", "8000"))

engine = create_engine(DATABASE_URL, future=True)

def wait_for_db():
    if DATABASE_URL.startswith("sqlite"):
        return

    for _ in range(30):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return
        except Exception:
            time.sleep(1)

    raise RuntimeError("Database is not ready")


def init_db():
    if DATABASE_URL.startswith("sqlite"):
        ddl = """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        );
        """
    else:
        ddl = """
        CREATE TABLE IF NOT EXISTS notes (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL
        );
        """

    with engine.begin() as conn:
        conn.execute(text(ddl))

@app.get("/")
def home():
    return "<h1>Hello, DevOps</h1><p>Routes: GET /notes, POST /notes</p>"

@app.get("/notes")
def list_notes():
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT id, content FROM notes ORDER BY id DESC")
        ).mappings().all()

    return jsonify([dict(r) for r in rows])


@app.post("/notes")
def add_note():
    data = request.get_json(silent=True) or {}
    content = (data.get("content") or "").strip()
    if not content:
        return jsonify({"error": "content is required"}), 400

    with engine.begin() as conn:
        conn.execute(text("INSERT INTO notes (content) VALUES (:content)"), {"content": content})

    return jsonify({"status": "ok"}), 201

if __name__ == "__main__":
    wait_for_db()
    init_db()
    app.run(host="0.0.0.0", port=APP_PORT)

