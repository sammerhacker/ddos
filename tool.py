import os
import sys
import time
sayser=print
ees=input
clear=os.system("clear")
run=os.system

### color ###
"\033[01;34m"

#icon
icon="""
\033[01;31m------------------------------
\033[01;31m            \033[01;31m|\033[01;37mPYTHON
\033[01;31m        \033[01;32mBY \033[01;37m: \033[01;31mEE\033[01;33mS \033[01;37m, \033[01;33mSAYSER
\033[01;31m
\033[01;31m    -----------------------
\033[01;31m       [\033[01;37m1\033[01;31m] \033[01;32mDDOS python cfscrape
\033[01;31m       [\033[01;37m2\033[01;31m] \033[01;36mDDOS python socket
\033[01;31m       [\033[01;37m3\033[01;31m] \033[01;32mexit
\033[01;31m
\033[01;32m       exit \033[01;31m{\033[01;37m3\033[01;31m} \033[01;37m&& \033[01;31mCTRL\033[01;37m+C
\033[01;31m-----------------------------
"""
################### code  ######################
def eesx():
           clear
           sayser(icon)
           tool=ees("\033[01;31mEE\033[01;33mS\033[01;31m=\033[01;32m>\033[01;31m>\033[01;32m> \033[01;37m")
           if tool == "1":
              run ("python ddosx.py")
           if tool == "2":
              run ("python ddosn.py")
           else:
                sayser (" ")
                toox=ees("y=back n=exit => ")
                if toox == "y":
                   run ("clear")
                   eesx()
                else:
                     exit(0)
try:
    eesx()
except KeyboardInterrupt:
       print ("EXIT ....")
