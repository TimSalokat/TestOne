import socket, threading

bind_ip = "127.0.0.1"
bind_port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)

print(f"[*] Listening on {bind_ip}:{bind_port}")

def handle_client(client_socket, address):
    
    while True:
        request = client_socket.recv(1024).decode()
        response = f"Received: {request}"

        if request == "exit client":
            client_socket.close()
            print(f"[*] {address}] Client closed")
            break
        else:
            print(f"[*] {address}] {response}")
            client_socket.send(response.encode())

while True:
    client, addr = server.accept()
    full_addr = f"{addr[0]}:{addr[1]}"

    print(f"[*] {full_addr}] Accepted connection")

    client_handler = threading.Thread(target=handle_client,args=(client,full_addr,))
    client_handler.start()