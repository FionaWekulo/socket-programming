import socket
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((socket.gethostname(), 1024))
complete_information=''
while True:
    message=server.recv(1024)
    if len(message)<=0:
        break
    complete_information += message.decode("utf-8")
    print(complete_information)
