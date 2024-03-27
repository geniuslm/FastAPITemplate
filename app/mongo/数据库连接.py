# mongo/数据库连接.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

def 创建数据库连接():
    """
    连接到 MongoDB 数据库。
    返回一个 MongoClient 实例。
    """
    连接字符串 = os.getenv('MONGODB_URI')
    客户端 = MongoClient(连接字符串)
    return 客户端


# 示例：使用这个函数来获取数据库实例
if __name__ == "__main__":
    客户端 = 创建数据库连接()
    数据库 = 客户端['Data']  # 替换为你的数据库名称
    集合 = 数据库['旧订单']  # 替换为你想要访问或创建的集合名称
    # 列出所以集合
    print(数据库.list_collection_names())

