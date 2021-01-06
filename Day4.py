# _author:YITLIU
# Date: 2021/1/3

# 三级菜单改进
    # 1.展示省市县（数据存在文件中）
    # 2.对菜单实现增删改

#  思路：
    # 1.首先创建一个txt文件
    # 2.奖数据字典放到txt文件中
    # 3.读txt内容
    # 4.eval（）将str转化成dict格式
    # 5.实现当前层级字典新增
    # 6.实现当前层级字典删除
    # 7.实现当前层级字典修改

# placeProvince = {
#     "湖南省": {
#             "常德市": {
#                     "汉寿县": {},
#                     "石门县": {}
#                     },
#             "益阳市": {}
#             }
# }
def readFile():
    with open("workface.txt", "r+", encoding="utf8") as f:
            data1 = eval(f.readline())
    return data1

def writeFile(data):
    with open("workface.txt", "w", encoding="utf-8") as f:
        f.write(data)

def simple(placeIndex):
    pass
# placeIndex控制三级菜单层级
placeIndex = []
data = readFile()

flag = True
while flag:
    if len(placeIndex) == 1:
        selectPlace = readFile()[placeIndex[0]]
    elif len(placeIndex) == 2:
        selectPlace = readFile()[placeIndex[0]][placeIndex[1]]
    elif len(placeIndex) == 0:
        selectPlace = readFile()
    for keys in selectPlace.keys():
        print(keys)

    place = input("选择:")
    if place in selectPlace.keys():
        selectPlace = selectPlace[place]
        if len(placeIndex) == 0:
            placeIndex.append(place)
        elif len(placeIndex) == 1:
            placeIndex.append(place)
    elif place == "b":
        if len(placeIndex) == 2:
            selectPlace = data[placeIndex[0]]
            placeIndex.pop(1)
        else:
            selectPlace = data
    elif place.split(" ")[0] == "add":
        if len(placeIndex) == 1:
            data[placeIndex[0]][place.split(" ")[1]] = {}
        elif len(placeIndex) == 2:
            data[placeIndex[0]][placeIndex[1]][place.split(" ")[1]] = {}
        else:
            data[place.split(" ")[1]] = {}
        writeFile(str(data))

    elif place.split(" ")[0] == "delete":
        if len(placeIndex) == 1:
            del data[placeIndex[0]][place.split(" ")[1]]
        elif len(placeIndex) == 2:
            del data[placeIndex[0]][placeIndex[1]][place.split(" ")[1]]
        else:
            del data[place.split(" ")[1]]
        writeFile(str(data))

    elif place.split(" ")[0] == "update":
        if len(placeIndex) == 1:
            data[placeIndex[0]][place.split(" ")[1]] = eval(place.split(" ")[3])
        elif len(placeIndex) == 2:
            data[placeIndex[0]][placeIndex[1]][place.split(" ")[1]] = eval(place.split(" ")[3])
        else:
            data[place.split(" ")[1]] = eval(place.split(" ")[3])
        writeFile(str(data))

    else:
        flag = False


