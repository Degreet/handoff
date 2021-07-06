import socket

users = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.103', 9090))
server.listen(2)

while True:
    user_socket, address = server.accept()
    users.append(user_socket)

    data = server.recv(2048).decode('utf-8')

    if data:
        for user in users:
            user.send(data)
