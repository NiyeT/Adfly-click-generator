from selenium import webdriver
import warnings

warnings.filterwarnings('ignore')

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
	
browser=webdriver.PhantomJS("/usr/local/bin/phantomjs")

# browser=webdriver.Chrome("/Cress/Drivers/chromedriver")

def visit(url):
	return browser.get(url)

def peek(url):
	visit(url)
	# browser.quit()

peek("http://zipansion.com/pm56")
# peek("https://google.com")