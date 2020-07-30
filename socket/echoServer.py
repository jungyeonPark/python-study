import socket

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()

client_socket, addr = server_socket.accept()

print('Connected by', addr)

while True:
    data = client_socket.recv(1024)
    print('Received from', addr, data.decode())
    send_data = input("입력하세요: ")
    if not send_data:
        print("다시 입력하세요.")
        continue
    client_socket.sendall(send_data.encode())

client_socket.close()
server_socket.close()
