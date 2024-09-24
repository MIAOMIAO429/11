import threading
import time


def sing():
    while True:
        print("在唱歌 啦啦啦啦啦啦....")
        time.sleep(1)
def dance():
    while True:
        print("在跳舞 哔哔哔哔哔哔....")
        time.sleep(1)
def RAP(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    #创建两个线程  ==   两个员工
    sing_thrad=threading.Thread(target=sing)#唱歌
    dance_thrad = threading.Thread(target=dance)#跳舞
    rap_thrad = threading.Thread(target=RAP,args=("我是rap",))#args元组传参
    #启动                                           加,   识别元组
    sing_thrad.start()
    dance_thrad.start()
    rap_thrad.start()
