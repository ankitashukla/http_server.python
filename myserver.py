import socket                         #for sockets

					###using AF_INET, STREAM socket 
					###or could have used DGRAM instead of STREAM
from time import gmtime, strftime

newSocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM)       #creating a socket object
print "The socket has been successfully created"

newSocket.bind (('', 7011))           #opening port 7007 for connections (binding address to port)
newSocket.listen(2)                   #asking the socket to wait (listen) for clients (setting up n strting TCP listener)
#also gives d max no of queued connections
#while True:                           #infinite loop
channel, addr_info = newSocket.accept()      #accepting client connections
print "Connected by ", addr_info            #print client's address
	#channel.send("Content-Type: text/html\r\n\r\n")
responseheaders='HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n' + strftime("%Y-%m-%d %H:%M:%S", gmtime())
channel.send(responseheaders)
channel.send ('<html><body><p><b>Hello World!</b></p></body></html>')              #sending a message back (transmitting TCP msg)

channel.close                             

newSocket.close()