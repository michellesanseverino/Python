from selenium import webdriver as settingsSelenium
from selenium.webdriver.common.by import By

browser = settingsSelenium.Chrome()

browser.get("https://rpachallengeocr.azurewebsites.net/")

elementTable = browser.find_element(By.XPATH, '//*[@id="tableSandbox"]')

lines = elementTable.find_elements(By.TAG_NAME, "tr")
columns = elementTable.find_elements(By.TAG_NAME, "td")

line = 1

for i in lines:
    print(i.text)
    line += 1