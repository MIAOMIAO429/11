# import  random
# num=random.randint(1,10)
# print(num)
# guess_num=int(input("输入猜测数字"))
# if guess_num==num:
#     print("猜中了")
# else:
#
#     if guess_num > num:
#         print("猜大了")
#     if guess_num < num:
#         print("猜小了")
# guess_num=int(input("输入猜测数字"))
# if guess_num==num:
#     print("猜中了")
# else:
#
#     if guess_num > num:
#         print("猜大了")
#     if guess_num < num:
#         print("猜小了")
# guess_num=int(input("输入猜测数字"))
# if guess_num==num:
#     print("猜中了")
# else:
#
#     if guess_num > num:
#         print("猜大了")
#     if guess_num < num:
#         print("猜小了")



import  random
num=random.randint(1,100)
flag=True
count=0
while (flag):
    count+=1
    print(num)
    guess_num=int(input("输入猜测数字"))
    if guess_num==num:
        print("猜中了")
        flag=False
    else:

        if guess_num > num:
            print("猜大了")
        if guess_num < num:
            print("猜小了")

print(count)