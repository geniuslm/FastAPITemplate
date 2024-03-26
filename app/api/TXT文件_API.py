# app/api/TXT文件_API.py

from fastapi import APIRouter, HTTPException
from pathlib import Path
from typing import List

router = APIRouter()

@router.get("/获取文本内容/{文件路径:path}")
async def 获取文本内容(文件路径: str):
    基础目录 = Path("小说目录")  # 指向您的小说目录
    完整文件路径 = 基础目录 / 文件路径

    # 确保文件路径安全，避免路径遍历攻击
    if not 完整文件路径.is_file() or not 完整文件路径.exists() or ".." in 文件路径:
        raise HTTPException(status_code=404, detail="文件不存在或路径不安全")

    # 读取并返回文件内容
    try:
        with open(完整文件路径, "r", encoding="utf-8") as 文件:
            内容 = 文件.read()
        return {"文件内容": 内容}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"读取文件时发生错误: {e}")
