import socket, threading

bind_ip = "127.0.0.1"
bind_port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)

print(f"[*] Listening on {bind_ip}:{bind_port}")

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()

    print(f"[*] Received: {request}")

    client_socket.send("ACK!".encode())
    client_socket.close()

while True:
    client, addr = server.accept()

    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()