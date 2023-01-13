from time import sleep
from random import choice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver:        
    def run(self) -> None:
        try:
            delay = 45
            options = webdriver.FirefoxOptions()
            options.add_argument("-headless")
            options.set_preference('geo.prompt.testing', True)
            options.set_preference('geo.prompt.testing.allow', True)
            options.set_preference('geo.provider.network.url','data:application/json,{"location": {"lat": -15.587636, "lng": -56.083424}, "accuracy": 100.0}')
            driver = webdriver.Firefox(service_log_path="logs/geckodriver.log",options=options)
            url = "http://circuitomt.com.br/"
            driver.get(url)
            div = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "cookieinfo-close")))
            div.click()
            WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "overlay-link")))
            links = driver.find_elements(By.CLASS_NAME, "overlay-link")
            link  = choice(links)
            driver.execute_script("arguments[0].click();",link)
            driver.implicitly_wait(120)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(delay)
        finally:
            driver.quit()