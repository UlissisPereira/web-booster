from time import sleep
from random import choice
from services.log import Log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver:
    webdriver = None
    log = Log()

    def __init__(self) -> None:
        try:
            options = webdriver.FirefoxOptions()
            options.add_argument("-headless")
            options.set_preference('geo.prompt.testing', True)
            options.set_preference('geo.prompt.testing.allow', True)
            options.set_preference('geo.provider.network.url',
                                   'data:application/json,{"location": {"lat": -15.587636, "lng": -56.083424}, '
                                   '"accuracy": 100.0}')
            options.set_preference('geo.wifi.uri', 'data:application/json,{"location": {"lat": -15.587636, '
                                                   '"lng": -56.083424}, "accuracy": 100.0}')
            options.set_preference('binary', 'services/drivers/geckodriver')
            options.set_preference('profile', 'services/drivers/profile')
            self.webdriver = webdriver.Firefox(options=options)
        except Exception as e:
            self.log.log_error.error("{} : {} : {}".format("Init error", type(e).__name__, e))

    def run(self) -> None:
        try:
            delay = 45

            url = "https://circuitomt.com.br/"
            self.webdriver.get(url)
            WebDriverWait(self.webdriver, delay).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "pfy-post-title")))
            links = self.webdriver.find_elements(By.CLASS_NAME, "pfy-post-title")
            pai = choice(links)
            children = pai.find_element(By.TAG_NAME, "a")
            if type(children) is not list:
                link = children
                url = link.get_attribute("href")
            else:
                link = choice(children)
                url = link.get_attribute("href")
            self.webdriver.execute_script("arguments[0].click();", link)
            self.webdriver.implicitly_wait(120)
            self.webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(delay)
            self.log.log_info.info("Acesso realizado com sucesso - url: {}".format(url))
        except Exception as e:
            self.log.log_error.error("{} : {} : {}".format("Execute error", type(e).__name__, e))
        finally:
            self.webdriver.quit()
