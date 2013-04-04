import socket                       #for sockets
									###using AF_INET, STREAM socket 
									###or could have used DGRAM instead of STREAM
import time
import sys
import signal
class Aviator:
	def __init__(self):
		self.host=''
		self.port=8012
	def launch(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #creating a socket object
		print "Aviator is launched on port no:",self.port
		self.socket.bind((self.host, self.port))
		while True: 	 	
			try:
				print ("trying")
				self.connect()
			except KeyboardInterrupt:
				print ("Could not acquire the port")
				print ("Shutting down Aviator")
				sys.exit(1)
			#print("Conne")
	def responseHeaders(self):
		self.header=''
		self.header += "Version:HTTP/1.1\nContent-Type:text/html\nStatus:200 OK\nServer:Aviator (HTTP server implemented in Python)\n"
		time1=time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
		self.header += time1+"\n"
		return self.header
	def connect(self):
		self.socket.listen(2)
		#while True:
		channel, addr_info=self.socket.accept()      #accepting client connections
		print ("Connected by ", addr_info)            #print client's address
		headers=self.responseHeaders()
		channel.send(headers)
		channel.send('<html><body><b>Hello World!</b></body></html>')              #sending a message back (transmitting TCP msg)

print "Here comes Aviator!!"
s=Aviator()
s.launch()