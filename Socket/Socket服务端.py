import socket
#创建socket 对象
socket_server=socket.socket()

#绑定 socket_server 到指定IP地址  端口
socket_server.bind(("localhost",8888))#绑定地址  回环地址127.0.0.1
#监听端口
socket_server.listen(1)
#.listen(1) 接受整数 表示接受链接数量

#等待客户端链接
result=socket_server.accept()
conn=result[0]
addess=result[1]
#  等同==   conn,addess=socket_server.accept()
#accept() 方法返回的是 二元元组（链接对象,客户端信息）
#可以通过 变量1 ，变量2 = socket_server.accept()  的形式，直接接受二元元组的两个元素
#accept() 方法  阻塞方法 等待客户端链接 如果没有来拿货一直等待
print(f"接收到了客户端的链接，客户端的信息{addess}")
while True:
    #接收客户端信息 使用客户端和服务端 本次链接对象，而非socket_server
    data:str=conn.recv(1024).decode("UTF-8")
    #recv 接受的参数是缓冲区大小  一般给1024
    #recv方法 返回值是 字节数组也就是 Bytes  不是字符串   字节数组 （用UTF-8编码）——>字符串
    print(f"客户端发来的信息：{data}")
    #发送回复信息

    msg=str(input(f"请输入回复信息:"))

    if msg=="exit":
        break
    #字符串（用UTF-8解码）——>字节数组
    conn.send(msg.encode("UTF-8"))


#关闭链接
conn.close()
socket_server.close()