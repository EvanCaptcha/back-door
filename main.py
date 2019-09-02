import requests
import time
import threading
from botoptions import *
from pypresence import Presence
import urllib.request
from bs4 import BeautifulSoup
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

threads=10
global apilink
size = '7-5'
def getcookies () :
    time.sleep(0.1)
    s = requests.session()
    s = requests.session()
    s = requests.session()
    s = requests.session()
    s = requests.session()
    apic = requests.get(apilink)
    soup = BeautifulSoup(apic.content, 'html.parser')
    pid = soup.find(attrs={"name": "product_id"})
    output = pid['value']
    r = requests
    s = requests.session()
    s.cookies.clear()
    variant = int(output)+ int(1)
    atclink = apilink + "?attribute_pa_size=" + str(size) + "&quantity=1&add-to-cart=" + str(output) + "&product_id=" + str(output) + "&variation_id=" + str(variant)
    s.cookies.clear()
    s.cookies.clear()
    s.cookies.clear()
    atc = s.get(atclink)
    print(atc.status_code)
    if atc.status_code != 200:
        print('failed')
        exit(0)
    print(bcolors.OKGREEN + "PRODUCT ADDED TO CART - ")
    print('Your cookies were written to cookies.txt!')
    cookies = s.cookies.get_dict()
    cookies_json = json.dumps(cookies, sort_keys=True)
    f=open("cookies.txt","a")
    f.write(str(cookies_json + '\n'))
    f.close()
    print(bcolors.OKGREEN + "PROCEDING TO CHECKOUT!")
    webhook = 'https://discordapp.com/api/webhooks/617541633583349781/s7bwho1Jq_ZYzW20144hGsX954ex6rQgdM3P6-JV4tDv858__i5LzPdT6BhGEa4lWLUX'
    s.cookies.clear()


url = 'http://entibot.atwebpages.com/jndjksajoOUIAJHDuoisahndsa.html'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
apilink = soup.get_text()
print(apilink)
print('Starting monitor on shared server')
while 'API' in apilink:
    url = 'http://entibot.atwebpages.com/jndjksajoOUIAJHDuoisahndsa.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    apilink = soup.get_text()
print('Product loaded on API!')
# create threads
jobs = []
for i in range(0, threads):
    jobs.append(threading.Thread(target=getcookies))

# start  threads
for j in jobs:
    j.start()

# ensure all threads have been finished
for j in jobs:
    j.join()


