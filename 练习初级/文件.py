import time

#f=open("E:/Python合/6666.txt","r",encoding="UTF-8")
# print(type(f))
# # print(f.read()) #读取
# #
# # list1=f.readline()
# # print(f"list{list1}")
# # print(type(list1))
# list2=f.readline()
# print(list2)
# list2=f.readline()
# print(list2)
# list2=f.readline()
#
# print(list2)
# list2=f.readline()
# print(list2)
# list2=f.readline()
# print(list2)
# with open("E:/Python合/123.txt","r",encoding="UTF-8") as f:
#     for line in f:
#         print(line)

f=open("E:/Python合/6666.txt","w",encoding="UTF-8")
f.write("晚安 酷酷酷")
time.sleep(3)
f.flush()
f.close()
