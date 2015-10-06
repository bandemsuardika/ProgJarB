# chat_client.py

import sys
import socket
import select
 
def chat_client():
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    print 'you are connected. please login first.'
    print 'to login, please type login with lowercase.'
    cin=raw_input()
    if cin == "login" :
	sys.stdout.write('type your username '); sys.stdout.flush()
	cin=raw_input()
	if cin == '' :
	   sys.exit()
    	try :
           s.connect((host, port))
    	except :
           print 'Unable to connect'
           sys.exit()
	print 'type sendto [username] [messages] to send messages to spesific user'
	print 'type sendall [messages] to send messages to all logged user'
	print 'list to see a list of logged user'
	print 'You can start sending messages'
    	sys.stdout.write(cin+" says "); sys.stdout.flush()
	s.send(cin+" says "+cin)
	while 1:
           socket_list = [sys.stdin, s]
           # Get the list sockets which are readable
           ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
           for sock in ready_to_read:
		if sock == s:
                   # incoming message from remote server, s
                   data = sock.recv(4096)
                   if not data :
                      print '\nDisconnected from chat server'
                      sys.exit()
                   else :
		      #print data
                      sys.stdout.write(data)
                      sys.stdout.write(cin+" says "); sys.stdout.flush()
            
            	else :
                   # user entered a message
                   msg = sys.stdin.readline()
		   msg = cin+ " says "+msg
                   s.send(msg)
                   sys.stdout.write(cin+" says "); sys.stdout.flush()

if __name__ == "__main__":

    sys.exit(chat_client())

#sumber : http://www.bogotobogo.com/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php
#https://github.com/bandemsuardika/ProgJarB
