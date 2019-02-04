# -*- coding: utf-8 -*-
# Author:D4Vinci
# Don't touch my code, it's art :D
from __future__ import print_function
import sys, argparse
try: # Instead of using sys to detect python version
	input = raw_input
except:
	pass

def my_map(fuck,asses):
	#Because map behaves differently in python 2 and 3, I decided to write my own fuckin version :3
	lols = []
	for ass in asses:
		lols.append( fuck(ass) ) # LOL
	return lols

# As python 3 has no long function anymore, I will do mine
def ip2long(ip, p=3, long_ip=0): # With simple math I could replace the old shitty function with this loop
	for part in my_map( int,ip.split(".") ):
		long_ip += pow(256,p)*part
		p -=1
	return [ str(long_ip) ]

def ip2octal(ip):
	  return [ '.'.join([ format(int(x), '04o') for x in ip.split('.') ]) ]

def ip2hex(ip, length=4):
	# With length I will decided which parts to convert
	ip_parts = my_map(int,ip.split("."))
	return ".".join( my_map( hex,ip_parts[:length] ) + my_map(str,ip_parts[length:]) )

def hex_alike(ip):
	result,n = [],6
	for x in range(1,5):
		result.append( ip2hex(ip,x) )

	result.append( "0x"+"0"*8+ip2hex(ip).split(".")[0][2:] )
	for p in ip2hex(ip).split(".")[1:]:
		result[4] = ".".join([ result[4], "0x"+"0"*n+p[2:] ])
		n -= 2
	return result + [ip2hex( ip2long(ip)[0] ).replace("L","")]

def ip_urlencoded(ip):
	return [ ( "%2E".join([ "%3"+i for i in ip.split(".") ]) ).replace(":","%3A") ]

def ip_as_url(ip):
	urls = ["http://howsecureismypassword.net@","http://google.com@accounts@","https://www.facebook.com+settings&tab=privacy@"]
	return [ u+ip for u in urls]

def main():
	parser = argparse.ArgumentParser(prog='Cuteit.py')
	parser.add_argument("ip", help="IP you want to convert")
	parser.add_argument("--disable-coloring", action="store_true", help="Disable colored printing")
	args = parser.parse_args()
	G,B,R,W,M,C,end = '\033[92m','\033[94m','\033[91m','\x1b[37m','\x1b[35m','\x1b[36m','\033[0m'
	Bold,underline  = "\033[1m","\033[4m"
	heart = '❤️ '
	if args.disable_coloring:
		G = B = R = W = M = C = Bold = underline = ''
		heart = "<3" # Fuck you windows!
	print(end+G+Bold+"Cuteit IP obfuscator made with "+heart+" By Karim 'D4Vinci' Shoair", file=sys.stderr)
	ip = args.ip
	if ip.count(".")!=3:
		print(end+R+Bold+"Sorry, we convert ips only not urls!"+end, file=sys.stderr)
		exit(0)

	# My own shit regex :D
	for shit in ["http://", "https://", "\\", "/"]:
		while shit in ip:
			ip = ip.replace(shit,"")
	ip = ip.split(":")[0]

	formats = {"IP to Long":ip2long, "IP to HEX":hex_alike, "IP to Octal":ip2octal, "IP to urlencoded IP":ip_urlencoded}

	for form in formats:
		print(end+M+Bold+"- Converting "+form+end, file=sys.stderr)
		for n,thing in enumerate( formats[form](ip) ):
			print(end+G+"\t* Using "+end+R+"http://"+thing+end+G+" form", file=sys.stderr)
			for i,shape in enumerate(ip_as_url(thing)):
				print(end+W+"\t\t["+str(i)+"] "+end+G+shape, file=sys.stderr)
				sys.stdout.flush() # So it prints line by line not hanging
			print("", file=sys.stderr)
			sys.stdout.flush()

class lib:
	def __init__(self, ip):
		self.ip = ip
		self.hex        = ip2hex(self.ip)
		self.long       = ip2long(self.ip)[0]
		self.oct        = ip2octal(self.ip)[0]
		self.urlencoded = ip_urlencoded(self.ip)[0]
		self.hex_parts  = hex_alike(self.ip)[:-1]
		self.in_urls = lambda ip : ip_as_url(ip)

if __name__ == '__main__':
	main()
