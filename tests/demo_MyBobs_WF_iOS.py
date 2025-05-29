from appium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.safari.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os
from selenium.webdriver.support.wait import WebDriverWait

# Get BrowserStack credentials
BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

# BrowserStack URL
URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# Create options and set capabilities
options = Options()
options.set_capability("browserName", "safari")
options.set_capability("bstack:options", {
    "deviceName": "iPhone 15",
    "osVersion": "16",
    "interactiveDebugging": True,
    "disableCorsRestrictions": True
})

# Initialize Appium driver using updated syntax
driver = webdriver.Remote(command_executor=URL, options=options)
driver.implicitly_wait(60)
wait = WebDriverWait(driver, 60)

try:
    driver.get("https://bobsaccess:t_uhor2c3ave@s3.bdfhybris.com/")
    time.sleep(5)

    userEmail = 'parthasarathi.kesana@isoftstone.com'
    userPassword = 'Test@1234'

    # Switch to native context to allow location permission
    driver.switch_to.context("NATIVE_APP")
    driver.find_element(By.ID, "Allow").click()
    time.sleep(5)

    # Print contexts and switch back to web
    contexts = driver.contexts
    for context in contexts:
        print("Available context:", context)
        if "CHROMIUM" in context or "WEBVIEW" in context:
            driver.switch_to.context(context)
            break

    # Login as Registered User
    driver.find_element(By.XPATH, "//div[@aria-label='My Account']//*[name()='svg']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='Email Address*']").send_keys(userEmail)
    driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign in with Password']").click()
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(userPassword)
    driver.find_element(By.XPATH, "//button[@class='sofa-button-pill-md sofa-btn-red sofa-btn-stretch']").click()
    time.sleep(5)

    # Search for a Product
    driver.find_element(By.XPATH, "//input[@class='bobs-header-search-box__input ng-untouched ng-pristine ng-valid']").send_keys("Stevie Charcoal 65'' Loveseat")
    # driver.find_element(By.XPATH,
    #                     "//input[@class='bobs-header-search-box__input ng-valid ng-dirty ng-touched']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//div[@aria-label='Search']//*[name()='svg']").click()
    time.sleep(5)

    # for reference : Close button (XPATH //button[@id='button3'])
    driver.find_element(By.XPATH, "//div[@class='product-name ng-star-inserted']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//bobs-add-to-cart[@class='bobs-add-to-cart__component']//button[@type='submit'][normalize-space()='Add to Cart']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/bobs-app-root/bobs-drawer/div/div[2]/bobs-mini-cart-hybris/div/div/bobs-mini-cart-header-hybris/div/bobs-drawer-header/header/div/div[4]/a/bobs-button/button/span[1]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[@class='bobs-button bobs-button--cart-action bobs-button--default']").click()
    time.sleep(5)

    # Checkout - Delivery step
    # driver.find_element(By.XPATH, "//input[@formcontrolname='email']").clear()
    # driver.find_element(By.XPATH, "//input[@formcontrolname='email']").send_keys(userEmail)
    # driver.find_element(By.XPATH, "//input[@type='tel']").clear()
    # driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("8604567890")
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[normalize-space()='Order Summary']").click()
    time.sleep(2)

    # button_ContinueToPayment = driver.find_element(By.XPATH, "/html/body/bobs-app-root/cx-storefront/main/cx-page-layout/cx-page-slot[1]/bobs-checkout-delivery/div/bobs-checkout-delivery-form/bobs-checkout-shipping-form/form/div/div[7]/button")
    driver.find_element(By.XPATH,
                        "//button[normalize-space()='Continue to payment']").click()
    time.sleep(15)

    driver.find_element(By.XPATH, "//span[@class='payment-type-text' and contains(text(),'Financing')]").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Use existing credit']").click()

    time.sleep(5)
    driver.find_element(By.XPATH,
                        "//button[normalize-space()='Review order']").click()  # //button[@class='btn btn-block btn-primary bobs-review-order-button']
    time.sleep(10)

    driver.find_element(By.XPATH, "//input[@class='scaled-input form-check-input ng-untouched ng-pristine ng-valid']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(15)

    val_OrderID = driver.find_element(By.XPATH, "//div[@class='bobs-order-id']").get_attribute("innerText")
    print(val_OrderID)


finally:
    driver.quit()