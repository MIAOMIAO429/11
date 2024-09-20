# try:
#     f=open("E:/Python合/xxx.txt","r",encoding="UTF-8")
# except:
#     print("异常")
#     f = open("E:/Python合/xxx.txt", "a", encoding="UTF-8")
#指定多个异常捕获
try:
    print(lm)
    print(1/0)
except (NameError,ZeroDivisionError) as e:
    print(e)
    print("变量未定义异常")
