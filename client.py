
import socket
import json
import random

def createUnique():
    randomString = ''
    li = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f']
    for i in range(32):
        if(i==8 or i==13 or i==18):
            randomString+='-'
        randomString+=str(li[random.randint(0, len(li)-1)])
    return randomString

def client_program():
    obj = {}
    host = '192.168.168.236'
    port = 5000
    while True:
        client_socket = socket.socket()  
        client_socket.connect((host, port))  
        message = input(" -> ")
        randomString = createUnique()
        obj['method'] = message
        obj['id'] = randomString
        json_dump = json.dumps(obj)
        json_obj = json.loads(json_dump)
        print(json_obj)
        client_socket.send(bytes(str(obj).encode()))
        print(client_socket.recv(1024))
        client_socket.close()


if __name__ == '__main__':
    client_program()
