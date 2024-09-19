from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc


class SearchAgent:


    def __init__(self) -> None:
        self.options = Options()
        self.options.add_argument('--headless')  # Run Chrome in headless mode
        self.options.add_argument('--no-sandbox')  # Bypass OS security model
        self.options.add_argument('--disable-dev-shm-usage')  # Avoids issues with shared memory
        self.options.add_argument('--locale=en_us')
        self.driver=uc.Chrome(options=self.options)
        
    def search(self,query):
        pass