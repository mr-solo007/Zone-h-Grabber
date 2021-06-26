import requests
import os
import re
import datetime
#Libr (*_*)
from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)
hmar  = Fore.RED
zrak = Fore.BLUE
fc = Fore.CYAN
byad = Fore.WHITE
sfar = Fore.YELLOW
khdar = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
x = requests.session()
def Folder(directory):
  if not os.path.exists(directory):
  	os.makedirs(directory)
Folder("Result")
user = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
def grab() :
	id = raw_input("add Id Attacker : ")
	url = "https://zone-d.org/attacker/id/"+id+"/"
	if os.name == "nt" :
		os.system("cls")
	else :
		os.system("clear")
	try :
		for i in range(1,1000) :
			req = x.get(url+str(i), headers=user).text
			graber = re.findall('"><td>(.*?)<td><a',req)
			for n in graber :
				sp = n.split("/")[0]
				http = ("http://"+sp)
				print(hmar+"[ MrSolo71 ]  "+byad+http)
				with open("Result/lista.txt","a") as file :
					file.write(http+"\n")
					file.close()
	except :
		pass
def onhold() :
	try :
		link = "https://zone-d.org/mirror/onhold/"
		for mm in range(1, 1188) :
			check = x.get(link+str(mm), headers=user).text
			go = re.findall('"><td>(.*?)<td><a', check)
			for oo in go :
				hhh = oo.split("/")[0]
				htt = ("http://"+hhh)
				print(hmar+"[ MrSolo71 ]  "+byad+htt)
				with open("Result/onhod-solo.txt","a") as lol :
					lol.write(htt+"\n")
					lol.close()
	except :
		pass
def archive() :
	urs = 'https://zone-d.org/mirror/archive/'
	for xd in range(1, 5643) :
		requ = x.get(urs+str(xd), headers=user).text
		grab = re.findall('"><td>(.*?)<td><a',requ)
		for site in grab :
			if "/" in site :
				sp = site.split("/")[0]
				link = ('http://'+sp)
				print(fc+"[ SOLO ] "+byad+link)
				with open('Result/arichive-d.txt','a') as files :
					files.write(link+"\n")
					files.close()
			else :
				link = ("http://"+site)
				print(fc+"[ SOLO ] "+byad+link)
				with open("Result/archive-d.txt","a") as files :
					files.write(link+"\n")
					files.close()
def main() :
	logo = """ 
	
	1 - grab website from id attacker 
	2 - grab website from onhold 
	3 - grab website from archive """
	print(logo)
	print(""*200)
	choose = input("HI Mr Solo71 CHOOSE NUMBER : ")
	if choose == "1" :
		grab()
	elif choose == "2" :
		onhold()
	elif choose == "3" :
		archive()
	else :
		exit()
def coding() :
	date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
	#02/02/2021 19:19
	xd = input("PassworD of Script : ")
	if "2022" in date :
		exit()
	elif xd == "MrSolo2021" :
		main()
	else :
		exit()
coding()
