'''
money=50
goods=10;
print("余额：",money)
money-=goods

#print("购买商品：",-goods)
print("购买商品余额：",money)
'''
'''i=999.99

print(int(i));

print("/”转义字符")
'''
'''
name="刘淼"
age=30
#print(str(age)+name)
add="刘淼 %s" % age
print(add)

class_num=43
avg_money=6000
message="IT 第%s期 平均工资%s"%(class_num,avg_money)
print(message)
'''''
'''
n1=11
n2=1234234321.1111111111111
print("宽度限制5 %-5d"%n1)  #正 负 号 控制左右对其
print("宽度限制1 %1d"%n1)
print("宽度限制5 %-7.2f"%n2)
print("宽度限制1 %.2f"%n2)

print("2*2=%d"%(2*2))
'''
name="强盛集团"
stock_price=18.8
stock_Code="001234"
stock_daily_growth=1.2
growth_day=7
ENDSUM=stock_price*growth_day**stock_daily_growth
print( "%s 股票价格:%d 涨幅%2f 天数%d 今价%.2f"%(name,
       stock_price,stock_daily_growth,growth_day,ENDSUM))