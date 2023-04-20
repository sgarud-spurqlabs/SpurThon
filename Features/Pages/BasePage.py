from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Basepage(object):
    def __init__(self,driver):
        self.driver=driver
        self.wait =WebDriverWait(self.driver,30)
        self.implicit_wait=25

    def element_click(self,path):
        element=self.wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        element.click()

