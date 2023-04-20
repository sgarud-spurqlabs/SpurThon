import json
from selenium import webdriver
from datetime import datetime
import os

from allure_commons.types import AttachmentType
from allure_commons._allure import attach
from Features.Pages.BasePage import Basepage
from Features.Pages.Calculator_Page import Calculator_page
from webdriver_manager.chrome import ChromeDriverManager

data = json.load(open("Features/Resources/config.json"))


# def before_all(context):
#    #print("Before all")
#    now=datetime.now()
#    d1=now.strftime("%d_%m_%y_%H_%M_%S")
#    context.dirname="SpecLink_"+d1
#    os.mkdir("Features/TestResults/"+context.dirname)

def before_scenario(context, scenario):
    # context.driver=webdriver.Chrome(executable_path=data['driver_path'])
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    baseobject = Basepage(context.driver)
    context.driver.get(data["app_Url"])
    context.driver.maximize_window()
    context.calcpage = Calculator_page(baseobject)
    # scenarioname = (((((str(scenario)).replace(" ", "")).replace("<", "")).replace(">", "")).replace("Scenario", "")).replace('"','')
    # os.mkdir("Features/TestResults/" + context.dirname + "/" + scenarioname)
    # context.filepath = "Features/TestResults/" + context.dirname + "/" + scenarioname + "/"
    context.stepid = 1


def after_step(context, step):
    # if 'I start decorators check case 2' in str(step):
    # print ('==After Step==' + str(step))
    # context.driver.save_screenshot(context.filepath + str(context.stepid) + '.png')
    attach(context.driver.get_screenshot_as_png(), name=str(context.stepid), attachment_type=AttachmentType.PNG)
    context.stepid = context.stepid + 1


def after_scenario(context, scenario):
    print("After Scenario", scenario)
    context.driver.close()
