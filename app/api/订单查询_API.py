# api/旧订单_API.py

from fastapi import APIRouter
from ..mongo.订单查询 import 查询旧订单

路由 = APIRouter()


@路由.get("/订单")
async def 获取旧订单():
    return 查询旧订单()
