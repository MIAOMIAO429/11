def ATMOn(initial_amount=0):
    def ATMIn(num,deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount +=num

            print(f"存款+{num} 账户余额{initial_amount}")
        else:
            initial_amount -= num

            print(f"取款-{num} 账户余额{initial_amount}")

    return ATMIn

atm=ATMOn()
atm(100)
atm(666)
atm(100,deposit=False)