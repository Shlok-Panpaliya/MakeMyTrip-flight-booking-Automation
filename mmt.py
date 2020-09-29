import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from config import(
    get_chrome_web_driver,
    get_web_driver_options,
    set_browser_as_incognito,
    base_url,
    depart,
    arrive
)

class YatraAPI:
    def __init__(self,base_url):
        
        options = get_web_driver_options()
      #  set_ignore_certificate_error(options)
        set_browser_as_incognito(options)
        self.base_url = base_url
        self.driver = get_chrome_web_driver(options)
        
        
        #self.arrive = arrive
        
        
    
    def run_script(self):
        
        self.driver.get(base_url)
        act = ActionChains(self.driver)
        
        self.driver.find_element_by_id("toCity").send_keys(arrive)
        time.sleep(3)
        act.send_keys(Keys.DOWN,Keys.ENTER).perform()
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@id='fromCity']").send_keys(depart)
        act.send_keys(Keys.DOWN,Keys.ENTER).perform()
        
        time.sleep(2)
        self.driver.quit()
if __name__ == "__main__":
    Yatra = YatraAPI(base_url)
    Yatra.run_script()
    