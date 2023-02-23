import socket

HEADER_SIZE = 10

# socket.AF_INET -> IPv4
# socket.SOCK_STREAM -> TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.3.1', 1235))

# full_msg = ''
# new_msg = True
while True:
    msg = "Welcome to the raspberry pi!"
    msg = f'{len(msg):<{HEADER_SIZE}}' + msg
    # clientsocket, address = s.accept()
    # print(f'Connection from {address} has been established!')
    s.send(bytes(msg, "utf-8"))
    # msg = s.recv(16)
    # if new_msg:
    #     print(f'the length of the message is:{msg[:HEADER_SIZE]}')
    #     msgLen = int(msg[:HEADER_SIZE])
    #     new_msg = False

    # full_msg += msg.decode('utf-8')

    # if len(full_msg) - HEADER_SIZE == msgLen:
    #     print('entire message recovered!')
    #     print(f'{full_msg[HEADER_SIZE:]}')
    #     new_msg = True
    #     full_msg = ''
