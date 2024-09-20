''''

class Phone1:
    IMEI=None
    producer="HH"


    def call_4G(self):
        print("4G通话")


class Phone2(Phone1):

    face_id="11100"
    def call_5G(self):
        print("5G通话")


phone=Phone2()
phone.call_4G()
phone.call_5G()
'''
class NFC:
    Id=1000
    def nfc(self):
        print("父类 NFC ")
class TF:
    def TF(self):
        print("TF读卡器")
class XIAOMI(NFC,TF):

    def phone(self):
        print("小米手机")
        pass#空空

    def nfc(self):
        print("子类 NFC ")

my_phone=XIAOMI()
my_phone.nfc()
my_phone.TF()
my_phone.phone()
print(f"{NFC.Id}")
NFC.nfc(self=0)