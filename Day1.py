# _author:YITLIU
# Date: 2020/12/30

import random


randomAge = random.randrange(20, 25)
print(randomAge)

while True:
     inputAge = int(input("请输入我的年龄："))
     if inputAge == randomAge:
         print("你猜对了")
         break
     else:
         print("差点就对了！")

def bigOne(list):
    '''
    :param list:
    :return: 最大值
    '''
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

print(bigOne([1,5,4]))

names = "zhangsan zhangsan lisi wangwu"
print(names.index("h"))
listName = names.split(" ")
#listName.remove("zhangsan")
# listName.pop(1)
listName.reverse()
print(listName)
for i in listName:
    print(i)

