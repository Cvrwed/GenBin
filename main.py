import os
import sys
import random
import ctypes
from time import sleep
from pystyle import Colors, Colorate, Cursor

rtp = Colors.red_to_purple
rty = Colors.red_to_yellow
gty = Colors.green_to_yellow
lb = Colors.light_blue
lr = Colors.light_red
pp = Colors.purple
wh = Colors.white
v = Colorate.Vertical
d = Colorate.Diagonal
h = Colorate.Horizontal
Cursor.HideCursor()
os.system("cls")

sx = "CCTools"
ctypes.windll.kernel32.SetConsoleTitleW(sx)

#slowmode ignore
def tortuga(_str):
    for letra in _str:
        sys.stdout.write(letra);sys.stdout.flush();sleep(0.03)
#slowmode ignore

class Tools():

	def Bins():
		print(v(rtp,"""
   
 ▄▄▄▄    ██▓ ███▄    █      ▄████ ▓█████  ███▄    █ 
▓█████▄ ▓██▒ ██ ▀█   █     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒██▒ ▄██▒██▒▓██  ▀█ ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██░█▀  ░██░▓██▒  ▐▌██▒   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
░▓█  ▀█▓░██░▒██░   ▓██░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
░▒▓███▀▒░▓  ░ ▒░   ▒ ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
▒░▒   ░  ▒ ░░ ░░   ░ ▒░     ░   ░  ░ ░  ░░ ░░   ░ ▒░
 ░    ░  ▒ ░   ░   ░ ░    ░ ░   ░    ░      ░   ░ ░ 
 ░       ░           ░          ░    ░  ░         ░ 
      ░                                             
                      """))
		increasing = 1
		amount = int(input(f" {pp}¿How many bin's would you like to generate?: {wh}"))
		while increasing <= amount:
			generator = str(random.randint(300000,600000))
			bingen = generator + "xxxxxxxxxx"
			print(h(rtp, bingen))
			increasing += 1
			print(bingen, file=open("bins.txt", "a+"))

		print(f" {pp}¿Do you want to continue using the tool? y/n")
		back = input(f"{pp}[{lb}>{pp}] {wh}").lower()
		if back == "y":
			return Tools.modules()
		else:
			tortuga(f"{lb} Thanks you for using CCTools..{wh}")


	def CC():
		print(v(rtp, """
 ▄████▄   ▄████▄       ▄████ ▓█████  ███▄    █ 
▒██▀ ▀█  ▒██▀ ▀█      ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒▓█    ▄ ▒▓█    ▄    ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒ ▓███▀ ░▒ ▓███▀ ░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ░▒ ▒  ░░ ░▒ ▒  ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
  ░  ▒     ░  ▒        ░   ░  ░ ░  ░░ ░░   ░ ▒░
░        ░           ░ ░   ░    ░      ░   ░ ░ 
░ ░      ░ ░               ░    ░  ░         ░ 
░        ░                
			"""))
		increasing = 1
		amount = int(input(f"{pp}¿How many cards would you like to generate?: {wh}"))
		while increasing <= amount:
			generator = str(random.randint(4000000000000000,6000000000000000))
			cvv = str(random.randint(000, 999))
			month = str(random.randint(1, 12))
			year = str(random.randint(21,30))
			exp = month + "|" + year
			save = "CC: " + generator + "|" + exp + "|" + cvv + "\n" + "____________________________________"
			increasing += 1
			print(save, file=open("ccs.txt", "a+"))
			print(h(rtp, save))

		print(f" {pp}¿Do you want to continue using the tool? y/n")
		back = input(f"{pp}[{lb}>{pp}] {wh}").lower()
		if back == "y":
			return Tools.modules()
		else:
			tortuga(f"{lb} Thanks you for using CCTools..{wh}")
			
	def modules():
		print(v(rtp, fr"""
 ▄████▄   ▄████▄     ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▒██▀ ▀█  ▒██▀ ▀█     ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▒▓█    ▄ ▒▓█    ▄    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒ ▓███▀ ░▒ ▓███▀ ░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
░ ░▒ ▒  ░░ ░▒ ▒  ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
  ░  ▒     ░  ▒          ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
░        ░             ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
░ ░      ░ ░                      ░ ░      ░ ░      ░  ░      ░  
░        ░                                                       
            ╔═══════════════════════════════════════╗
            ║   Welcome {os.getlogin()}                       ║ 
            ║   Github https://github.com/zEncrypte ║
            ║═══════════════════════════════════════║
            ║   [1] Random bins generator           ║
            ║   [2] Random credit card generator    ║
            ║   [3] Exit                            ║
            ╚═══════════════════════════════════════╝

"""))
        
		resq = int(input(f" {pp}[{lb}>{pp}] {wh}"))
    
		if resq == 1:
			Tools.Bins()
		elif resq == 2:
			Tools.CC()
		elif resq == 3:
			tortuga(f"{lb} Thanks you for using CCTools..{wh}")
			return

Tools.modules()
