
# This file is part of Copernicus Framework
# See the file 'LICENSE' for copying permission.

import os
import sys
import atexit

def main():
    logo()
    print "################################################"
    print "#                                              #"
    print "# Welcome to the Copernicus Pentest Framework! #"
    print "#                   v.1.0                      #"
    print "#         Jason Jeske - Kaizen Security        #"
    print "#                                              #"
    print "################################################"
    print
    print
    while True:
        print "Select An Option from the Menu:"
        print
        print "\t 1.)  Attach Framework to a Deployed Agent/Create Agent"
        print "\t 2.)  Send Commands to an Agent"
        print "\t 3.)  View Information Gathered"
        print "\t 4.)  Attach Framework to a Mobile Modem"
        print "\t 5.)  Run a remote attack"
        print "\t 6.)  Run a social engineering or client side attack"
        print "\t 7.)  Clear/Create Database"
        print "\t 8.)  Use Metasploit"
        print "\t 9.)  Compile code to run on mobile devices"
        print "\t10.)  Install Stuff"
        print "\t11.)  Use Drozer" 
        print "\t 0.)  Exit"
        print
        print

        choice = raw_input('cfm> ').strip().lower()
        print

        if choice == '1':
            logo()
        if choice == '2':
            logo()
        if choice == '3':
            logo()
        if choice == '4':
            logo()
        if choice == '5':
            remote_attack()
        if choice == '6':
            social()
        if choice == '7':
            database_clear()
        if choice == '8':
            metasplat()
        if choice == '9':
            compile()
        if choice == '10':
            installstuff()
        if choice == "exit" or choice == '0':
            exit()

        print
        print '- '*3
        print
 
 
def logo():
    print("""
   _____                            _ _    
  / ____|                          (_) |   
 | |     ___  _ __   ___ _ __ _ __  _| | __
 | |    / _ \| '_ \ / _ \ '__| '_ \| | |/ /
 | |___| (_) | |_) |  __/ |  | | | | |   < 
  \_____\___/| .__/ \___|_|  |_| |_|_|_|\_\\v.1
             | |                           
             |_|   
                  
        """)

       
        
if __name__ == '__main__':
    main()
