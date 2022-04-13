import random
import requests
import json
from colorama import Fore, Style, init
import os
init()

num = int()
amount = int()
threads = int()
class Tools():
	global num
	global amount
	global threads

	def Bins():
		print(Fore.WHITE + """
   
╭━━╮  ╭━━╮ ╭━╮ ╭╮      ╭━━━╮ ╭━━━╮ ╭━╮ ╭╮ 
┃╭╮┃  ╰┫┣╯ ┃┃╰╮┃┃      ┃╭━╮┃ ┃╭━━╯ ┃┃╰╮┃┃ 
┃╰╯╰╮  ┃┃  ┃╭╮╰╯┃      ┃┃ ╰╯ ┃╰━━╮ ┃╭╮╰╯┃ 
┃╭━╮┃  ┃┃  ┃┃╰╮┃┃ ╭━━╮ ┃┃╭━╮ ┃╭━━╯ ┃┃╰╮┃┃ 
┃╰━╯┃ ╭┫┣╮ ┃┃ ┃┃┃ ╰━━╯ ┃╰┻━┃ ┃╰━━╮ ┃┃ ┃┃┃ 
╰━━━╯ ╰━━╯ ╰╯ ╰━╯      ╰━━━╯ ╰━━━╯ ╰╯ ╰━╯ 
                      """)
		increasing = 1
		amount = int(input("¿How many bin's would you like to generate?: "))
		while increasing <= amount:
			generator = str(random.randint(3,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9))
			bingen = generator + "xxxxxxxxxx"
			print(bingen)
			increasing += 1
			print(bingen, file=open("bins.txt", "a+"))

		print("¿Do you want to continue using the tool? y/n")
		back = input("[>] ").lower()
		if back == "y":
			return Tools.modules()
		else:
			print("Thanks you for using CCTools..")


	def CC():
		print(Fore.RED + Style.BRIGHT + """
╭━━━╮ ╭━━━╮      ╭━━━╮ ╭━━━╮ ╭━╮ ╭╮ 
┃╭━╮┃ ┃╭━╮┃      ┃╭━╮┃ ┃╭━━╯ ┃┃╰╮┃┃ 
┃┃ ╰╯ ┃┃ ╰╯      ┃┃ ╰╯ ┃╰━━╮ ┃╭╮╰╯┃ 
┃┃ ╭╮ ┃┃ ╭╮ ╭━━╮ ┃┃╭━╮ ┃╭━━╯ ┃┃╰╮┃┃ 
┃╰━╯┃ ┃╰━╯┃ ╰━━╯ ┃╰┻━┃ ┃╰━━╮ ┃┃ ┃┃┃ 
╰━━━╯ ╰━━━╯      ╰━━━╯ ╰━━━╯ ╰╯ ╰━╯ 
                                                           
			""")
		increasing = 1
		amount = int(input("¿How many cards would you like to generate?: "))
		while increasing <= amount:
			generator = str(random.randint(4,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			cvv = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			month = str(random.randint(1,12))
			year = str(20) + str(random.randint(21,30))
			exp = month + "/" + year
			save = "\n" + "CC: " + generator + "\n" + "Exp: " + exp + "\n" + "Cvv: " + cvv + "\n" + "____________________________________"
			increasing += 1
			print(save, file=open("ccs.txt", "a+"))
			print(save)

		print("¿Do you want to continue using the tool? y/n")
		back = input("[>] ").lower()
		if back == "y":
			return Tools.modules()
		else:
			print("Thanks you for using CCTools..")
			
	def modules():
		os.system("cls")
		print(Fore.CYAN + Style.BRIGHT + """
╭━━━╮ ╭━━━╮       ╭━━━━╮ ╭━━━╮ ╭━━━╮ ╭╮    ╭━━━╮
┃╭━╮┃ ┃╭━╮┃       ┃╭╮╭╮┃ ┃╭━╮┃ ┃╭━╮┃ ┃┃    ┃╭━╮┃
┃┃ ╰╯ ┃┃ ╰╯  ╭━━╮ ╰╯┃┃╰╯ ┃┃ ┃┃ ┃┃ ┃┃ ┃┃    ┃╰━━╮
┃┃ ╭╮ ┃┃ ╭╮  ╰━━╯   ┃┃   ┃┃ ┃┃ ┃┃ ┃┃ ┃┃ ╭╮ ╰━━╮┃
┃╰━╯┃ ┃╰━╯┃         ┃┃   ┃╰━╯┃ ┃╰━╯┃ ┃╰━╯┃ ┃╰━╯┃  
╰━━━╯ ╰━━━╯         ╰╯   ╰━━━╯ ╰━━━╯ ╰━━━╯ ╰━━━╯ 

[1] Random bins generator
[2] Random credit card generator
[3] Exit
[!] Soon more tools will be added
[Github] https://github.com/zEncrypte
""")

		resq = int(input(Fore.RED + "[>] "))

		if resq == 1:
			Tools.Bins()
		elif resq == 2:
			Tools.CC()
		elif resq == 3:
			print(Fore.BLUE + Style.BRIGHT + "Thanks you for using CCTools..")
			return

Tools.modules()
