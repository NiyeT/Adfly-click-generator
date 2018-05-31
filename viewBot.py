import expressvpn
import browser
import schedule

# serverStorage=expressvpn.list_locations()

ipStorage=[]

def unique_ip_check(attempts=3):
	my_ip=getMyIP()
	for attempt in attempts:
		if(ipStorage.index(my_ip)):
			expressvpn.change_ip()
		else:
			ipStorage.append(my_ip)
			return True
	expressvpn.change_server()

def view(url="http://zipansion.com/pm56"):
	expressvpn.connect()
	unique_ip_check()
	browser.visit(url)
	expressvpn.disconnect()

browser.view("http://zipansion.com/pm56")