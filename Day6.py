# _author:YITLIU
# Date: 2021/1/5

# 1 - f.seek()调整读文件指针位置

# with open("README.md", "r", encoding="utf8") as f:
#     print(f.tell())
#     print(f.read(8))
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())

# 2 - 文件写入可以用flush()直接刷入内存
#
# import sys,time
#
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     # print("",end="",flush = True) 可以实现同样的效果
#     time.sleep(1)

# 3 - truncate()截断
# num = 0
# with open("README.md", "r+", encoding="utf8") as f:
#     with open("README1.md", "w", encoding="utf8") as f1:
#     # f.truncate(5)
#     # print(f.isatty())
#     # print(f.readline())
#     # f.readline()
#     # print(f.tell())
#     # f.write("hello")
#         for i in f:
#             num s+= 1
#             if num == 2:
#                 i = "".join([i, "kevin"])
#             f1.write(i)


# 4 - 文件追加模式
#
# with open("README.md", "a", encoding="utf8") as f:
#     print(f.write("222"))

with open("workface.txt", "r", encoding="utf-8") as f:
    print(type(eval(f.readline())))