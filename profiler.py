import subprocess, time, sys, os, re, urllib, requests, json
from termcolor import colored
from tqdm import tqdm
import colorama
from colorama import Fore, Back, Style
import time
from time import sleep
os.system('clear')
colorama.init(autoreset=True)
print(Style.BRIGHT + Fore.RED + """
 _____         ___ _ _        
|  _  |___ ___|  _|_| |___ ___ 
|   __|  _| . |  _| | | -_|  _|
|__|  |_| |___|_| |_|_|___|_|  
""")

print(Fore.BLUE + """
Osint investigation tool
lookup online public data of a person anonymously π₯Έπ»
""")
time.sleep(3)
first_name = str(input("[+] first name: "))
last_name = str(input("[+] last name: "))
os.system('echo "name: '+first_name+' '+last_name+'" >> names.txt')
print(Fore.BLUE + "gathering information on target")
os.system('w3m -dump https://www.spokeo.com/'+first_name+'-'+last_name+'?loaded=1 > output.txt')
print(Fore.BLUE + "finding social media profiles ππ¨βπ©βπ¦")
os.system('google "'+first_name+' '+last_name+'" > socials.txt')
print(Fore.BLUE + "searching locationsπ")
time.sleep(5)
print(Fore.BLUE + "looking for phone numbers, emails, and addressesππ±")
time.sleep(7)
print(Fore.BLUE + "searching for public recordsπ")
time.sleep(8)
print(Fore.BLUE + "getting your infomation ready!")
time.sleep(4)
for _ in tqdm(range(200),
    desc = "PROFILER ",
    ascii = False,ncols=100):
    time.sleep(0.2)

def menu():
    print(Fore.BLUE + """
=OSINT=MODULES==================================================================
  βββ[1] names
  βββ[2] location
  βββ[3] past locations
  βββ[4] family
  βββ[5] other names she or he goes by
  βββ[6] personal data included
=ADD=MODULES====================================================================
  βββ[7] add the persons state to get better and closer results
  βββ[8] add the persons region to get exact/closer results
  βββ[9] add the persons email to get to see if the password is available
  βββ[10] add phone number to get the address/names/location
  βββ[11] add the VIN number of the persons car
=DUMP=MODULES===================================================================
    βββ[12] dump location of the phone number
    βββ[13] dump all Related Phone Number addresses
    βββ[14] dump all Related Phone Number names from the addresses
    βββ[15] dump all Related Phone Numbers connected to the names and addresses
    βββ[16] dump all email results
    βββ[17] dump all VIN details about the persons car
=SOCIAL=PROFILES================================================================
        βββ[18] social media profiles
        βββ[99] exit
    """)
    selection=int(input(Style.BRIGHT + Fore.RED + "[+] "+first_name+" "+last_name+": "))
    if selection==1:
        names()
    elif selection==2:
          locations_location()
    elif selection==3:
          past_locations()
    elif selection==4:
          related_to()
    elif selection==5:
          go_by()
    elif selection==6:
          Includes()
    elif selection==7:
          add_location()
    elif selection==8:
          add_region()
    elif selection==9:
          addemail()
    elif selection==10:
          add_phonenumber()
    elif selection==11:
          add_VIN()
    elif selection==12:
          dump_place()
    elif selection==13:
          dump_address()
    elif selection==14:
          dump_names()
    elif selection==15:
          dump_relateph()
    elif selection==16:
          email_results()
    elif selection==17:
          dump_VINDT()
    elif selection==18:
          socials()
    elif selection==99:
          exit
    else:
        print(Fore.BLUE + "not a option")
        menu()

def names():
    print(Fore.GREEN + "[+] finding all possible names of "+first_name+" "+last_name+"")
    time.sleep(4)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match(first_name, line):
          print(Style.BRIGHT + Fore.BLUE + "[π₯Έπ] "+line)
          sleep(1)
    menu()

def locations_location():
    print(Fore.GREEN + "[+] finding all the possible locations of "+first_name+" "+last_name+"")
    time.sleep(4)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Resides in", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π] "+line)
          sleep(0.5)
    menu()

