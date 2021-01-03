# _author:YITLIU
# Date: 2021/1/3

# 三级菜单改进

placeProvince = {
    "湖南省": {
            "常德市": {
                    "汉寿县": {},
                    "石门县": {}
                    },
            "益阳市": ""
            }
}

# placeIndex控制三级菜单层级
placeIndex = [None, None]
selectPlace = placeProvince
flag = True
while flag:

    for keys in selectPlace.keys():
        print(keys)

    place = input("选择:")
    if place in selectPlace.keys():
        selectPlace = selectPlace[place]
        if placeIndex[0] == None:
            placeIndex[0] = place
        elif placeIndex[1] == None:
            placeIndex[1] = place
    elif place == "b":
        if placeIndex[1] != None:
            selectPlace = placeProvince[placeIndex[0]]
            placeIndex[1] = None
        else:
            selectPlace = placeProvince

    else:
        flag = False


