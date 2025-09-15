from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/welcome")
async def welcome():
    return {"message": "Welcome to Codethinkers Academy 🚀"}

@app.get("/slow")
async def slow():
    await asyncio.sleep(3)
    return {"message": "Done after 3 seconds"}

from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, select

DATABASE_URL = "postgresql+psycopg2://fastapiuser:fastapi37811@localhost:5432/fastapidb"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

app = FastAPI()

@app.get("/api/program-pages")
async def get_program_pages():
    metadata.reflect(bind=engine)
    program_pages_table = Table("django_fastapi_programpage", metadata, autoload_with=engine)
    with engine.connect() as conn:
        result = conn.execute(select(program_pages_table))
        pages = [
            {
                "id": row.id,
                "title": row.title,
                "subtitle": row.subtitle,
                "description": row.description,
                "cta_text": row.cta_text,
                "benefits": row.benefits
            }
            for row in result.fetchall()
        ]
    return pages
