# app/api/目录_API.py
from fastapi import APIRouter, HTTPException
from typing import List
import os
from pathlib import Path

router = APIRouter()


@router.get("/目录/{目录名称:path}", response_model=List[str])
async def 读取目录内容(目录名称: str):
    当前文件路径 = Path(__file__).resolve()
    项目根目录路径 = 当前文件路径.parent.parent.parent
    完整目录路径 = 项目根目录路径 / 目录名称
    基础目录 = 项目根目录路径 / "小说目录"

    print(完整目录路径)
    print('E:\python项目\\fastApiProject\小说目录\我大明武德充沛')
    # 检查目录是否存在
    if not 完整目录路径.exists():
        raise HTTPException(status_code=404, detail="目录不存在")

    # 检查路径是否为一个目录
    if not 完整目录路径.is_dir():
        raise HTTPException(status_code=400, detail="请求的路径不是一个目录")

    文件相对路径列表 = []
    for 文件 in 完整目录路径.iterdir():
        if 文件.is_file():
            # 计算文件的相对路径，并使用斜杠作为目录分隔符
            相对路径 = 文件.relative_to(基础目录).as_posix()
            文件相对路径列表.append(相对路径)

    return 文件相对路径列表
