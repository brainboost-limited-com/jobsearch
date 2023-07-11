from bb_gt_web_automation.SearchAgent import SearchAgent
from selenium.webdriver.common.keys import Keys

class DuckDuckGo(SearchAgent):
    
    def __init__(self):
        super.__init__(self)
        
        
    def search(self,query):
        # Find the search box and enter the search query
        search_box = self.driver.find_element_by_name('q')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        self.driver.implicitly_wait(10)

        # Find the first result link and print its href attribute
        first_result = self.driver.find_element_by_css_selector('#links .result__url')
        print(first_result.get_attribute('href'))

        # Close the browser window
        self.driver.quit()
