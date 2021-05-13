from colorama import Back,Fore,Style
import requests
import colorama
import time
import os
os.system("title IP Information by T1m")
colorama.init(autoreset=True)
print(Fore.BLUE + """

============================================
= ██╗██████╗░  ██╗███╗░░██╗███████╗░█████╗░=
= ██║██╔══██╗  ██║████╗░██║██╔════╝██╔══██╗=
= ██║██████╔╝  ██║██╔██╗██║█████╗░░██║░░██║=
= ██║██╔═══╝░  ██║██║╚████║██╔══╝░░██║░░██║=
= ██║██║░░░░░  ██║██║░╚███║██║░░░░░╚█████╔╝=
= ╚═╝╚═╝░░░░░  ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░=
============================================
""")
print(Fore.RED + "by T1m")
colorama.init(autoreset=True)
query=input("IP : ")
os.system("cls")
print("""

============================================
= ██╗██████╗░  ██╗███╗░░██╗███████╗░█████╗░=
= ██║██╔══██╗  ██║████╗░██║██╔════╝██╔══██╗=
= ██║██████╔╝  ██║██╔██╗██║█████╗░░██║░░██║=
= ██║██╔═══╝░  ██║██║╚████║██╔══╝░░██║░░██║=
= ██║██║░░░░░  ██║██║░╚███║██║░░░░░╚█████╔╝=
= ╚═╝╚═╝░░░░░  ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░=
============================================
""")
print(Fore.GREEN + "by T1m")

url = f"http://ip-api.com/json/{query}"

data=requests.get(url).json()
status = data["status"]
colorama.init(autoreset=True)
print(Fore.BLUE + "Status : " +status)
stadt = data["city"]
colorama.init(autoreset=True)
print(Fore.RED + "Stadt : " + stadt)
region = data["regionName"]
print(Fore.GREEN + "Region : " + region)
country = data["country"]
print(Fore.BLUE + "Land : " + country)
orga=data["org"]
print(Fore.RED + "Netzbetreiber : "+ orga)
post=data["zip"]
print(Fore.GREEN + "Postleitzahl : "+post)
zeitzone=data["timezone"]
print(Fore.BLUE + "Zeitzone : " + zeitzone)
ccode=data["countryCode"]
print(Fore.RED + "Country Code : " + ccode)
while True:    
    time.sleep(1)

