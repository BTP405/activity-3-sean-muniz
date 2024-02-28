import socket 
import threading
import pickle

IP = "localhost"
PORT = 8000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "q"

def handle_client(conn, addr): 
    print(f"[SERVER NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        pickle_data = conn.recv(SIZE)
        msg = pickle.loads(pickle_data)
        if msg == DISCONNECT_MSG:
            connected = False; 
        
        print(f"[{addr}] {msg}")
        # response = f"MSG recieved: {msg}"            
        # conn.sendall(response.encode(FORMAT))
    conn.close()

def run_server():
    print("[Starting] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}: {PORT}")
    
    while True: 
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

run_server()
        
    

        
        
            