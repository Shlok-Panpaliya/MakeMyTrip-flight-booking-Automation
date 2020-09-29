from selenium import webdriver

base_url = 'https://www.makemytrip.com/'
#depart = input("Enter city to depart from")
#arrive = input("Enter city to arrive at")
#departure_date = input("Enter date in the format of day month day year")

depart = 'Pune'
arrive = 'Jaipur'
departure_date = 'Thu Oct 08 2020'

def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver',chrome_options = options)

def get_web_driver_options():
    return webdriver.ChromeOptions()
def set_browser_as_incognito(options):
    options.add_argument('--incognito')

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')