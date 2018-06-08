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