from selenium import webdriver
import warnings

warnings.filterwarnings('ignore')

# browser=webdriver.Chrome("/Cress/Drivers/chromedriver")

def peek(url):
	browser.get(url)
	browser.quit()

