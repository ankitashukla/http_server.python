import socket                         #for sockets

					###using AF_INET, STREAM socket 
					###or could have used DGRAM instead of STREAM

newSocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM)       #creating a socket object
print "The socket has been successfully created"
newSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
newSocket.bind (('', 7070))           #opening port 7007 for connections (binding address to port)
newSocket.listen(2)                   #asking the socket to wait (listen) for clients (setting up n strting TCP listener)
#also gives d max no of queued connections
while True:                           #infinite loop
	channel, addr_info = newSocket.accept()      #accepting client connections
	#print "Connected by ", addr_info            #print client's address
	channel.send ( "Hello World!")              #sending a message back (transmitting TCP msg)
	channel.close                               #closing the socket

import urllib2
req = urllib2.Request('127.0.0.1:7007')
res = urllib2.urlopen(req)
print "Date:" + res.info().get('Date') ## printing the headers
print "Expires:" + res.info().get('Expires')
channel.send ("Expires:" + res.info().get('Expires'))
print "Content-Type:" + res.info().get('Content-Type')
print "Server:" + res.info().get('Server')
res.close();