def past_locations():
    print(Fore.GREEN + "[+] finding all the possible last locations of "+first_name+" "+last_name+"")
    time.sleep(5)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Lived", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π geo] "+line)
          sleep(0.4)
    menu()

def related_to():
    print(Fore.GREEN + "[+] finding all possible family members of "+first_name+" "+last_name+"")
    time.sleep(6)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Related", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π¨βπ©βπ¦] "+line)
          sleep(1)
    menu()

def go_by():
    print(Fore.GREEN + "[+] finding all possible other names "+first_name+" "+last_name+" goes by")
    time.sleep(4)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Also known", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] "+line)
          sleep(0.2)
    menu()

def Includes():
    print(Fore.GREEN + "[+] finding all possible person info Included on "+first_name+" "+last_name+"")
    time.sleep(3)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Includes", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] "+line)
          sleep(0.3)
    menu()

def add_location():
    print(Fore.BLUE + "type the state she/he lives in")
    time.sleep(2)
    print(Style.BRIGHT + Fore.RED + """AL - alabama
AK - alaska
AZ - arizona
AR - arkansas
CA - california
CO - colorado
CT - connecticut
DE - delaware
DC - district of columbia
FL - florida
GA - Georgia
HI - hawaii
ID - idaho
IL - illinois
IN - indiana
IA - iowa
KS - kansas
KY - kentucky
LA - louisiana
ME - maine
MD - maryland
MA - massachusetts
MI - michigan
MN - minnesota
MS - mississippi
MO - missouri
MT - montana
NE - nebraska
NV - nevada
MH - new hampshire
NJ - new jersey
NM - new mexico
NY - new york
NC - north carolina
ND - north dakota
OH - ohio
OK - oklahoma
OR - oregon
PA - pennsylvania
PR - puerto rico
RI - rhode island
SC - south carolina
SD - south dakota
TN - tennessee
TX - texas
UT - utah
VT - vermont
VA - virginia
WA - washington
WV - west virginia
WI - wisconsin
WY - wyoming
    """)
    global location
    location = input(Fore.BLUE + "[+] add state: ")
    os.system('w3m -dump https://www.spokeo.com/'+first_name+'-'+last_name+'/'+location+' > output.txt')
    print(Fore.BLUE + "==================")
    print(Style.BRIGHT + Fore.CYAN + first_name)
    print(Style.BRIGHT + Fore.CYAN + last_name)
    print(Style.BRIGHT + Fore.CYAN + location)
    print(Fore.BLUE + "==================")
    anykey=input(Fore.BLUE + "press enter")
    print(Style.BRIGHT + Fore.GREEN + "saved!")
    time.sleep(3)
    menu()

def add_region():
    print(Fore.BLUE + "[+] type the region were "+first_name+" "+last_name+" lives in to get better results")
    time.sleep(2)
    global region
    region = input(Fore.BLUE + "[+] add region: ")
    os.system('w3m -dump https://www.spokeo.com/'+first_name+'-'+last_name+'/'+location+'/'+region+' > output.txt')
    print(Fore.BLUE + "==================")
    print(Style.BRIGHT + Fore.CYAN + first_name)
    print(Style.BRIGHT + Fore.CYAN + last_name)
    print(Style.BRIGHT + Fore.CYAN + region)
    print(Fore.BLUE + "==================")
    anykey=input(Fore.BLUE + "press enter")
    print(Style.BRIGHT + Fore.GREEN + "saved!")
    time.sleep(3)
    menu()

def addemail():
    print(Fore.BLUE + "[+] type the email of "+first_name+" "+last_name+" to get possible password")
    time.sleep(3)
    global mail
    mail = input(Fore.BLUE + "[+] Enter The Email : ")
    time.sleep(3)
    print(Fore.BLUE + "==================")
    print(Style.BRIGHT + Fore.CYAN + first_name)
    print(Style.BRIGHT + Fore.CYAN + last_name)
    print(Style.BRIGHT + Fore.CYAN + mail)
    print(Fore.BLUE + "==================")
    anykey=input(Fore.BLUE + "press enter")
    print(Style.BRIGHT + Fore.GREEN + "saved!")
    time.sleep(3)
    menu()

