import expressvpn
import browser
import networking

# serverStorage=expressvpn.list_locations()

ipStorage=[]

#check if ip has already been used
def unique_ip_check(attempts=3):
	my_ip=networking.ip()
	for address in ipStorage:
		if(address==my_ip):
			return False
	ipStorage.append(my_ip)
	return True
	
#increase adfly view count
def view(url):
	expressvpn.connect()
	if(unique_ip_check()):
		browser.visit(url)
		expressvpn.disconnect()
