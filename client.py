import pyperclip
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.103', 9090))


temp_cb = pyperclip.paste()

while True:
    data = client.recv(2048).decode('utf-8')
    new_cb = pyperclip.paste()

    if data:
        print('copy')
        pyperclip.copy(data)

    if temp_cb != new_cb:
        print('paste')
        temp_cb = new_cb
        client.send(new_cb.encode('utf-8'))
