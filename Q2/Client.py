import socket
import pickle
# from tasks import add, subtract

def run_client(task, *args): 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8000)
    client_socket.connect(server_address)
    
    try: 
        task_data = pickle.dumps((task, args))
        client_socket.sendall(task_data)
        results = client_socket.recv(1024)
    finally:
        client_socket.close()
        return pickle.loads(results)

# if __name__ == "__main__": 
#     print("add result: " +str(run_client(add, 8, 20)))
#     print("subtract result: " + str(run_client(subtract, 45,15)))