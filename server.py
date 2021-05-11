#!/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer
import cv2
from os import curdir, sep,remove
from io import StringIO
import cgi
from Crypto.Cipher import AES
from subprocess import call


#CONSTANTS
PORT_NUMBER = 8080

message = "Super secret message here wow!"
AES_KEY = "SimpleAsabc12311"
passphrase = "abc123"
messageFilename = "message.txt"
inFilename = "webcam.jpg"
outFilename = "cam_1.jpg"

class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):

		pathSplit = self.path.split("?")

		if len(pathSplit) > 1:
			tempParams = pathSplit[1].split("&")
			params = {}
			for p in tempParams:
				pSplit = p.split("=")
				params[pSplit[0]] = pSplit[1]
		print(("path["+self.path+"]"))
		if pathSplit[0]=="/":
			pathSplit[0] = "/index.html"
		self.path = "/static"+pathSplit[0]

		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False

			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True



			if "ptz" in self.path:
				print(("BUTTON",params))

			if self.path == "/static/cam_1.jpg":
				'''#Send Steged image

				#		Encrypt Message
				encryption_suite = AES.new(AES_KEY, AES.MODE_CBC, 'This is an IV456')
				cipher_text = encryption_suite.encrypt(message[:16])
				f = open(messageFilename, 'wb')
				f.write(cipher_text)
				f.close()


				#		Capture Webcam Image
				camera = cv2.VideoCapture(0)
				return_value,image = camera.read()
				cv2.imwrite('webcam.jpg',image)
				camera.release()

				#		Call Steg
		
				cmd = "outguess -k \'" + passphrase + "\' -d  " + messageFilename + " " + inFilename + " " + outFilename
				call(cmd,shell=True)
				self.path = "cam_1.jpg"

				#		Cleanup
				remove(messageFilename)'''


			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path, "rb") 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

	#Handler for the POST requests
	def do_POST(self):
		if self.path=="/send":
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})

			print(("Your name is: %s" % form["your_name"].value))
			self.send_response(200)
			self.end_headers()
			self.wfile.write("Thanks %s !" % form["your_name"].value)
			return			
			
			
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print(('Started httpserver on port ' , PORT_NUMBER))
	
	#Wait forever for incoming http requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()
	