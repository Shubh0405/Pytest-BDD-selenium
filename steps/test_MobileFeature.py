from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select


@then(u'Click Mobile Category')
def ClickMobileCategory(context):
    
    mobile_category = context.driver.find_element(By.CLASS_NAME, "_37M3Pb").find_element(By.XPATH, "//div[2]/a/div[2][text()='Mobiles & Tablets']")
    assert mobile_category.is_displayed()
    context.driver.execute_script("arguments[0].click();", mobile_category)
    time.sleep(5)


@then(u'Click First phone')
def ClickFirstPhone(context):
    
    first_phone = context.driver.find_element(By.CLASS_NAME, "_6t1WkM").find_element(By.XPATH, "//div[4]/div/div[1]/a")
    # print(first_phone.find_element(By.XPATH,"//a/div/img[2]").get_attribute("alt"))
    assert first_phone.is_displayed()
    context.driver.execute_script("arguments[0].click();",first_phone)
    time.sleep(10)

@then(u'Verify Filter text on left navbar')
def VerifyFilterText(context):
    
    filter_element = context.driver.find_element(By.XPATH,"//section/div/div/span")
    print(filter_element.text)
    assert filter_element.text == "Filters"


@then(u'Set price filter to 20000')
def SetPrice(context):
    
    price_field = Select(context.driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[3]/select"))
    price_field.select_by_visible_text("₹20000")
    time.sleep(5)