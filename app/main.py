# 项目的主入口文件 main.py
from fastapi import FastAPI
from .api.目录_API import router as 目录_router
from .api.TXT文件_API import router as txt_router

app = FastAPI()

app.include_router(txt_router)
app.include_router(目录_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
