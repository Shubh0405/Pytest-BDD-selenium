from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# @given(u'Open Chrome Browser')
# def OpenBrowser(context):
#     driver_location = "/snap/bin/chromium.chromedriver"
#     binary_location = "/usr/bin/chromium-browser"

#     options=webdriver.ChromeOptions()
#     options.binary_location=binary_location

#     caps=DesiredCapabilities().CHROME
#     caps["pageLoadStrategy"] = "eager"

#     context.driver = webdriver.Chrome(desired_capabilities=caps,executable_path=driver_location, options=options)
#     context.driver.maximize_window()


# @when(u'Flipkart Home Page is Displayed')
# def OpenFlipkart(context):
#     context.driver.get("https://www.flipkart.com")
#     time.sleep(5)


@then(u'Verify Top Categories is present')
def VerifyTopCategories(context):
    top_categories_text = context.driver.find_element(By.CLASS_NAME, "_37M3Pb").find_elements(By.XPATH,"//div/a/div[2]")
    assert len(top_categories_text) > 0