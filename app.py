import asyncpg
import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
async def healthz():
    return {"ok": True}


@app.get("/hello")
async def healthz():
    return {"ok": "hello there"}


@app.get("/db-ping")
async def db_ping():
    dsn = os.getenv("DATABASE_URL")
    conn = await asyncpg.connect(dsn)
    try:
        val = await conn.fetchval("select 1")
        return {"db": val}
    finally:
        await conn.close()
