# _author:YITLIU
# Date: 2021/1/7


'''
    深copy和浅copy
'''


s = [[1, 2], 'alex', 'alvin']

# 浅拷贝
s1 = s.copy()
s1[0][0] = 2
print(s)
print(s1)

# 深拷贝
s2 = s

"""
    集合
    1.唯一一种定义集合的方法：set() 
    2.集合是一种不可哈希对象  
    3.集合运算
"""
# set()可以去重
s = set([1, 2, 3])
#s.add("asd")
s.update("asd")
s.clear()
print(s)
print(type(s))

# 交集
s.intersection()
# 并集
s.union()
# 差集
s.difference()
