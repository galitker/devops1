import socket

def is_valid_ipv4_address(addr):
	try:
    		socket.inet_aton(addr)
    		print ("ipv4 address")
	except socket.error:
	#except Exception as e:
    		print ("not ipv4 address")
is_valid_ipv4_address("1.2.3.84")
