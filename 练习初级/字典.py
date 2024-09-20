'''''
#定义字典
zidiao={"刘淼":"20","周杰伦":"50"}
zidian2={}
zidiao3=dict()
print(zidiao)
print(zidian2)
#Key找Valve
zi=zidiao["刘淼"]
print(f"{zi}")
#字典嵌套
StuScoreDict={
    "刘淼":{
        "语文":66,
        "数学":66,
        "英语":66,
    },"小莫":{
        "语文":88,
        "数学":88,
        "英语":88,
    },"龙傲天":{
        "语文":100,
        "数学":100,
        "英语":100,

    }
}
print(f'小莫{StuScoreDict["小莫"]}')
StuScoreDict["刘淼"]={"语文":100,
        "数学":80,
        "英语":10,}
print(f'刘淼{StuScoreDict["刘淼"]}')
StuScoreDict.pop("小莫")

print(StuScoreDict.keys())
len1=len(StuScoreDict)
print(len1)

'''''
Dict={
    "王力宏":{
        "部门":"科研部",
        "工资":3000,
        "级别":1

    },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },
    "林俊杰":{
        "部门":"市场部",
        "工资":7000,
        "级别":3
    },
    "张学友":{
        "部门":"科研部",
        "工资":4000,
        "级别":1
    },
    "刘德华":{
        "部门":"市场部",
        "工资":6000,
        "级别":1
    }
}
for X in Dict:

    if Dict[X]["级别"]==1:
        Dict[X]["级别"] += 1
        Dict[X]["工资"]+=1000


print(Dict)

