import socket


def client(host, port):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, port))

    print("connent to server = {0}, port = {1}".format(host, port))
    return c


client = client("192.168.200.2", 8000)

while True:
    cmd = "Please input msg:"
    cmd = bytes(cmd, 'UTF-8')
    client.send(cmd)
    data = client.recv(1024)
    print(data)
