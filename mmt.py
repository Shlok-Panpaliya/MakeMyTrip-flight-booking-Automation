import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from config import(
    get_chrome_web_driver,
    get_web_driver_options,
    set_ignore_certificate_error,
    set_browser_as_incognito,
    base_url,
    depart,
    arrive,
    departure_date,
    secure,
    covid
)

class MMTApi:
    def __init__(self,base_url):
        
        options = get_web_driver_options()
        set_browser_as_incognito(options)
        self.base_url = base_url
        self.driver = get_chrome_web_driver(options)
        set_ignore_certificate_error(options)
        #self.arrive = arrive
        self.act = ActionChains(self.driver)
        
        
    
    def run_script(self):
        
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.to_from_date()
        self.get_date()
        self.choose_flight()
        self.review()
        self.travelers_detail()
        self.go_to_payment()
        self.final_checkout()
        time.sleep(2)
        self.driver.quit()
    def to_from_date(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='toCity']").send_keys(arrive)
    #    self.driver.find_element_by_id("toCity").send_keys(arrive)
        time.sleep(1)
        self.act.send_keys(Keys.DOWN,Keys.ENTER).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='fromCity']").send_keys(depart)
        self.act.send_keys(Keys.DOWN,Keys.ENTER).perform()
    
    def get_date(self):
        time.sleep(2)
        element = self.driver.find_element_by_xpath("//p[@data-cy='departureDate']")
        
        time.sleep(2)
        element.click()

        check = self.driver.find_element_by_xpath("//div[@aria-label='" +departure_date+ "']")

        if check.get_attribute('aria-disabled') == 'false':
            check.click()
        else:
            print("Flight not available on that day") 
        
        self.driver.find_element_by_class_name('widgetSearchBtn').click()
                        

    def choose_flight(self):
    
        time.sleep(5)
        element = self.driver.find_elements_by_class_name('ViewFareBtn')
        #element1 = self.driver.find_elements_by_class_name('actual-price')
        element2 = self.driver.find_elements_by_class_name('fli_primary_btn')
       # print(element,element2)
        #flag = 0
        #element2[0].click()
        if not element:
            element2[0].click()
        else:
            element[0].click()
            time.sleep(1)
            element2[0].click()
        time.sleep(2)

    def review(self):
       
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        time.sleep(2)
        #print(self.driver.current_url)
        
        if secure == 'y':
            element = self.driver.find_elements_by_xpath("//input[@type='radio']")[0]
            time.sleep(1)
            element.click()
        else:
            element = self.driver.find_elements_by_xpath("//input[@type='radio']")[1]
            print(element)    
            time.sleep(1)
            element.click()
       
        time.sleep(1)
        element1 = self.driver.find_element_by_class_name('fli_primary_btn')
        time.sleep(2)
        element1.click() 

    def travelers_detail(self):
      
        time.sleep(2)
        ele = self.driver.find_elements_by_class_name('font14')
        for i in ele:
        #    print(i.text)
            if i.text == '+ ADD ADULT':
                add = i
         #       print('hi')
        time.sleep(1)
        add.click()
        arr = self.driver.find_elements_by_class_name('tvlrInput')
        arr[0].send_keys('Shlok')
        arr[1].send_keys('Panpaliya')
        gender = self.driver.find_element_by_xpath("//label[@tabindex='0']")
        time.sleep(1)
        gender.click()
        arr[2].send_keys('1234567891')
        arr[3].send_keys('asd@gmail.com')
        time.sleep(2)
        if covid =='y':
            covid_test = self.driver.find_element_by_xpath("//a[@class='font16 LatoBold paddL15']")
            time.sleep(2)
            covid_test.click()
        time.sleep(2)
        self.driver.find_element_by_class_name('ack-cta').click()


    def go_to_payment(self):
        time.sleep(2)
        okay1 = self.driver.find_element_by_class_name('fli_secondry_btn')
        time.sleep(1)
        okay1.click()
        time.sleep(1)
      #  okay.click() 
       # time.sleep(1)
        payment_page = self.driver.find_element_by_xpath("//a[@id='ancillary-secondary']")
        time.sleep(1)
        payment_page.click()
        time.sleep(2)
        skip = self.driver.find_element_by_class_name('fli_secondry_btn')
        skip.click()
       # e = self.driver.find_elements_by_class_name('ancillary-nav-icon')[1]
       # time.sleep(1)
       # e.click()
       # e1 = self.driver.find_element_by_id('ancillary-secondary')
       # time.sleep(1)
       # self.act.click(e1)
        #time.sleep(2)
       # print(e1.text)
        #e1.click()
    def final_checkout(self):
      
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        print(self.driver.current_url)
        card = self.driver.find_elements_by_xpath("//li[@class='tab_section_list']")
        #card = self.driver.find_elements_by_class_name('tab_section_list')
        time.sleep(2)
        card[2].click()
        time.sleep(1)
        card_no = self.driver.find_element_by_xpath("//input[@id='PAYMENT_cardNumber']")
        card_no.send_keys('12121212121212')
        name = self.driver.find_element_by_xpath("//input[@id='PAYMENT_nameOnCard']")
        name.send_keys('Shlok Panpaliya')
       # expiry_month = self.driver.find_element_by_xpath("//select[@id='PAYMENT_expiryMonth']").click()

if __name__ == "__main__":
    MMT = MMTApi(base_url)
    MMT.run_script()
    