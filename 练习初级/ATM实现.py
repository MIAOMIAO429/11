#定义全局变量
money=50000000
name=None
#输入用户姓名
name=input("请输入您的姓名: ")
#查看余额
def query(show_header):
    if show_header:
        print("-----查询余额----")
    print(f"{name},您的余额为{money}元")
#存款
def saving(num):
    global  money
    money+=num
    print("------存款------")
    print(f"{name},您存款{money}元成功")
    query(False)
#取款
def get_money(num):
    global  money
    money -= num
    print("------取款------")
    print(f"{name},您取款{money}元成功")
    query(False)

#菜单
def main():
    print(f"{name}你好，欢迎淼淼银行")
    print("1\t\t余额余额")
    print("2\t\t存款")
    print("3\t\t取款")
    print("0\t\t退出")
    return  input("请输入你的选择 ")


while True:
    keyboard_input=main()
    if keyboard_input=='1':
        query(True)
        continue
    elif keyboard_input == '2':
        num=float(input("请输入存入金额 "))
        saving(num)
        continue
    elif keyboard_input == '3':
        num = float(input("请输入取出金额 "))
        get_money(num)
        continue
    else:
        print("退出")
        break




