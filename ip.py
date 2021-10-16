import webbrowser
import time
import socket
import os
import sys
import threading
import subprocess as sp
import time
import requests
import os,sys
os.system("title Death.ware")

print("       ----------------")
print("      | Death software |") 
print("       ----------------")
print ("""      
▒█░▒█  ░█▀▀█  ▒█▀▀█  ▒█░▄▀ █  ▒█▀▀▀█ 
▒█▀▀█  ▒█▄▄█  ▒█░░░  ▒█▀▄░  ░ ░▀▀▀▄▄ 
▒█░▒█  ▒█░▒█  ▒█▄▄█  ▒█░▒█ ░  ▒█▄▄▄█""")

simple = time.sleep(1)
id = print("            id - 1000")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 80))
host_name = socket.gethostname()
print("     Host name - "  + host_name)
s.close()
id 
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./50)
print("\n")
slowprint(" - The only python multihack - ")
slowprint("        - Death.ware - ")
time.sleep(1)
print("\n")
print("###############################################################")
print("Options:")
print("0.)Exit")
print(" ")
print("1.)Whats my ip")
print(" ")
print("2.)Ping an ip")
print(" ")
print("3.)Ip grabber link")
print(" ")
print("4.)IP to region")
print(" ")
print("5.)Help (If you don't know how to use the hack)")
print("###############################################################")

simple_1 = input("Please enter your option: ")
if simple_1 == "1":
    print("\n" * 100)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    print("ip - " + s.getsockname()[0])
    s.close()
    time.sleep(3)

if simple_1 == "2":
    print("\n" * 100)
    print("    ____      ____  _                       ")
    print("   /  _/___  / __ \(_)___  ____ ____  _____ ")
    print("   / // __ \/ /_/ / / __ \/ __ `/ _ \/ ___/")
    print(" _/ // /_/ / ____/ / / / / /_/ /  __/ /  ")
    print("/___/ .___/_/   /_/_/ /_/\__, /\___/_/    ")
    print("   /_/                  /____/          ")
    print("               By - sleepy")
    print("")
    print("")
    ipaddress = input("Type IP address to ping: ")
    times = input("How many times to ping? [Press 0 for infinite ping]")
    while True:
        os.system('ping -n ' + times + ' {}'.format(ipaddress))
        time.sleep(10)
        exit()

        if times == "0":
            os.system('ping -n 429290 {}'.format(ipaddress))

elif simple_1 == "5":
     print("\n" * 100)
     print(" - press a number and get your hack or join my discord for help - ")
     print("             - https://discord.gg/Z9MxmBmKDP - ")
     time.sleep(5)
    
if simple_1 == "3":
    print("\n" * 100)
    webbrowser.open("https://grabify.link/track/RAGPXK")
    print("\n" * 100)

if simple_1 == "4":
    print("\n" * 100)

    print(("""                         Welcome To The Ip Finder
                                  sleepy
                                   V1.0    """))
 
    print(("            =================GEO IP LOCATIONS=================  "))

    print("\n")

    inp=input(("            Target IP: "))
    def Geo_IP():
	    if inp.startswith('http://'):
		    print(colored("                 Sorry, You cannot use 'http://' "))
		    time.sleep(1)
		    print(colored("         Shutting down..."))
		    time.sleep(4)
		    sys.exit()
	    if inp.startswith("https://"):
		    sys.exit("Sorry, You cannot use 'https://' ")
	    try:
		    get=requests.get(f"https://api.hackertarget.com/geoip/?q={inp}")
		    print(get.text)
	    except Exception:
		    print(colored(f" °.° The address you entered '{inp}' is not Connectable ! \n Or check your Internet Connections, \nThank you."))

	    save=input(("Save info ? Y/n: "))
	    if save=="y":
		    file=open(f"./geo-{inp}.txt", "w")
		    print(file.write(str(get.text)))
		    print(colored(f"Informations saved from '{inp}' Check geo-{inp}.txt !", ))
	    if save=="Y":
		    file=open(f"./geo-{inp}.txt", "w")
		    print(file.write(str(get.text)))
		    print((f"Informations saved from '{inp}' Check geo-{inp}.txt !", ))
	    elif save=="n":
		    sys.exit("Done!")
	    elif save=="N":
		    sys.exit("Done!")
    Geo_IP()
    
else:
    print("Invalid option. Start the cheat again and select a valid option from the list.")
    
if simple_1 =="69":
    print("\n" * 100)
    time.sleep(1)
    print("nice")
    print("YOU FOUND THE EASTER EGG!") #dont dm me if you looked at the code, IM LOOKING AT YOU
    print("Go into my discord server and dm me to get a prize")

if simple_1 =="0":
    print("\n" * 100)
    os.close
