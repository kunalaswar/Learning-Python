
import socket
while(True):
    s= socket.socket()
    s.connect(("localhost",8558)) 
    cdata =input("Student --->")
    if (cdata.lower() =="bye"):
        s.send(cdata.encode())
        break
    else:
        s.send(cdata.encode())
        sdata = s.recv(1024).decode()
        print("KVR --->",sdata)


