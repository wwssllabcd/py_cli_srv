import socket


def server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("start server = {0}, port = {1}".format(host, port))
    return s


serversocket = server(socket.gethostname(), 8000)
(clientsocket, address) = serversocket.accept()

while True:
    try:        
        print("get clientsocket= {0}, addr={1}".format(clientsocket, address))
        while True:
            data = clientsocket.recv(1024)
            clientsocket.sendall(data)
    except:
        print("error")