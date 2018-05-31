from os import system
import re

def command(commands):
	response=str(system(commands))
	len_response=len(response)
	clean_resp=response[0:len_response-1]
	return clean_resp