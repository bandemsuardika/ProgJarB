#chatroom server
import sys
import socket
import select
import pickle
import string

# List to keep track of socket descriptors
HOST = 'localhost'
CONNECTION_LIST = []
USER_LIST = []
RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
PORT = 5000

def chat_server() :
    #creating TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # binding the socket
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
 
    print "Chat server started on port " + str(PORT)
 
    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[],0)
 
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                
                #broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
             
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    # receiving data from the socket.
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        data1 = msg.split()
                        
                        dleng = len(data1)
                        if data1[0] == "login" :
                            login(sock, str(data1[1]))

                        elif data1[0] == "sendto" :
                            #inisialisasi
                            logged = 0
                            user = ""
                            for x in range (len(USER_LIST)) :
                                #if socket already login
                                if USER_LIST[x] == sock :
                                    logged = 1
                                    user = USER_LIST[x+1]
                            #error message if user not login yet
                            if logged == 0 :
                                send(sock, "[System] You are not login")
                            else :
                                data2=""
                                for x in range (len(data1)) :
                                    if x>1 :
                                        if not data2 :
                                            data2+=str(data1[x])
                                        else :
                                            data2+=" "
                                            data2+=str(data1[x])
                                for x in range (len(USER_LIST)) :
                                    if USER_LIST[x] == data1[1] :
                                        send(USER_LIST[x-1], "["+user+"] "+data2+"\n")

                        elif data1[0] == "sendall" :
                            #inisialisasi
                            logged = 0
                            user = ""
                            for x in range (len(USER_LIST)) :
                                #check if socket already login
                                if USER_LIST[x] == sock :
                                    logged = 1
                                    user = USER_LIST[x+1]
                            #error message if user not login yet
                            if logged == 0 :
                                send(sock, "[System] You are not login")
                            else :
                                data2=""
                                for x in range (len(data1)) :
                                    if x>1 :
                                        if not data2 :
                                            data2+=str(data1[x])
                                        else :
                                            data2+=" "
                                            data2+=str(data1[x])
                                broadcast_data(server_socket, sock, "["+user+"] "+data2+"\n")

                        elif data1[0] == "list" :
                            #inisialisasi
                            logged = 0
                            for x in range (len(USER_LIST)) :
                                #check if socket already login
                                if USER_LIST[x] == sock :
                                    logged = 1
                            #error message if user not login yet
                            if logged == 0 :
                                send(sock, "[System] You are not login")
                            else :
                                data2=""
                                for x in range (len(USER_LIST)) :
                                    if x%2 == 1 : 
                                        data2+=" "
                                        data2+=str(USER_LIST[x])
                                send(sock, "[System] "+data2+" \n")
                        else :
                            print("[System] Invalid command")
                    else :
                        # remove the socket that's broken 
                        if sock in CONNECTION_LIST :
                            CONNECTION_LIST.remove(sock)
                        for x in range (len(USER_LIST)) :
                            if USER_LIST[x] == sock :
                                USER_LIST.pop(X+1)
                                USER_LIST.pop(x)
                        # at this stage, no data means probably the connection has been broken
                        print "Client (%s, %s) is offline" %addr
                except:
                    #broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print "Client (%s, %s) is offline" % addr
                    #sock.close()
                    #CONNECTION_LIST.remove(sock)
                    continue
     
    server_socket.close()

#Function to broadcast chat messages to all connected clients
def broadcast_data (server_socket, sock, message) :
    for x in range(len(USER_LIST)) :
        #send message only to peer
        if USER_LIST[x] != server_socket and USER_LIST[x] != sock and x%2==0 :
            try :
                USER_LIST[x].send(message)
            except :
                # broken socket connection
                USER_LIST[x].close()
                
                USER_LIST.pop(x+1)
                USER_LIST.pop(x)
                # broken socket, remove it
                if USER_LIST[x] in CONNECTION_LIST :
                    CONNECTION_LIST.remove(USER_LIST[x])

def send (sock, message) : 
    try:
        sock.send(message)
    except:
        sock.close()
        
        for x in range (len(USER_LIST)):
            if sock == USER_LIST[x]:
                USER_LIST.pop(x+1)
                USER_LIST.pop(x)
        
        if sock in CONNECTION_LIST:
            CONNECTION_LIST.remove(sock)

def log_in (sock, user):
    flag1 = 0
    flag2 = 0
    for name in USER_LIST:
        if name == user:
            flag1 = 1
        if name == sock:
            flag2 = 1
    
    if flag1==1:
        send_msg(sock, "[System] You already has a username\n")
    elif flag2==1:
        send_msg(sock, "[System] Username already exist\n")
    else:
        USER_LIST.append(sock)
        USER_LIST.append(user)
        send_msg(sock, "[System] Login success\n")
 
if __name__ == "__main__":
    chat_server()
