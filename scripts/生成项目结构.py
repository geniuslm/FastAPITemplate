import os

def 打印目录结构(根目录, 排除列表=[], 缩进前缀=''):
    目录项列表 = sorted(os.listdir(根目录), key=lambda x: (not os.path.isdir(os.path.join(根目录, x)), x))
    目录项总数 = len([目录项 for 目录项 in 目录项列表 if 目录项 not in 排除列表])
    处理过的目录项数量 = 0

    for 目录项 in 目录项列表:
        if 目录项 in 排除列表:
            continue

        处理过的目录项数量 += 1
        路径 = os.path.join(根目录, 目录项)
        是目录 = os.path.isdir(路径)
        是最后一个目录项 = 处理过的目录项数量 == 目录项总数

        前缀 = '└── ' if 是最后一个目录项 else '├── '
        子项缩进前缀 = 缩进前缀 + ('     ' if 是最后一个目录项 else '│    ')

        if 是目录:
            print(f'{缩进前缀}{前缀}{目录项}\\')
            打印目录结构(路径, 排除列表, 子项缩进前缀)
        else:
            # 确保在根目录下最后一个文件使用正确的符号
            print(f'{缩进前缀}{前缀}{目录项}')




排除列表 = ['小说目录','.nuxt','.idea','.venv','node_modules', '.git', '其他不需要的目录或文件',
            '.output', '.vscode', 'node_modules','components','__pycache__']
根目录 = os.getcwd()  # 获取当前工作目录
print(f'{根目录}\\')
打印目录结构(根目录, 排除列表)
