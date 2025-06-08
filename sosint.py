#!/data/data/com.termux/files/usr/bin/python3

import os
import requests
import socket
import json
from datetime import datetime
import argparse

# Цвета для вывода
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('clear')

def print_banner():
    banner = f"""
{colors.HEADER}{colors.BOLD}
▓█████▄  ██▓▓█████  ███▄ ▄███▓
▒██▀ ██▌▓██▒▓█   ▀ ▓██▒▀█▀ ██▒
░██   █▌▒██▒▒███   ▓██    ▓██░
░▓█▄   ▌░██░▒▓█  ▄ ▒██    ▒██ 
░▒████▓ ░██░░▒████▒▒██▒   ░██▒
 ▒▒▓  ▒ ░▓  ░░ ▒░ ░░ ▒░   ░  ░
 ░ ▒  ▒  ▒ ░ ░ ░  ░░  ░      ░
 ░ ░  ░  ▒ ░   ░   ░      ░   
   ░     ░     ░  ░       ░   
 ░                             
{colors.ENDC}
{colors.OKBLUE}Termux OSINT Toolkit v1.0{colors.ENDC}
"""
    print(banner)

def check_ip(ip):
    print(f"\n{colors.OKBLUE}[*] Проверка IP: {ip}{colors.ENDC}")
    try:
        # Проверка через ip-api.com
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
        data = response.json()
        
        if data['status'] == 'success':
            print(f"{colors.OKGREEN}Информация об IP:{colors.ENDC}")
            print(f"Страна: {data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
            print(f"Регион: {data.get('regionName', 'N/A')} ({data.get('region', 'N/A')})")
            print(f"Город: {data.get('city', 'N/A')}")
            print(f"Почтовый индекс:
