from fastapi import FastAPI
from sqlalchemy import MetaData, Table, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from fastapi.middleware.cors import CORSMiddleware


# Testing
# DATABASE_URL = "postgresql+asyncpg://fastapiuser:fastapi37811@localhost:5432/fastapidb"
# Production
# DATABASE_URL = "postgresql+psycopg2://ufo30bm52onkok:pd17fb510bee0d9e5ee2defb9a9d002afeaeead55b9e9a80478940f8b8d039737@c6oob9dspeco5.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d9lpb17qpeanjp"
DATABASE_URL = "postgresql+asyncpg://ufo30bm52onkok:pd17fb510bee0d9e5ee2defb9a9d002afeaeead55b9e9a80478940f8b8d039737@c6oob9dspeco5.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d9lpb17qpeanjp"



engine = create_async_engine(DATABASE_URL, echo=True)
metadata = MetaData()
app = FastAPI()

@app.get("/api/program-pages")
async def get_program_pages():
    async with engine.connect() as conn:
        # Reflect inside run_sync
        await conn.run_sync(metadata.reflect)
        program_pages_table = Table("django_fastapi_programpage", metadata, autoload_with=conn)
        result = await conn.execute(select(program_pages_table))
        rows = result.fetchall()

        pages = [
            {
                "id": row.id,
                "title": row.title,
                "description": row.description,
                "benefits": row.benefits,
            }
            for row in rows
        ]
    return pages


@app.get("/test")
async def root():
    return {"message": "Hello World. learners"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


origins = [
    "http://localhost:3000",             # React local dev
    "https://codethinkers.netlify.app",  # Your deployed React site
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # restrict to these domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
