import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Drom:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):       
        self.driver = webdriver.Chrome
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def set_region(self):
        
        self.driver.get("https://www.drom.ru")
        wait = WebDriverWait(self.driver, 15)
        change_region_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-ga-stats-name='HomeRegionChange']")))
        change_region_link.click()
        omsk_region_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Омская область')]")))
        omsk_region_link.click()   

    def reviews_search(self):
        
        self.driver.get("https://www.drom.ru")  
        wait = WebDriverWait(self.driver, 15)                 
        reviews_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/reviews/']")))
        reviews_link.click()                
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='bmw']"))).click()        
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='m5']"))).click()

    def tire_search(self):
        
        self.driver.get("https://www.drom.ru")
        wait = WebDriverWait(self.driver, 15)
        tire_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-ga-stats-name='topmenu_tire']")))        
        tire_link.click()
        search_tire = self.driver.find_element(By.CSS_SELECTOR, "input[name='query']")
        search_tire.send_keys("Pirelli")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value*='summer']"))).click()
        search_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        search_button.click()


    def catalog_search(self):
        
        self.driver.get("https://www.drom.ru") 
        wait = WebDriverWait(self.driver, 15)       
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/catalog/']"))).click()        
        catalog_search_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-ga-stats-name='advanced_search']")))
        catalog_search_link.click()       
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='only_actual']"))).click()       
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type*='submit']"))).click()

    def spare_parts_search(self):
        
        self.driver.get("https://www.drom.ru") 
        wait = WebDriverWait(self.driver, 15)         
        parts_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/sell_spare_parts/']")))
        parts_link.click()        
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='query']")
        search_input.send_keys("шаровая опора")         
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-url-label*='dopolnitelno']"))).click()        
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value*='new']"))).click()        
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-label*='Запчасть']"))).click()        
        search_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        search_button.click()
