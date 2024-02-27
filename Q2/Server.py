import socket 
import pickle
import os

def run_server(): 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8000 )
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Server is listening for incoming connections...")

    while True: 
        client_socket, client_address = server_socket.accept()
    
        try: 
            print("Connected to: ", client_address)
            task_data = client_socket.recv(1024)
            task, args = pickle.loads(task_data)
            
            result = task(*args)
            
            result_data = pickle.dumps(result)
            client_socket.sendall(result_data)

        finally: 
            client_socket.close()
            break

if __name__ == "__main__":
    run_server()