def add_phonenumber():
    print(Fore.BLUE + "[+] type the phone number of "+first_name+" "+last_name+" to get better results")
    time.sleep(2)
    print(Style.BRIGHT + Fore.YELLOW + "type the country area code for example (777)-888-9999")
    global code
    code = input(Fore.BLUE + "[+] area code: ")
    print(Style.BRIGHT + Fore.YELLOW + "[+] now type the number like this > 88809990000 then in the second line type the number like this > 888-999-0000")
    global number
    number = str(input(Fore.BLUE + "[+] add phone number: "))
    print(Style.BRIGHT + Fore.YELLOW + "[+] now type the number like this > 888-999-0000")
    global number2
    number2 = str(input(Fore.BLUE + "[+] add phone number: "))
    os.system('w3m -dump https://www.anywho.com/phone/'+number+' > phone_number.txt')
    os.system('w3m -dump https://www.thisnumber.com/'+number2+' > phone_addresses.txt')
    print(Fore.BLUE + "==================")
    print(Style.BRIGHT + Fore.CYAN + first_name)
    print(Style.BRIGHT + Fore.CYAN + last_name)
    print(Style.BRIGHT + Fore.CYAN + number)
    print(Style.BRIGHT + Fore.CYAN + number2)
    print(Fore.BLUE + "==================")
    anykey=input(Fore.BLUE + "press enter")
    print(Style.BRIGHT + Fore.GREEN + "saved!")
    time.sleep(3)
    menu()

def add_VIN():
    print(Fore.BLUE + "[+] type the VIN number of "+first_name+" "+last_name+"")
    time.sleep(3)
    global VIN
    VIN = input(Fore.BLUE + "[+] VIN number: ")
    os.system('w3m -dump https://www.vinfreecheck.com/vin/'+VIN+' > PLATE_lookup.txt')
    os.system('w3m -dump https://www.faxvin.com/vin-decoder/result?vin='+VIN+' > faxvin_lookup.txt')
    print(Fore.BLUE + "==================")
    print(Style.BRIGHT + Fore.CYAN + first_name)
    print(Style.BRIGHT + Fore.CYAN + last_name)
    print(Style.BRIGHT + Fore.CYAN + VIN)
    print(Fore.BLUE + "==================")
    anykey=input(Fore.BLUE + "press enter")
    print(Style.BRIGHT + Fore.GREEN + "saved!")
    time.sleep(3)
    menu()

def dump_place():
    print(Fore.GREEN + "[+] finding possible location from "+first_name+" "+last_name+"'s phone number")
    time.sleep(4)
    f = open("phone_number.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("City/State:", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π±π] > "+line)
    f = open("phone_number.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Street Address:", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π±π] > "+line)
          sleep(1)
    menu()

def dump_address():
    print(Fore.GREEN + "[+] finding all addresses we found searching the number you gave us")
    time.sleep(6)
    f = open("phone_addresses.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Address:", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π±π] > "+line)
          sleep(0.5)
    menu()

def dump_names():
    print(Fore.GREEN + "[+] finding all address names from the phone number you gave us")
    time.sleep(6)
    f = open("phone_addresses.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Name:", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π±π] > "+line)
          sleep(1)
    menu()

