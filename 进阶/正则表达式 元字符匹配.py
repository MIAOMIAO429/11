import re

s="liumiao ##6ZZZZZ66#% 刘淼 x0429x ccCCC*?"
# #找数字
# result1=re.findall(r'\d',s)#字符串前面加上 r 表示转义字符无效 为普通字符
# print(result1)
#
# #找出特殊字符
# result2=re.findall(r'\W',s)
# print(result2)

#找出英文字母
result3=re.findall(r'[a-zA-Z]',s)
print(result3)

#找出英文字母 数字
result3=re.findall(r'[0-9 A-z]',s)
print(result3)