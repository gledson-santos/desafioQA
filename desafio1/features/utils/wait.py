from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from features.utils.web_app import webapp
from time import sleep

class Wait(object):

    def __init__(self):
        self.driver = webapp.get_driver()
        self.wait = WebDriverWait(self.driver, 5)


    def aguardar_elemento_ficar_visivel_xpath(self, elemento):
        tentativas = 0
        while True:
            elemento = self.wait.until(EC.visibility_of_element_located((By.XPATH, elemento)))
            tentativas += 1
            if elemento is not None or tentativas > 3:
                return
            sleep(1)


    def aguardar_xpath_clicavel(self, elemento):
        tentativas = 0
        while True:
            elemento = self.wait.until(EC.element_to_be_clickable((By.XPATH, elemento)))
            tentativas += 1
            if elemento is not None or tentativas > 3:
                return
            sleep(1)
