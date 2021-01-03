# _author:YITLIU
# Date: 2021/1/1

# 三级菜单

# placeProvince = {
#     "01": "湖南省",
#     "02": "湖北省"
# }
#
# placeCity = {
#     "01": {
#         "011": "常德市",
#         "012": "益阳市"
#     }
# }
# placeCounty = {
#     "011": {
#         "0111": "汉寿县",
#         "0112": "石门县"
#     }
# }
#
# placeIndex = {
#     "Province": "",
#     "City": "",
#     "County": ""
# }
#
# flag = True
# while flag:
#     if placeIndex["Province"] == "":
#         for key, value in placeProvince.items():
#             print(key, "-", value)
#         place = input("选择:")
#         if place in placeProvince.keys():
#             placeIndex["Province"] = place
#             print("当前位置：%s" % (placeProvince[placeIndex["Province"]]))
#         else:
#             print("请输入正确的省份")
#     elif placeIndex["Province"] != "" and placeIndex["City"] == "":
#         for key, value in placeCity[placeIndex["Province"]].items():
#             print(key, "-", value)
#         place = input("选择:")
#         if place in placeCity[placeIndex["Province"]].keys():
#             placeIndex["City"] = place
#             print("当前位置：%s-%s" % (placeProvince[placeIndex["Province"]], placeCity[placeIndex["Province"]][placeIndex["City"]]))
#         else:
#             print("请输入正确的市")
#     else:
#         order = input("1.返回上一级 2.退出")
#         if order == "1":
#             placeIndex["City"] = ""
#         elif order == "2":
#             flag = False

# flag = False
# while not flag:
#     print("在第一层")
#     inputSelect = input("要不要继续：").lstrip()
#     if inputSelect == "1":
#         while not flag:
#             print("在第二层")
#             inputSelect1 = input("要不要继续：").lstrip()
#             if inputSelect1 == "1":
#                 pass
#             else:
#                 break
#
#     else:
#         break
