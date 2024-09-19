from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver as uc
import Levenshtein

class Website:
    
    def __init__(self,url) -> None:
        self.options = Options()
        self.options.add_argument('--headless')  # Run Chrome in headless mode
        self.options.add_argument('--no-sandbox')  # Bypass OS security model
        self.options.add_argument('--disable-dev-shm-usage')  # Avoids issues with shared memory
        self.options.add_argument('--locale=en_us')
        self.driver = uc.Chrome(options=self.options)
        self.forms = None
        self.texts = None
        self.passwords = None
        self.checkboxes = None
        self.radios = None
        self.submits = None
        self.resets = None
        self.files = None
        self.hiddens = None
        self.buttons = None
        self.links = None
        self.get_page_elements_into_a_dict(url)
    
    
    def is_signed_up(self):
        False
    
    def sign_up(self):
        variations = ["Register", "Create an account", "Join", "Enroll", "Become a member", "Sign in", "Sign on", "Subscribe", "Opt-in", "Participate", "Get started", "Access", "Sign me up", "Join now", "Start now"]

        
        if not self.is_signed_up():
            sign_up_element = self.find_closest_element_in_computational_distance(variations=variations,elements=(self.links+self.buttons+self.submits))
            sign_up_element.click()
        
        
    def sign_in(self):
        pass
        
    def confirm_registration(self):
        pass
        
    def second_factor_authentication(self):
        pass
    
    def find_jobs(self):
        pass
    
    def apply_job(self):
        pass
    

    def get_page_elements_into_a_dict(self,link):
        self.driver.get(link)
        page_title = self.driver.title
        print("Website:", link)
        print("Page Title:", page_title)
            
        try:
            if self.forms is None:
                self.forms = self.driver.find_elements(By.XPATH, "//form")
            if self.texts is None:
                self.texts = self.driver.find_elements(By.XPATH, "//input[@type='text']")
            if self.passwords is None:
                self.passwords = self.driver.find_elements(By.XPATH, "//input[@type='password']")
            if self.checkboxes is None:
                self.checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
            if self.radios is None:
                self.radios = self.driver.find_elements(By.XPATH, "//input[@type='radio']")
            if self.submits is None:
                self.submits = self.driver.find_elements(By.XPATH, "//input[@type='submit']")
            if self.resets is None:
                self.resets = self.driver.find_elements(By.XPATH, "//input[@type='reset']")
            if self.files is None:
                self.files = self.driver.find_elements(By.XPATH, "//input[@type='file']")
            if self.hiddens is None:
                self.hiddens = self.driver.find_elements(By.XPATH, "//input[@type='hidden']")
            if self.buttons is None:
                self.buttons = self.driver.find_elements(By.XPATH, "//button")
            if self.links is None:
                self.links = self.driver.find_elements(By.XPATH, "//a")
        except NoSuchElementException:
            # handle the case where no form element is found
            print("No form element found on the page.")
        self.driver.close()
        
        return {
            'forms': self.forms,
            'texts': self.texts,
            'passwords': self.passwords,
            'checkboxes': self.checkboxes,
            'radios': self.radios,
            'submits': self.submits,
            'resets': self.resets,
            'files': self.files,
            'hiddens': self.hiddens,
            'buttons': self.buttons,
            'links': self.links
        }
        
    def close_connection(self):
        # Quit the WebDriver session
        self.driver.quit()
        
    def get_input_purpose(self,element):
        input_location = element.location
        input_size = element.size

        # Check if the element has a direct label association using <label> tag
        try:
            label = element.find_element(By.XPATH, ".//label")
            return [label.text.strip()]
        except NoSuchElementException:
            pass
        
        # Check if the element has a placeholder attribute
        placeholder = element.get_attribute("placeholder")
        if placeholder:
            return [placeholder.strip()]
        
        # Check if there is nearby text within the same parent container
        parent = element.find_element(By.XPATH, "./..")
        sibling_text = parent.find_elements(By.XPATH, ".//*[text()][not(self::label)]")
        
        closest_texts = []
        min_distance = float('inf')
        
        for text_element in sibling_text:
            text = text_element.text.strip()
            if text:
                text_location = text_element.location
                text_size = text_element.size
                
                # Calculate the vertical distance between the input and text elements
                y_distance = abs(input_location['y'] - text_location['y'])
                
                # Calculate the horizontal distance between the input and text elements
                x_distance = abs(input_location['x'] - text_location['x'] - input_size['width'])
                
                # Calculate the total pixel distance between the input and text elements
                distance = (y_distance ** 2 + x_distance ** 2) ** 0.5
                
                # Update the closest texts if the distance is smaller
                if distance < min_distance:
                    closest_texts = [text]
                    min_distance = distance
                elif distance == min_distance:
                    closest_texts.append(text)
        
        if closest_texts:
            return closest_texts
        
        # Check if the element has a custom data attribute with hints
        data_attribute = element.get_attribute("data-hint")
        if data_attribute:
            return [data_attribute.strip()]
        
        # Check if the element has a CSS class or ID with hints
        css_class = element.get_attribute("class")
        if css_class:
            return [css_class.strip()]
        
        element_id = element.get_attribute("id")
        if element_id:
            return [element_id.strip()]
        
        # Return an empty list if no hints are found
        return []

    def find_closest_element_in_computational_distance(self, variations=None, elements=None):
        closest_element = None
        min_distance = float('inf')

        for variation in variations:
            variation_lower = variation.lower()
            
            for element in elements:
                element_strings = self.get_input_purpose(element)
                
                for each_element_string in element_strings:
                    each_element_string_lower = each_element_string.lower()
                    distance = Levenshtein.distance(variation_lower, each_element_string_lower)

                    if distance < min_distance:
                        min_distance = distance
                        closest_element = element

        return closest_element

