#匹配账号 只能由字母数字 组成 长度限制 6-10位
import re

# r1='^[0-9 a-z A-Z ]{6,10}$'#规则
# s="125rerwefa"
# print(re.findall(r1,s))



# #匹配QQ号  纯数字 长度限制 5-10位 第一位 不为0
# r2='^[1-9][0-9]{4,10}$'
#   # 数量要求  长度要求
# s="1234566"
# print(re.findall(r2,s))


#匹配邮箱地址 只允许 qq 163 gmail 三种邮箱地址
#{内容}.{内容}@{内容}.{内容}
#3085755899@qq.com
r3=r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w]+)+$)'
s="30857asdas55asdas899@qq.com"
#print(re.findall(r3,s))
print(re.match(r3,s).group())