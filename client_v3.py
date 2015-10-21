#chatroom client
import socket
import string
import sys
import select 
import pickle 
import time

def prompt() :
    sys.stdout.write('[Me] ')
    sys.stdout.flush()
 
#main function

def chat_client() :   
    if(len(sys.argv) < 3) :
        print 'Usage : python client.py hostname port'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    # create TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. Start sending messages'
    prompt()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    prompt()
             
            #user entered a message
            else :
                msg = []
                temp = sys.stdin.readline()
                data1 = msg.split()

                dleng = len(data1)
                if data1[0] == "login" :
                    if dleng>2 :
                        print('[System] Username invalid')
                    elif dleng<2 :
                        print('[System] Type your username')
                    else :
                        s.send(temp)

                elif data1[0] == "sendto" :
                    if dleng<3 :
                        print('[System] Invalid sendTo command')
                    else :
                        s.send(temp)

                elif data1[0] == "sendall" :
                    if dleng<2 :
                        print('[System] Invalid sendall command')
                    else :
                        s.send(temp)

                elif data1[0] == "list" :
                    if dleng>1 :
                        print('[System] Invalid list command')
                    else :
                        s.send(temp)

                else :
                    print('[System] Invalid command')
                    print '[System] type [sendto] [username] [messages] to send messages to spesific user'
                    print '[System] type [sendall] [messages] to send messages to all logged user'
                    print '[System] type [list] to see a list of logged user'

                prompt()

if __name__ == "__main__":
    chat_client()
