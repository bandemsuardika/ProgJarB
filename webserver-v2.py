import sys
import socket
import time

REQ_SIZE = 10
RECV_BUFFER_SIZE = 1024

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#sys.stdout.write('Port : ')
#PORT = raw_input()
#PORT = int (PORT)

# Bind the socket to the port
server_address = ('localhost', 9000)
print >>sys.stderr, 'Serving HTTP starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(REQ_SIZE)

while True:
	# Wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	client_connection, client_address = sock.accept()
	print >>sys.stderr, 'Connection from', client_address
	print ''
    request = client_connection.recv(RECV_BUFFER_SIZE)
    #print request
    http_body = "<html><body><i>Hello <b>World!</b></body></html>"
    http_response = "HTTP/1.1 200 OK\n\n%s"%http_body
    print (request.decode())
    client_connection.send(http_response)
    if (message.startwith("GET /1 HTTP/1.1")):
        client_connection.send(get_file('1.jpg'))
    elif (message.startwith("GET /2 HTTP/1.1")):
        client_connection.send(get_file('2.jpg'))
    elif (message.startwith("GET /3 HTTP/1.1")):
        client_connection.send(get_file('3.jpg'))
    elif (message.startwith("GET /4 HTTP/1.1")):
        client_connection.send(get_file('4.jpg'))
    if (message.endswith("\r\n\r\n")):
        client_connection.send(get_file('gambar.jpg')) #membuka file
        break

    # Clean up the connection
    client_connection.close()
