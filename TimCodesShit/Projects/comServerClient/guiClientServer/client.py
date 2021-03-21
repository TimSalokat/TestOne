import sys, os, threading
from socket import *

stop = False

def send(clientSocket):
    global stop
    while True:
        if stop == True:
            break
        send_msg = input("Message: ")
        clientSocket.sendall(send_msg.encode())
    
def recv(clientSocket):
    global stop
    while True:
        data = clientSocket.recv(1024).decode()
        if data == "q":
            print("Closing connection")
            stop = True
            break
        else:
            print("\nServer: " + data)



#the main function code
def client():

    threads = []
    # TODO (1) - define HOST name, this would be an IP address or 'localhost' (1 line)
    HOST = 'localhost'  # The server's hostname or IP address
    # TODO (2) - define PORT number (1 line) (Google, what should be a valid port number)
    PORT = 6789        # The port used by the server

    # Create a TCP client socket
    #(AF_INET is used for IPv4 protocols)
    #(SOCK_STREAM is used for TCP)
    # TODO (3) - CREATE a socket for IPv4 TCP connection (1 line)
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # request to connect sent to server defined by HOST and PORT
    # TODO (4) - request a connection to the server (1 line)
    clientSocket.connect((HOST, PORT))
    print('Client is connected to a chat sever!\n')


    # call the function to send message to server
    #send_to_server(clientSocket)
    t_send = threading.Thread(target=send, args=(clientSocket,))
    # call the function to receive message server
    #recv_from_server(clientSocket)
    t_rcv = threading.Thread(target=recv, args=(clientSocket,))
    threads.append(t_send)
    threads.append(t_rcv)
    t_send.start()
    t_rcv.start()

    t_send.join()
    t_rcv.join()

    print('EXITING')
    sys.exit()

client()