import socket
import os
import json


def server_program():
    host = '192.168.168.236'
    port = 5002

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port)) 
    server_socket.listen()
    print('listening...')
    while True:
        conn, addr = server_socket.accept()
        print("Connection from: " + str(addr))
        data = conn.recv(1024).decode()
        data = eval(str(data))
        data = json.dumps(data)
        data = json.loads(data)
        # print("from connected user: " + str(data))
        # conn.sendall(b'some')
        print(data)
        print(os.system(data['method']))
        conn.send(bytes(str(os.popen(data['method']).read()).encode()))
        conn.close()


if __name__ == '__main__':
    server_program()
