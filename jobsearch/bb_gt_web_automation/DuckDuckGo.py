from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class DuckDuckGo:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')  # Run Chrome in headless mode
        options.add_argument('--no-sandbox')  # Bypass OS security model
        options.add_argument('--disable-dev-shm-usage')  # Avoid issues with shared memory
        options.add_argument('--locale=en_us')
        self.driver = webdriver.Chrome(options=options)
    
    def search(self, query):
        query = query.replace(' ','+')
        search_results = self.driver.get("https://duckduckgo.com/?q=" + query)
        self.driver.implicitly_wait(5)  # Wait for the results to load
        search_results = self.driver.find_elements(By.XPATH, "//*/div[2]/h2/a")
        result_links = [result.get_attribute("href") for result in search_results]
        return result_links


    def close(self):
        self.driver.quit()