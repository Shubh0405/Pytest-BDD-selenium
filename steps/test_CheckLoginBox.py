from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@given(u'launch chrome browser')
def LaunchBrowser(context):
    driver_location = "/snap/bin/chromium.chromedriver"
    binary_location = "/usr/bin/chromium-browser"

    options=webdriver.ChromeOptions()
    options.binary_location=binary_location

    caps=DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"

    context.driver = webdriver.Chrome(desired_capabilities=caps,executable_path=driver_location, options=options)
    context.driver.maximize_window()


@when(u'Flipkart home page opens')
def OpenFlipkart(context):
    context.driver.get("https://www.flipkart.com")
    time.sleep(5)


@then(u'Verify Login Text is Present')
def VerifyLoginText(context):
    login_text_element = context.driver.find_element(By.CLASS_NAME, "_36KMOx").find_element(By.TAG_NAME, "span").is_displayed()
    assert login_text_element



@then(u'Verify Username field is Present')
def VerifyUsernameField(context):
    username_field = context.driver.find_element(By.XPATH, "//span[text()='Enter Email/Mobile number']").is_displayed()
    assert username_field


@then(u'Verify Password field is Present')
def VerifyPasswordField(context):
    password_field = context.driver.find_element(By.XPATH, "//span[text()='Enter Password']").is_displayed()
    assert password_field


@then(u'Close Browser')
def CloseBrowser(context):
    context.driver.quit()
