import socket
import pickle

def run_client(host, port): 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    client_socket.connect(server_address)
    
    try: 
        fileName = "file.txt"
        with open(fileName, 'rb') as f:
            fileData = f.read()
        
        data = {
            "fileName": fileName,
            "fileData": fileData
        }
        
        pickled_file_data = pickle.dumps(data)
        
        # message= "Hello, server! This is the client."
        client_socket.sendall(pickled_file_data)
        data = client_socket.recv(1024)
        print("(Client) recieved ack message ", data.decode())
    finally: 
        client_socket.close()

if __name__ == "__main__": 
    run_client()