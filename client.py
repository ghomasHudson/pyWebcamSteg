#!/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer
import cv2
from os import curdir, sep,remove
from io import StringIO
import cgi
from Crypto.Cipher import AES
from subprocess import call

import requests


'''decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
plain_text = decryption_suite.decrypt(cipher_text)'''


proxyPort = 4125
messageSize = 128
messageQueue = []


class proxyHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		#Load headers into message Queue
		#'Poke' server's buttons to alert it that steg data avalible at this IP


		#TODO: remove
		r = requests.get(self.path,stream=True,headers=self.headers)
		for chunk in r.iter_content(100):
			self.wfile.write(chunk)

		print("|",self.headers,"|")
		# breakpoint()
		messageQueue = [str(self.headers)[i:i+messageSize] for i in range(0, len(str(self.headers)), )]
		print(messageQueue)
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', proxyPort), proxyHandler)
	print(('Started webcam proxy on port' , proxyPort))

	#Wait forever for incoming http requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()
