import socket 
import pickle

IP = "localhost"
PORT = 8000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "q"

def run_client2():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}: {PORT}")
    
    connected = True 
    while connected:
        msg = input("client2 > ")
        client.send(pickle.dumps(msg))
        
        if msg == DISCONNECT_MSG:
            connected = False
        # else:
        #     msg = client.recv(SIZE).decode(FORMAT)
        #     print(f"[SERVER] {msg}")

run_client2()
            
