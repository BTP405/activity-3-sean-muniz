#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.
import socket 
import pickle
import os

def run_server(host, port): 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port )
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Server is listening for incoming connections...")

    while True: 
        client_socket, client_address = server_socket.accept()
        
        # we must save the file in a new directory. 
        receivedDir = 'receivedFiles'
        if not os.path.exists(receivedDir):
            os.makedirs(receivedDir)

        try: 
            print("Connected to: ", client_address)

            #the item to be received is interpreted as a byte string
            #if it is empty, then the loop will end
            item = b""
            data = client_socket.recv(1024)
            if not data:
                break
            
            # concatonate the data which is also sent as a byte string item
            item += data
            
            #unpickle the data         
            unpickled_data = pickle.loads(item)
            
            # the dictionary that was unpickled will then be accessed by assigning the
            #key value pairs to these variables. 
            fileName = unpickled_data['fileName']
            fileData = unpickled_data['fileData']
            
            # this will construct a file path by joining the directory we made above
            # with the fileName that we recieve from the unpickled data.
            fileName = os.path.join(receivedDir, fileName)
            
            # this will open the file. the contents from fileData will then be written
            # to this file
            with open (fileName, 'wb') as f:
                f.write(fileData)
                
            message = "\n(Server) Message recieved by the server!"
            print("(Server) unpickled data: " + str(unpickled_data))
            client_socket.sendall(message.encode())
        finally: 
            client_socket.close()
            break

if __name__ == "__main__":
    run_server()

#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.