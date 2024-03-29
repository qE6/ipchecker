# Coded by qE6.
# Simple script for getting information about IP address
# Script use ip-api.com

import requests
import json
import sys
from colorama import Fore, Style
# from colorama import init, deinit  # uncommet this line on Windows

# Some really easy IP validator
def isGoodIP(ip=str):
    try:
        ipnums = ip.split(".")
        if len(ipnums) != 4:
            return False
        for i in ipnums:
            if int(i) > 255:
                return False
        return True
    except:
        return False

# Function for sending request to ip-api
def getIPInfo(ipstr=str):
    try:
        req = requests.get("http://ip-api.com/json/" + ipstr)
        if req.status_code != 200:
            print(Fore.RED + Style.BRIGHT + "[-] Answer error!" + Style.RESET_ALL)
            # deinit() # uncomment this line on Windows
            exit(0)
    except:
        print(Fore.RED + Style.BRIGHT + "[-] Something went wrong!" + Style.RESET_ALL)
        # deinit() # uncomment this line on Windows
        exit(0)

    return req.text

def main():
    # init()  # uncomment this line on Windows
    if len(sys.argv) == 1:
        print(Fore.RED + Style.BRIGHT + "Usage: " + Style.RESET_ALL + sys.argv[0] + " <ip>")
        # deinit() # uncomment this line on Windows
        exit(0)
    ipstr = sys.argv[1]

    if isGoodIP(ipstr) != True:
        print(Fore.RED + Style.BRIGHT + "[-] IP format error" + Style.RESET_ALL)
        exit(0)
        # deinit() # uncomment this line on Windows

    print("[*] Trying to get infromation about " + Style.BRIGHT + Fore.BLUE + ipstr + Style.RESET_ALL)
    result = json.loads(getIPInfo(str(ipstr)))

    if result["status"] == "success":
        print(Style.BRIGHT + Fore.GREEN + "[+] We found something!\n" + Style.RESET_ALL)
        print("IP: " + Fore.BLUE + Style.BRIGHT + result["query"] + Style.RESET_ALL)
        print("\nGEO INFO\nCountry: " + Fore.BLUE + Style.BRIGHT + result["country"] + Style.RESET_ALL)
        print("City: " + Fore.BLUE + Style.BRIGHT + result["city"] + Style.RESET_ALL)
        print("Coords: " + Fore.BLUE + Style.BRIGHT + str(result["lat"]) + Style.RESET_ALL + ", " + Style.BRIGHT + Fore.BLUE + str(result["lon"]))
        print(Style.RESET_ALL + "\nCOMPANY INFO\nISP: " + Fore.BLUE + Style.BRIGHT + result["isp"])
        print(Style.RESET_ALL + "ORG: " + Style.BRIGHT + Fore.BLUE + result["org"])
        print(result["as"] + Style.RESET_ALL)

        print("\nInformation may contain inaccuracies.")
    else:
        print(Style.BRIGHT + Fore.RED + "[-] Failed." + Style.RESET_ALL)
  # deinit() # uncomment this line on Windows

if __name__ == "__main__":
    main()
