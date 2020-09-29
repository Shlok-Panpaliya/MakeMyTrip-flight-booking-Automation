from selenium import webdriver

base_url = 'https://www.makemytrip.com/'
#depart = input("Enter city to depart from")
#arrive = input("Enter city to arrive at")
depart = 'Mumbai'
arrive = 'Guwahati'

def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver',chrome_options = options)

def get_web_driver_options():
    return webdriver.ChromeOptions()
def set_browser_as_incognito(options):
    options.add_argument('--incognito')