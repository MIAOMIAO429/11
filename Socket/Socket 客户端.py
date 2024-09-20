import socket
#创建 socket对象
socket_client=socket.socket()

#链接服务端
socket_client.connect(("localhost",8888))#链接地址  回环地址127.0.0.1
while True:
    #发送信息
    msg=input("请输入发送服务端信息：")
    if msg == "exit":
        break
    socket_client.send(msg.encode("UTF-8"))

    #接收信息
    recv_data=socket_client.recv(1024)
    print(f"服务端回复信息：{recv_data.decode('UTF-8')}")


socket_client.close()