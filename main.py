from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
async def welcome():
    return {"message": "Welcome to Codethinkers Academy 🚀"}


import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/slow")
async def slow():
    await asyncio.sleep(3)  # ⏳ Simulate heavy task
    return {"message": "Done after 3 seconds"}
