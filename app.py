import os

import asyncpg
from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
async def healthz():
    return {"ok": True}


@app.get("/hello")
async def healthz():
    return {"ok": "hello there"}


@app.post("/add-user")
async def add_user(name: str, email: str):
    dsn = os.getenv("DATABASE_URL")
    conn = await asyncpg.connect(dsn)
    try:
        await conn.execute("INSERT INTO users (name, email) VALUES ($1, $2)", name, email)
        return {"ok": True}
    finally:
        await conn.close()


@app.get("/list-users")
async def list_users():
    dsn = os.getenv("DATABASE_URL")
    conn = await asyncpg.connect(dsn)
    try:
        rows = await conn.fetch("SELECT id, name, email FROM users")
        return [dict(r) for r in rows]
    finally:
        await conn.close()


@app.get("/db-ping")
async def db_ping():
    dsn = os.getenv("DATABASE_URL")
    conn = await asyncpg.connect(dsn)
    try:
        val = await conn.fetchval("select 1")
        return {"db": val}
    finally:
        await conn.close()
