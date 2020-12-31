# _author:YITLIU
# Date: 2020/12/31


# 元组

tupleA = ('a', 'b')
for i, v in enumerate(tupleA, 1):
    #print(i, "+", v)
    pass
# 判断字符是否为数字
#print("22".isdigit())

# 字典

dictB = {
    "xh": 23,
    "xx": 24
}
# id() 查询对象的内存地址
#print(id(dictB))

# 字典增删改查
dictB.setdefault("xh", 23)
dictB["xh"] = 24
dictB["zyw"] = 25
dictB.pop("zyw")
print(dictB)

