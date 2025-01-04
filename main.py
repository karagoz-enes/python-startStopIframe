from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import os

driver = None

def openWebPage(url, isMaximized=False, isIncognito=False):
    global driver

    options = Options()
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    if isMaximized:
        options.add_argument("--start-maximized")

    if isIncognito:
        options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    print(f"Chrome has been started. isMaximized: {isMaximized}, isIncognito: {isIncognito}")

def closeWebPage():
    global driver
    if driver:
        driver.quit()
        print("Chrome has been closed.")

def startIframe(xpath):
    """
    Starts iframe.
    Args:
        xpath: string -> the xpath of the iframe (ex://*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/nav/a[2]/div[1]/span)
    """ 
    global driver
    iframe_element = driver.find_element(By.XPATH, xpath)
    driver.switch_to.frame(iframe_element)
    print(f"Switched to iframe {xpath}")

def stopIframe():
    """
    Stops the iframe.
    """ 
    global driver
    driver.switch_to.default_content()
    print("Switched back to default content")

pageURL = "your webpage url"
openWebPage(pageURL)
time.sleep(5)
iframeXpath = "xpath of your iframe"
startIframe()

### your process here ###

stopIframe()
closeWebPage()




