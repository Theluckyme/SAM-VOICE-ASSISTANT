from take_command import speak
import requests
import json
from urllib.request import urlopen

def get_ip_detail(ip=None):
    if ip is None:
        url = 'http://ipinfo.io/json'
    else:
        url = f'http://ipinfo.io/{ip}/json'
    response = urlopen(url)
    data = json.loads(response.read().decode())
    return data
    

def ip_info():
    data = get_ip_detail()
    ip = data['ip']
    speak(f"Your IP address is {ip}")

def city_info():
    data = get_ip_detail()
    city = data['city']
    speak(f"You are now in {city}")