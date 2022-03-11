import random
import requests
import json
from colorama import Fore, init
import os
os.system("Cc Tools | Made by zEncrypte")
init()

num = int()
amount = int()
threads = int()
class CcTools():
	global num
	global amount
	global threads

	def GenBins():
		print(Fore.CYAN + """
   
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
			print(bingen, file=open("GenBins.txt", "a+"))

		print("¿Do you want to continue using the tool? y/n")
		back = input("[>] ").lower()
		if back == "y":
			return CcTools.modules()
		else:
			print("Thank you for using CcTools...")


	def CcGen():
		print(Fore.WHITE + """

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
			generator = str(random.randint(3,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			cvv = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
			month = str(random.randint(1,12))
			year = str(20) + str(random.randint(21,30))
			date_exp = month + "|" + year
			save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"

			apart, apart1, apart2, apart3, apart4, apart5 = generator[0], generator[1], generator[3], generator[4], generator[5], generator[6]
			dividers_two = apart + apart1
			dividers_three = apart + apart1 + apart2 
			dividers_four = apart + apart1 + apart2 + apart3
			dividers_five = apart + apart1 + apart2 + apart3 + apart4
			dividers_six = apart + apart1 + apart2 + apart3 + apart4 + apart5
			whole_two = int(dividers_two)
			whole_three = int(dividers_three)
			whole_four = int(dividers_four)
			whole_five =  int(dividers_five)
			whole_six =+ int(dividers_six)

			if dividers_two == "34" or dividers_two == "37":
				generator += str(random.randint(0,9))
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)

			elif dividers_two == "62":
				a = random.randint(1, 4)
				if a == 1:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)
				elif a == 2:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)	
				elif a == 3:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)
				else:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)
			
			elif whole_three >= 300 and whole_three <= 305:
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)
			
			elif dividers_four == "5610" or whole_six >= 560221 and whole_six <= 560225: 
				
				print("") 
			
			elif dividers_four == "2014" or dividers_four == "2149":
				
				print("") 
			
			elif dividers_three == "309"  or dividers_two == "36" or whole_two >= 38 and whole_two <= 39:
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)
			
			elif dividers_two == "54" or dividers_two == "55":
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)
			#
			elif dividers_four == "6011" or whole_six >= 622126 and whole_six <= 622925 or whole_three >= 644 and whole_three <= 649 or dividers_two == "65":
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				increasing += 1
				print(save, file=open("CcGen.txt", "a+"))
				print(save)
			#
			elif dividers_three == "636":
				a = random.randint(1, 4)
				if a == 1:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)	
				elif a == 2:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)	
				elif a == 3:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)		
				else:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)		
			#
			elif whole_three >= 637 and whole_three <= 639:
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)
			#
			elif whole_four >= 3528 and whole_four <= 3589:
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)
			#
			elif dividers_four == "6304" or dividers_four == "6706" or dividers_four == "6771" or dividers_four == "6709":
				
				print("") 
			#
			elif whole_six >= 500000 and whole_six <= 509999 or whole_six >= 560000 and whole_six <= 699999:
				a = random.randint(1,8)
				if a == 1:
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)
				elif a == 2:
					generator += str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)
				elif a == 3:
					generator += str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)		
				elif a == 4:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
						
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)	
				elif a == 5:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)
				elif a == 6:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)
				elif a == 7:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)
				else:
					generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
					
					increasing += 1
					save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
					print(save, file=open("CcGen.txt", "a+"))
					print(save)
			
			elif dividers_four == "5019":
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)
			
			elif whole_six >= 222100 and whole_six <= 272099:
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)
			
			elif whole_two >= 51 and whole_two <= 55:
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)
			
			elif dividers_four == "6334" or dividers_four == "6767":
				
				print("") 
			
			elif dividers_four == "4903" or dividers_four == "4905" or dividers_four == "4911" or dividers_four == "4936" or dividers_six == "564182" or dividers_six == "633110" or dividers_four == "6333" or dividers_four == "6759":
				
				print("") 
			
			elif apart == "4" or dividers_four == "4026" or dividers_six == "417500" or dividers_four == "4405" or dividers_four == "4508" or dividers_four == "4508" or dividers_four == "4844" or dividers_four == "4913" or dividers_four == "4917":
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)
			
			else:
				generator += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
				
				increasing += 1
				save = "\n" + "CC: " + generator + "\n" + "CVV: " + cvv + "\n" + date_exp + "\n" + "+===================================+"
				print(save, file=open("CcGen.txt", "a+"))
				print(save)

		print("¿Do you want to continue using the tool? y/n")
		back = input("[>] ").lower()
		if back == "y":
			return CcTools.modules()
		else:
			print("Thank you for using CcTools...")
			
	def modules():
		os.system("cls")
		print(Fore.RED + """


╭━━━╮ ╭━━━╮       ╭━━━━╮ ╭━━━╮ ╭━━━╮ ╭╮    ╭━━━╮
┃╭━╮┃ ┃╭━╮┃       ┃╭╮╭╮┃ ┃╭━╮┃ ┃╭━╮┃ ┃┃    ┃╭━╮┃
┃┃ ╰╯ ┃┃ ╰╯  ╭━━╮ ╰╯┃┃╰╯ ┃┃ ┃┃ ┃┃ ┃┃ ┃┃    ┃╰━━╮
┃┃ ╭╮ ┃┃ ╭╮  ╰━━╯   ┃┃   ┃┃ ┃┃ ┃┃ ┃┃ ┃┃ ╭╮ ╰━━╮┃
┃╰━╯┃ ┃╰━╯┃         ┃┃   ┃╰━╯┃ ┃╰━╯┃ ┃╰━╯┃ ┃╰━╯┃  
╰━━━╯ ╰━━━╯         ╰╯   ╰━━━╯ ╰━━━╯ ╰━━━╯ ╰━━━╯             

1.Random bins generator
2.Random credit card generator
3.Exit

Soon more tools will be added

Made By zEncrypte
Github: https://github.com/zEncrypte
""")

		resp = int(input("[>] "))

		if resp == 1:
			CcTools.GenBins()
		elif resp == 2:
			CcTools.CcGen()
		elif resp == 3:
			print("Thank you for using CcTools...")
			return

CcTools.modules()
