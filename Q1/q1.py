import threading
import Client
import Server
if __name__ =="__main__":
    host ="localhost"
    port = 8000
    
    server_thread =threading.Thread(target=Server.run_server, args=(host, port))

    server_thread.start()
    
    Client.run_client(host, port)
    
    server_thread.join()