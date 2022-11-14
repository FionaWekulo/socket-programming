import socket
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1024))
server.listen(5)
while True:
    client, address=server.accept()
    print(f"Connection to {address} has been established")
    client.send(bytes(" SOCKET PROGRAMMING.\n ***********************************\n Established a connection between client and server.\n Client calls print procedure.\n Server executes the called procedure.\n Server sends response back to client where it is display.", "utf-8"))
    client.close()