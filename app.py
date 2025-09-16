from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, select

app = FastAPI()



@app.get("/test")
async def root():
    return {"message": "Hello World 222"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Testing
# DATABASE_URL = "postgresql+psycopg2://fastapiuser:fastapi37811@localhost:5432/fastapidb"
# Production
DATABASE_URL = "postgresql+psycopg2://ufo30bm52onkok:pd17fb510bee0d9e5ee2defb9a9d002afeaeead55b9e9a80478940f8b8d039737@c6oob9dspeco5.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d9lpb17qpeanjp"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

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
                "benefits": row.benefits,
            }
            for row in result.fetchall()
        ]
    return pages
