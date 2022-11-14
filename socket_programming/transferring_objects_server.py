import socket
import pickle

a=10 #header size
s-socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),2133))     #binding tuple
s.listen(5)
while True:
    clt,address=s.accept()
    print(f"Connection to {address} estblished")
    m={1:"Client", 2:"Server"}
    mymsg = pickle.dumps(m)     #the message you want to print later
    mymsg =  bytes(f'{len(mymsg):<={a}}',"utf-8") + mymsg
    clt.send(mymsg)
