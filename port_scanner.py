#!/usr/bin/env python3

#Copyright:
#The content of the port_scanner.py program is protected by copyright.
#Any use of it, as well as the use of any part of it for commercial purposes
#or for their direct or indirect support without the prior consent of Marek Kowolowski will be considered a violation of copyright in the sense of generally binding legal norms.
#PROGRAM IS FOR EDUCATIONAL PURPOSES ONLY!
 
#Port scanning program
#Author: Marek Kowolowski

###################################################################
import sys
import socket
from datetime import datetime
###################################################################

###################################################################

while True:

	intar = input("Target IP address: ")

	inpminimum = input("Minimal number of port: ")
	if inpminimum:
		try:
			minimum = int(inpminimum)
		except ValueError as err:
			print(err)
			print("No number was entered.")
			print("Exiting program...")
			break

	inpmaximum = int(input("Maximal number of port: "))
	if inpmaximum:
		try:
			maximum = int(inpmaximum)
		except ValueError as err:
			print(err)
			print("No number was entered.")
			print("Exiting program...")
			break
			

	if len(intar) == 11:
		target = socket.gethostbyname(intar)
	else:
		print("Invalid number of arguments.")
		print("Syntax: python3 scanner.py <ip>")

	###################################################################
	print("-" * 45)
	print("Scanning target IP address: " + target)
	print("Scan started: " + str(datetime.now()))
	print("-" * 45)
	###################################################################

	try:
		for port in range(minimum, maximum):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port))
			if result == 0:
				print("Port {} is open".format(port))
				print("The scan is finished.")
			s.close()
		yes_or_no = input("Do you want to repeat the program (yes/no)?: ")
		if yes_or_no == "yes":
			continue
		else:
			print("Exiting program...")
			break
	except KeyboardInterrupt:
		print("\n Exiting program...")
		sys.exit()

	except socket.gaierror:
		print("The host name cannot be resolved!")
	except socket.error:
		print("Unable to connect to server! Try it later.")
		sys.exit()

	###################################################################
