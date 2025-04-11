#!/usr/bin/python3
import requests
import sys



miner = sys.argv[1]
site = sys.argv[2]


url = 'http://' + str(site) + 'mine.ddns.net:5000/reboot?miner=' + str(miner) + '&site=' + str(site)

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
