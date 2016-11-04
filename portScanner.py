#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from errno import ECONNREFUSED
from functools import partial
from multiprocessing import Pool
import socket
import os
import sys


host = sys.argv[1]
portin = sys.argv[2]
port = int(portin)
NUM_CORES = 2
BUFFER_SIZE = 1024
message = "test"

if(len(sys.argv) < 3) :
	print ('Usage : python client.py hostname')
	sys.exit()
if(len(sys.argv) > 3) :
	print ('Usage : python client.py hostname')
	sys.exit()

def ping(host, port):
	#kokeile socket
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		print(str(port) + " Open")
		return port
	except socket.error as err:
		if err.errno == ECONNREFUSED:
			return False
		raise
def scan_ports(host, port):
	p = Pool(NUM_CORES)
	ping_host = partial(ping, host)
	return filter(bool, p.map(ping_host, range(port, 65536)))

def main(host):
	if host is None:
		host = "127.0.0.1"

	print("\nScanning ports on " + host + " ...")
	ports = list(scan_ports(host, port))
	print("\nDone.")

	print(str(len(ports)) + " ports available.")
	print(ports)


if __name__ == "__main__":

	main(host)

