''''
print("欢迎来到 游乐园")
age=(int(input()))

if age<18:
	print("免费玩")
else:
	print("买票")
	'''''

# age =(int(input()))
# if age<18:
# 	print("不可以PC了")
# 	print("可以PC了")
# elif age<60:
# 	print("有点危险，可以PC了")
# else:
# 	print("太老了，别玩了")

age=55
money=300
if age>=18 :
    print("你是成年人了")
    if 0 <= money < 1000:
        print("可以PC")
    elif money>=2000:
        print("可以玩高端PC")
else:
    print("你未成年，不可以玩PC")