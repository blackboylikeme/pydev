# _author:YITLIU
# Date: 2021/1/4

# 文件操作

# with open('book.txt', 'r+', encoding='utf8') as f:
#     data = f.read()
#     print(data)


# f.readlines 读取全部内容至内存
# with open('README.md', 'r+', encoding='utf8') as f:
#     for i in f.readlines():
#         print(i.strip())

#
with open('README.md', 'r+', encoding='utf8') as f:
    for i in f:

        print(i.strip())
