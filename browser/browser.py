from selenium import webdriver
import warnings

warnings.filterwarnings('ignore')

temp="http://zipansion.com/pm56"

# browsers={
# 	"Chrome":{
# 		"dir":"/Cress/Drivers/chromedriver"
# 	},
# 	"Firefox":{
# 		"dir":"/Cress/Drivers/geckodriver"
# 	}
# }

# active_browser="Chrome"

# browser_location=browsers[active_browser]['dir']

# browser=vars(webdriver)[active_browser](browser_location)
	
browser=webdriver.Chrome("/Cress/Drivers/chromedriver")

# browser=webdriver.Chrome("/Cress/Drivers/chromedriver")

def visit(url):
	return browser.get(url)

def peek(url):
	visit(url)
	# browser.quit()

# peek("http://zipansion.com/pm56")

print(visit(temp))

