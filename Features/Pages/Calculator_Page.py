import json
from Features.Pages.BasePage import Basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class Calculator_page(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context

    data = json.load(open('Features/Resources/config.json'))

    def EnterNumber(self, number):
        for s in number:
            elem = self.driver.find_element("xpath", "//span[@onclick=\'r(" + s + ")\']")
            elem.click()

    def selectOperation(self, Operator):
        elem = self.driver.find_element("xpath", "//span[@onclick=\"r(\'" + Operator + "\')\"]")
        elem.click()

    def ReturnResult(self):
        elem = self.driver.find_element(By.ID, "sciOutPut")
        result = (elem.text).strip()
        return result
