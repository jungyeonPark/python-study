import socket

HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))
while True:
    send_data = input("입력하세요: ")
    if not send_data:
        print("다시 입력하세요.")
        continue
    client_socket.sendall(send_data.encode())
    data = client_socket.recv(1024)
    print('Received', repr(data.decode()))


client_socket.close()