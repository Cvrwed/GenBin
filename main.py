import os, random
from os import name as _name, system as _system, get_terminal_size as _terminal_size
from sys import stdout as _stdout
from ctypes import c_int, c_byte, Structure, byref, windll

Windows = _name == 'nt'
Unix = _name == 'posix'
nagatoro = __name__ == '__main__'

class _OcultInfo(Structure):
  _fields_ = [("size", c_int), ("visible", c_byte)]

def trap():
  return _system("cls" if Windows else "clear")

def colors(life: str) -> str:
  return f"\033[38;2;{life}m"

m = colors('161;42;252')
ml = colors('255;0;102')
w = colors('255;255;255')
r = colors('255;0;0')
j = colors('255;147;92')

def Ocultism():
  if Windows:
    _Ocultism(False)
  elif Unix:
    _stdout.write("\033[?25l")
    _stdout.flush()

def _Ocultism(visible: bool):
  ci = _OcultInfo()
  handle = windll.kernel32.GetStdHandle(-11)
  windll.kernel32.GetConsoleCursorInfo(handle, byref(ci))
  ci.visible = visible
  windll.kernel32.SetConsoleCursorInfo(handle, byref(ci))

Ocultism()

def Owo(uwu: str):
  if Windows:
    return _system(f"title {uwu}")

Owo("CCTools")

def cc(zerotwo: str, drop: int = None, icon: str = " "):
  if drop is None:
    drop = _xd(zerotwo=zerotwo)
    return "\n".join((icon * drop) + zerotwo for zerotwo in zerotwo.splitlines())

def _xd(zerotwo: str):
    try:
      nya = _terminal_size().columns
    except OSError:
        return 0
    tortuge = zerotwo.splitlines()
    chocolat = max((len(v) for v in tortuge if v.strip()), default = 0)
    return int((nya - chocolat) / 2)

def Bins():
    trap()
    bnn = fr"""
    
    {r}▄▄▄▄    ██▓ ███▄    █      ▄████ ▓█████  ███▄    █ 
    ▓█████▄ ▓██▒ ██ ▀█   █     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
    ▒██▒ ▄██▒██▒▓██  ▀█ ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
    ▒██░█▀  ░██░▓██▒  ▐▌██▒   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
    ░▓█  ▀█▓░██░▒██░   ▓██░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
    ░▒▓███▀▒░▓  ░ ▒░   ▒ ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
    ▒░▒   ░  ▒ ░░ ░░   ░ ▒░     ░   ░  ░ ░  ░░ ░░   ░ ▒░
    ░    ░  ▒ ░   ░   ░ ░    ░ ░   ░    ░      ░   ░ ░ 
    ░       ░           ░          ░    ░  ░         ░ 
        ░                                             
    """[1:]
    bnn = cc(bnn)
    print(bnn)
    increasing = 1
    amount = int(input(f"{m}¿How many bin's would you like to generate?: {w}"))
    while increasing <= amount:
        generator = str(random.randint(400000,600000))
        bingen = generator + "xxxxxxxxxx"
        print(bingen)
        increasing += 1
        print(bingen, file=open("bins.txt", "a+"))
    input(f"{m}[{r}!{m}] {w}Press enter for continue...")
        


def CC():
    trap()
    ccsc = fr"""
    {r}▄████▄   ▄████▄       ▄████ ▓█████  ███▄    █ 
    ▒██▀ ▀█  ▒██▀ ▀█      ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
    ▒▓█    ▄ ▒▓█    ▄    ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
    ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
    ▒ ▓███▀ ░▒ ▓███▀ ░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
    ░ ░▒ ▒  ░░ ░▒ ▒  ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
    ░  ▒     ░  ▒        ░   ░  ░ ░  ░░ ░░   ░ ▒░
    ░        ░           ░ ░   ░    ░      ░   ░ ░ 
    ░ ░      ░ ░               ░    ░  ░         ░ 
    ░        ░                
    """[1:]
    ccsc = cc(ccsc)
    print(ccsc)

    increasing = 1
    amount = int(input(f"{m}¿How many cards would you like to generate?: {w}"))
    while increasing <= amount:
        generator = str(random.randint(4000000000000000,6000000000000000))
        cvv = str(random.randint(000, 999))
        month = str(random.randint(1, 12))
        year = str(random.randint(22,31))
        exp = month + "|" + year
        save = "CC: " + generator + "|" + exp + "|" + cvv
        increasing += 1
        print(save, file=open("ccs.txt", "a+"))
        print(save)
    input(f"{m}[{r}!{m}] {w}Press enter for continue...")
        
			
def main():
    while True:
        trap()
        sex = fr"""
        {m}▄████▄   ▄s████▄     ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
        ▒██▀ ▀█  ▒██▀ ▀█     ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
        ▒▓█    ▄ ▒▓█    ▄    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
        ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
        ▒ ▓███▀ ░▒ ▓███▀ ░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
        ░ ░▒ ▒  ░░ ░▒ ▒  ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
        ░  ▒     ░  ▒          ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
        ░        ░             ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
        ░ ░      ░ ░                      ░ ░      ░ ░      ░  ░      ░  
        ░        ░                                                       
                    {ml}╔═══════════════════════════════════════╗
                    {ml}║   {m}Welcome {os.getlogin()}  {ml}                     ║ 
                    {ml}║   {m}Github https://github.com/Swxy7w7 {ml}  ║
                    {ml}║═══════════════════════════════════════║
                    {ml}║   {m}[{r}1{m}] Random bins generator{ml}           ║
                    {ml}║   {m}[{r}2{m}] Random credit card generator{ml}    ║
                    {ml}║   {m}[{r}3{m}] Exit      {ml}                      ║
                    {ml}╚═══════════════════════════════════════╝
        """[1:]
        sex = cc(sex)
        print(sex)
        print()
        choice = input(f" {m}[{j}>{m}] {w}")
        if choice == "1":
            Bins()
        if choice == "2":
            CC()
        if choice == "3":
            exit()
        
if nagatoro:
    main()
