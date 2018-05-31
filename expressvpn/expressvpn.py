# from expressvpn import wrapper
# import logging
# from json import load
# from urllib2 import urlopen

# print(wrapper.random_connect)

# public_ip = load(urlopen('http://jsonip.com'))['ip']
# print(public_ip)

# def main():
#     while True:
#         try:
#             scrape()
#         except BannedException as be:
#             logging.info('BANNED EXCEPTION in __MAIN__')
#             logging.info(be)
#             logging.info('Lets change our PUBLIC IP GUYS!')
#             change_ip()
#         except Exception as e:
#             logging.error('Exception raised.')
#             logging.error(e)



# def change_ip():
#     max_attempts = 10
#     attempts = 0
#     while True:
#         attempts += 1
#         try:
#             logging.info('GETTING NEW IP')
#             wrapper.random_connect()
#             logging.info('SUCCESS')
#             return
#         except Exception as e:
#             if attempts > max_attempts:
#                 logging.error('Max attempts reached for VPN. Check its configuration.')
#                 logging.error('Browse https://github.com/philipperemy/expressvpn-python.')
#                 logging.error('Program will exit.')
#                 exit(1)
#             logging.error(e)
#             logging.error('Skipping exception.')

import shell

ip=None

server_num=0

def list_locations():
    return shell.command("expressvpn list")

def connect(location):
    location=" "+location
    if(not location):
        command="expressvpn connect"
    else:
        command="expressvpn connect" + location
    try:
        return  shell.command(command)
    except Exception:
        return False

def disconnect():
    return shell.command("expressvpn disconnect")

def attempt(action,attempts=int):
    for attempt in attempts:
        try:
            action()
            return True
        except Exception():
            pass
    return False

def change_ip(location=""):
    disconnect()
    connect(location)

def change_server(location):
    locations=list_locations()
    disconnect()
    if(not location):
        if(server==len(locations)-1):
            server=0
        location=locations[location]
    if(connect(location)):
        return True
    else:
        return False

print(list_locations())