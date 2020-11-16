import requests, os, platform, time
from colorama import Fore, Back, Style

# List of databases / JSON APIs
databases = [
	"https://extreme-ip-lookup.com/json/"
]



print(Fore.RED + """

    ____                  ___   ____  _      __             
   / __ \____ _____ _____|__ \ / __ \(_)____/ /_  ___  _____
 """ + Fore.GREEN + """ / /_/ / __ `/ __ `/ ___/_/ // /_/ / / ___/ __ \/ _ \/ ___/
 """ + Fore.BLUE + """/ _, _/ /_/ / /_/ (__  ) __// _, _/ / /__/ / / /  __(__  ) 
""" + Fore.RED + """/_/ |_|\__,_/\__, /____/____/_/ |_/_/\___/_/ /_/\___/____/
""" + Fore.BLUE + """            /____/                razgonnaruleitall

Link: https://github.com/80b/Rags2Riches

""" + Fore.WHITE)

print("GeoIP Lookup")
print("")
print("")

ip = input("[" + Fore.GREEN + "INPUT" + Fore.WHITE + "] Input IP: ")


class Lookup:
	city = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["city"]
	
	
	isp = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["isp"]
	hostname = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["ipName"]
	query = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["query"]
	countryCode = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["countryCode"]
	country = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["country"]
	iptype = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["ipType"]
	region = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["region"]
	status = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["status"]
	asnorg = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["org"]
	lat = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["lat"]
	lon = requests.get("http://extreme-ip-lookup.com/json/" + ip).json()["lon"]

os.system("clear")
print(Fore.RED + """

    ____                  ___   ____  _      __             
   / __ \____ _____ _____|__ \ / __ \(_)____/ /_  ___  _____
 """ + Fore.GREEN + """ / /_/ / __ `/ __ `/ ___/_/ // /_/ / / ___/ __ \/ _ \/ ___/
 """ + Fore.BLUE + """/ _, _/ /_/ / /_/ (__  ) __// _, _/ / /__/ / / /  __(__  ) 
""" + Fore.RED + """/_/ |_|\__,_/\__, /____/____/_/ |_/_/\___/_/ /_/\___/____/
""" + Fore.BLUE + """            /____/                razgonnaruleitall

Link: https://github.com/80b/Rags2Riches

""" + Fore.WHITE)

print("GeoIP Lookup")
print("")
print("")
print("Start of IP Lookup")
print(Fore.GREEN + "Rags2Riches IP Tool")
print(Fore.BLUE + "By: Raz")
print("")
print(Fore.RED + "IP you searched: " + Lookup.query)
print("")
print(Fore.GREEN + "IP Type: " + Lookup.iptype)
print("")
print(Fore.YELLOW + "Status: " + Lookup.status)
print("")
print(Fore.RED + "CC: " + Lookup.countryCode)
print("")
print(Fore.GREEN + "Country: " + Lookup.region)
print("")
print(Fore.YELLOW + "ASN ORG: " + Lookup.asnorg)
print("")
print(Fore.RED + "IP Hostname: " + Lookup.hostname)
print("")
print(Fore.BLUE + "ISP: " + Lookup.isp)
print("")
print(Fore.YELLOW + "City: " + Lookup.city)
print("")
print(Fore.RED + "Latitude: " + Lookup.lat)
print("")
print(Fore.BLUE + "Longitude: " + Lookup.lon)
print("")
print(Fore.YELLOW + "End of IP Lookup!")
print("Make sure to star the collection on Github! Link: https://github.com/80b/Rags2Riches")
print("")
wre = input("Would you like to write this to a file named lookupresults.txt? Y/N: ")

if wre == "Y":
	f = open("lookupresults.txt", "w+")
	f.write("Start of IP Lookup\n")
	f.write("IP you searched: " + Lookup.query)
	f.write("\nIP Type: " + Lookup.iptype)
	f.write("\nStatus: " + Lookup.status)
	f.write("\nCC: " + Lookup.countryCode)
	f.write("\nCountry: " + Lookup.region)
	f.write("\nASN ORG: " + Lookup.asnorg)
	f.write("\nHostname: " + Lookup.hostname)
	f.write("\nISP: " + Lookup.isp)
	f.write("\nCity: " + Lookup.city)
	f.write("\nLatitude: " + Lookup.lat)
	f.write("\nLongitude: " + Lookup.lon)
	f.write("\nEnd of IP Lookup")
	f.write("\nMake sure to star the github! Link: https://github.com/80b/Rags2Riches")
	
