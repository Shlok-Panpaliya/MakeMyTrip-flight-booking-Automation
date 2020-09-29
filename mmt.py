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
    departure_date
)

class YatraAPI:
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
        
      #  self.choose_flight()
       # print("review")
       # self.review()
      #  self.travelers_detail()
       # self.driver.quit()
        #self.final_payment()
    def to_from_date(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='toCity']").send_keys(arrive)
    #    self.driver.find_element_by_id("toCity").send_keys(arrive)
        time.sleep(1)
        self.act.send_keys(Keys.DOWN,Keys.ENTER).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='fromCity']").send_keys(depart)
        self.act.send_keys(Keys.DOWN,Keys.ENTER).perform()
       # time.sleep(2)
        
        #self.act.send_keys(Keys.TAB,Keys.TAB).perform()
        #time.sleep(1)

       # self.driver.find_element_by_class_name('widgetSearchBtn').click()
        #ele = self.driver.find_element_by_xpath("//div[@class='DayPicker-Day']")
        
       # time.sleep(1)
       # ele.click()
     #   self.act.send_keys(Keys.ENTER).perform()
     #   time.sleep(1)
       # self.choose_flight()
    def get_date(self):
        time.sleep(1)
        element = self.driver.find_element_by_xpath("//p[@data-cy='departureDate']")
        #element = self.driver.find_element_by_class_name('latoBold appendBottom10')
       # print(element)
      #  time.sleep(2)
        element.click()

      #  check = self.driver.find_element_by_xpath("//div[]")

        check = self.driver.find_element_by_xpath("//div[@aria-label='" +departure_date+ "']")
        check.click()
        # time.sleep(5)
        #print(check.)
        if check.get_attribute('aria-disabled') == 'false':
            check.click()
        else:
            print("Flight not available on that day") 
                        

    def choose_flight(self):
        self.driver.get('https://www.makemytrip.com/flight/search?itinerary=BOM-GAU-30/09/2020&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E')
        time.sleep(8)
        element = self.driver.find_elements_by_class_name('ViewFareBtn')
        #element1 = self.driver.find_elements_by_class_name('actual-price')
        element2 = self.driver.find_elements_by_class_name('fli_primary_btn')
        print(element,element2)
        flag = 0
        #element2[0].click()
        if not element:
          #  print('hi')
           # self.act.click_and_hold(element2[0])
            #self.act.release(element2[0])
          
          
            #     print('hi1')
            element2[0].click()
            
            
        else:
            
            
            element[0].click()
            time.sleep(1)
            element2[0].click()
        time.sleep(5)
    def review(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
    #    self.driver.get('https://www.makemytrip.com/flight/review/?itineraryId=588fc7a93edf21f096f8425be35f65d1525b7c91&rKey=RKEY:48e61b65-58d5-4c81-a9e3-58d03ca72429:11_0&crId=4d107627-16e7-4504-84d0-b3f8e14e72c8&cur=INR&openFF=undefined&xflt=eyJjIjoiRSIsInAiOiJBLTFfQy0wX0ktMCIsInQiOiIiLCJzIjoiQk9NLUdBVS0yMDIwMDkzMCJ9&ccde=IN')
       # time.sleep(2)
        print(self.driver.current_url)
        element = self.driver.find_element_by_xpath("//input[@type='radio']")
        time.sleep(1)
        element.click()
       
            
        time.sleep(1)
        element1 = self.driver.find_element_by_class_name('fli_primary_btn')
        time.sleep(2)
        element1.click() 
    def travelers_detail(self):
        self.driver.get('https://www.makemytrip.com/flight/traveller/?itineraryId=87aab543d283ad4c0c11e240cbaba425be4a16da&crId=cfba6ce3-e0c6-407f-8831-342f2c88ec6a&cur=INR')
       # element = self.driver.find_element_by_xpath("//p[@class='viewAll-trvlr']/a")
        time.sleep(2)
        ele = self.driver.find_elements_by_class_name('font14')
       # print(ele)
        for i in ele:
        #    print(i.text)
            if i.text == '+ ADD ADULT':
                add = i
         #       print('hi')
        add.click()
        arr = self.driver.find_elements_by_class_name('tvlrInput')
        arr[0].send_keys('Shlok')
        arr[1].send_keys('Panpaliya')
        self.driver.find_element_by_xpath("//label[@tabindex='0']").click()
        arr[2].send_keys('1234567891')
        arr[3].send_keys('asd@gmail.com')
        self.driver.find_element_by_class_name('ack-cta').click()

    def final_payment(self):
        self.driver.get('http://makemytrip.com/flight/ancillary/?crId=cfba6ce3-e0c6-407f-8831-342f2c88ec6a&itineraryId=87aab543d283ad4c0c11e240cbaba425be4a16da')
        time.sleep(2)
        e = self.driver.find_elements_by_class_name('ancillary-nav-icon')[1]
        time.sleep(1)
        e.click()
        e1 = self.driver.find_element_by_id('ancillary-secondary')
        time.sleep(1)
        self.act.click(e1)
        #time.sleep(2)
       # print(e1.text)
        #e1.click()

        
if __name__ == "__main__":
    Yatra = YatraAPI(base_url)
    Yatra.run_script()
    