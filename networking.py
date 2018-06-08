import requests

def ip():
	ip_raw=requests.get('http://ip.42.pl/raw').text
	return ip_raw