class Phone:

    __current_voltage=0.5 #私有成员变量

    def __keep_work(self): #私有成员方法
        print("单独 工作")
    def call_5G(self):
        if self.__current_voltage>=1:
            print("开启5G通话")
        else:
            print("开启5G通话,失败")
    __is_5G=False
    def IS_5G(self):
        if self.__is_5G==True:
            print("开启5G通话啦啦啦啦啦")
        else:
            print("开启5G通话,失败5555")



phone=Phone()
#phone.__keep_work     #报错
#print(phone.current_voltage)  #报错
#phone.call_5G()
phone.IS_5G()