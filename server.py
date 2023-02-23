import socket
import time

HEADER_SIZE = 10
# socket.AF_INET -> IPv4
# socket.SOCK_STREAM -> TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket is the end point that recieves data
s.bind(('192.168.2.151', 1237))
# s.connect(('192.168.3.1', 1235))
# queue of 5 clients
s.listen(5)

full_msg = ''
new_msg = True
clientsocket, address = s.accept()
print(f"connected with {address}")
while True:
    msg = clientsocket.recv(HEADER_SIZE)
    msgLen = int(msg)
    msg = msg + clientsocket.recv(msgLen)

    if float(msg[HEADER_SIZE:]) <= 11.0:
        print('STOP')
    else:
        print(float(msg[HEADER_SIZE:]))
    # if new_msg:
    #     print(f'the length of the message is:{msg[:HEADER_SIZE]}')
    #     msgLen = int(msg[:HEADER_SIZE])
    #     new_msg = False

    # full_msg += msg.decode('utf-8')
    # print((len(full_msg) - HEADER_SIZE))
    # # print(full_msg)

    # if len(full_msg) - HEADER_SIZE == msgLen:
    #     print('entire message recovered!')
    #     print(f'{full_msg[HEADER_SIZE:]}')
    #     new_msg = True
    #     full_msg = ''
    #     break

# while True:
#     msg = "Welcome to the raspberry pi!"
#     msg = f'{len(msg):<{HEADER_SIZE}}' + msg
#     clientsocket, address = s.accept()
#     print(f'Connection from {address} has been established!')
#     clientsocket.send(bytes(msg, "utf-8"))

    # while True:
    #     time = time.sleep(3)
    #     msg = f'the time is:{time.time()}'
    #     msg = f'{len(msg):<{HEADER_SIZE}}' + msg
    #     clientsocket.send(bytes(msg, "utf-8"))
    # msg = s.recv(1024)
    # msg = msg.decode('utf-8')
    # print(msg)

    # clientsocket, address = s.accept()
    # print(f"connected eith {address}")
    # print(clientsocket.recv(1024).decode('utf-8'))
