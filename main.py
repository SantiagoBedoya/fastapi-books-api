import uvicorn
from fastapi import FastAPI
from db.config import engine, Base
from routers import book_router

app = FastAPI()
app.include_router(book_router.router)

@app.get('/healthcheck')
async def healthcheck():
    return {"status": "OK"}


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host='127.0.0.1', reload=True)