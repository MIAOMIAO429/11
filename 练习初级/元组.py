shu1=(1,2,3,4,5)
shu2 =()# 空元组
shu3=tuple()# 空元组
football=["足球"]
music=["弹钢琴"]
JL=("周杰伦",55,[football],[music])
for x in JL:
    print(x)
w1={JL.index(55)}
w2={JL.index("周杰伦")}
print(f"位置1{w1} 位置2{w2}")
football.remove("足球")
music.append("打游戏")
L=("周杰伦",55,[football],[music])
for x in JL:
    print(x)

