# mongo/订单查询.py
from 数据库连接 import 创建数据库连接


def 查询旧订单():
    客户端 = 创建数据库连接()
    数据库 = 客户端['Data']
    旧订单集合 = 数据库['旧订单']
    查询结果 = 旧订单集合.find({})
    return list(查询结果)




if __name__ == "__main__":
    查询结果 = 查询旧订单()
    print("查询到的旧订单数量:", len(查询结果))
    for 序号, 订单 in enumerate(查询结果):
        if 序号 < 10:
            print(订单)
        else:
            break