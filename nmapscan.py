# Run a quick nmap scan from hackertarget

import requests
site=''
while not site:
  print("[+] Please Enter the Domain Ip/Address of the target:")
  site=input()
  break
x = requests.get("https://api.hackertarget.com/nmap/?q="+site)
print(x.text)

# Prints out the output in the terminal. 