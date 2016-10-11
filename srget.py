#!/usr/bin/env python

import socket as skt
import sys
from urlparse import urlparse
name = "http://10.27.8.20:8080/randSt.hamuel"
port = 8080

web = urlparse(name)
host = web.hostname
path = web.path
# print "netloc", web.hostname
# print "path", web.path
Socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
Socket.connect((host, port))
print "connecting"

def request(path,server):
	return "GET " + path + " HTTP/1.1\r\nHost: " + server + "\r\n\r\n"

with open('Baddas.txt', 'wb') as download:
	Socket.send(request(path,host))
	header = ""
	while True:
		data = Socket.recv(1024)
		header += data
		if "\r\n\r\n" in data:
			split_header = header.split("\r\n\r\n")
			# print split_header
			break
	
	header = split_header[0]
	begin_content = split_header[1]
	download.write(begin_content)
	content_length = header[header.find("Content-Length")+16:header.find("Connection")-1]
	print content_length
	download_leaw = 0
	while content_length >= download_leaw:
		data = Socket.recv(1024)
		download.write(data)
		download_leaw += len(data)
		if content_length == download_leaw:
			break

print "done"

Socket.close()

