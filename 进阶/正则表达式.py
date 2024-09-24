import re

''''
s1="Python 我的最爱！"
result=re.match("Python",s1)  #从头匹配 头部不匹配 返回None
print(result)
print(result.span())#打印位置区间 （0,6） 不包含6
print(result.group())#打印


s2="123123Python 我的最爱！"
result=re.search("我的最爱",s2)
print(result)
print(result.group())
'''
s3="1231我的最爱23Pyt我的最爱hon 我的最爱！"
result=re.findall("我的最爱",s3)
print(result)