def dump_relateph():
    print(Fore.GREEN + "[+] finding all related phone numbers with the code of "+code+"")
    time.sleep(6)
    f = open("phone_addresses.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match(code, line):
          print(Style.BRIGHT + Fore.YELLOW + "[π±π] > "+line)
          sleep(0.7)
    menu()

def email_results():
    print(Fore.GREEN + "[+] dumping out information we found on the given email")
    time.sleep(8)
    key = "VrzIuNfj27KXWnHHALabdRqfBowBVciW"
    api = "https://ipqualityscore.com/api/json/email/"+key+"/"+mail+""
    response = urllib.request.urlopen(api)
    data = response.read()
    value = json.loads(data)
    print('')
    print(Style.BRIGHT + Fore.YELLOW + "[+] Success Status: " + str(value['success']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Valid: " + str(value['valid']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Disposable: " + str(value['disposable']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Honeypot: " + str(value['honeypot']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Smtp Score: " + str(value['smtp_score']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Overall Score: " + str(value['overall_score']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] First Name: " + str(value['first_name']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Generic: " + str(value['generic']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Dns Valid: " + str(value['dns_valid']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Deliverability: " + str(value['deliverability']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Frequent Complainer: " + str(value['frequent_complainer']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Spam Trap: " + str(value['spam_trap_score']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Catch All: " + str(value['catch_all']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Time Out: " + str(value['timed_out']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Abused Recently: " + str(value['recent_abuse']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Fraud Score: " + str(value['fraud_score']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Suggested Domain: " + str(value['suggested_domain']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Leaked: " + str(value['leaked']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Domain Age Human: " + str(value['domain_age']['human']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Time Stamp: " + str(value['domain_age']['timestamp']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] ISO: " + str(value['domain_age']['iso']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] First Seen: " + str(value['first_seen']['human']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] First Seen Timestamp: " + str(value['first_seen']['timestamp']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] First Seen ISO: " + str(value['domain_age']['iso']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Sanitized Email: " + str(value['sanitized_email']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Request ID: " + str(value['request_id']))
    print('')
    menu()

def dump_VINDT():
    print(Fore.GREEN + "[+] finding all vin details on "+VIN+"")
    time.sleep(7)
    f = open("PLATE_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Year", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("PLATE_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Make", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("PLATE_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Model", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("PLATE_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Trim Level", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("PLATE_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Style", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("PLATE_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Made In", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("License Plate:", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "car details")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Engine Type", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Transmission-short", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Transmission-long", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Driveline", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Locking Differential", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Traction Control", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Vehicle Stability Control System", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Seating")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Standard Seating", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Driver Multi-Adjustable Power Seat", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Front Heated Seat", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Front Power Lumbar Support", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Front Power Memory Seat", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Leather Seat", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Passenger Multi-Adjustable Power Seat", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Second Row Folding Seat", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Second Row Heated Seat", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Fuel")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Tank", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Fuel Economy-city", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Fuel Economy-highway", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Braking")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Anti-Brake System", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Front Brake Type", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Rear Brake Type", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("ABS Brakes", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Wheels and Tires")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Tires", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Alloy Wheels", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Weight")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Curb Weight-automatic", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Standard Towing", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Maximum Towing", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Standard Payload", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Maximum Payload", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Standard GVWR", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Maximum GVWR", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Dimensions")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Turning Diameter", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Front Headroom", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Rear Headroom", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Front Legroom", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Front Shoulder Room", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Rear Shoulder Room", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Overall Length", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Overall Width", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Overall Height", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Wheelbase", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Track Front", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Track Rear", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Passenger Volume", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Cargo Volume", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Suspension")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Steering Type", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Front Suspension", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Rear Suspension", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Front Spring Type", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Rear Spring Type", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Safety")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Child Safety Door Locks", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Power Door Locks", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Vehicle Anti-Theft", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Driver Airbag", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Front Side Airbag", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Passenger Airbag", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Side Head Curtain Airbag", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Second Row Side Airbag", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Electronic Parking Aid", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("First Aid Kit", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Keyless Entry", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Warranty")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Basic-duration", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Basic-distance", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Powertrain-duration", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Powertrain-distance", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Rust-duration", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Rust-distance", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Pricing")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("MSRP", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Dealer Invoice", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Destination Charge", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Lighting")
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Automatic Headlights", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Daytime Running Lights", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Fog Lights", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("High Intensity Discharge Headlights", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    print(Fore.BLUE + "============================================")
    print(Fore.BLUE + "Entertainment")
    time.sleep(2)
    f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("AM/FM Radio", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("CD Player", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("DVD Player", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
          f = open("faxvin_lookup.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Navigation Aid", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π]  > "+line)
    menu()

def socials():
    print(Fore.GREEN + "[+] finding all possible social media accounts on "+first_name+" "+last_name+"")
    time.sleep(3)
    f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.tiktok.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.instagram.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://twitter.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.amazon.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.yahoo.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.linkedin.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.youtube.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.aol.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://insurance-agent.safeco.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://viralpornhub.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.pinterest.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[π§] social profile links > "+line)
          sleep(1)
    menu()

menu()
