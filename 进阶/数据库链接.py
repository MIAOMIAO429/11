from  pymysql import Connect
conn=Connect(

    host="127.0.0.1", #主机名称
    port=3306,        #端口
    user="root",      #账户
    password="123456",#密码 password
    autocommit=True   #自动提交


)
#print(conn.get_server_info())
cursor=conn.cursor()  #游标对象
#选择已有的数据库
conn.select_db("myku")
#执行SQL 语句
#新创建表
#cursor.execute("create table test_pymysql(id int)")
'''''
#插入
cursor.execute("insert into stu values(004,'小莫',36)")
#数据修改 提交确认
#conn.commit()
'''''
#查询
cursor.execute("select * from stu") #from
results=cursor.fetchall()
print(type(results))
#print(results)
for r in results:
    print(r) #查表


#关闭数据库
conn.close()