from socket import *
s = socket(AF_INET,SOCK_STREAM) 
s.bind(("",8000))
s.listen(5)
print("----------------CHAT APPLICATION--------------")
c,a=s.accept()
while True:
    data=c.recv(100).decode()
    print("<--",data)
    if(data=="bye" or ""):
        p="bye"
        c.send(p.encode('utf-8'))
        print("Chat End")
        break
msg=input("-->",)
c.send(msg.encode('utf-8'))