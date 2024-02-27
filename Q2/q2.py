import Client
import Server
import threading
from tasks import add, subtract
if __name__ =="__main__":
    host ="localhost"
    port = 8000
    
    server_thread =threading.Thread(target=Server.run_server)

    server_thread.start()
    
    print("results for add function: " + str(Client.run_client(add, 8, 20)))
    print("results for subract function: " + str(Client.run_client(subtract, 45, 30)))
    
    server_thread.join()