import expressvpn
import browser
import networking

current_location="usa - los angeles - 1"

ipStorage=[]

unique_ip_attempts=0

def change_server(current_location):
	new_location=expressvpn.change_server(current_location)
	current_location=new_location
	return new_location

#check if ip has already been used
def unique_ip_check(attempts=3):
	my_ip=networking.ip()
	for address in ipStorage:
		if(address==my_ip):
			if(unique_ip_attempts == 3):
				change_server()
				ipStorage=[]
				unique_ip_attempts=0
			return False
	ipStorage.append(my_ip)
	return True
	
#increase adfly view count
def view(url):
	expressvpn.connect(current_location)
	if(unique_ip_check()):
		browser.visit(url)
	expressvpn.disconnect()

def start():
	while(True):
		view("http://zipansion.com/pm56")

