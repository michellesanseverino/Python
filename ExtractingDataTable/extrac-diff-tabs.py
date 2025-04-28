from selenium import webdriver as settingsSelenium
from selenium.webdriver.common.by import By

import pyautogui as timeWaiting

import pandas as pd

browser = settingsSelenium.Chrome()

browser.get("https://rpachallengeocr.azurewebsites.net/")

dataFrameList = []

line = 1
i = 1

while i < 4:
    elementTable = browser.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    lines = browser.find_elements(By.TAG_NAME, "tr")
    columns = browser.find_elements(By.TAG_NAME, "td")

    for currentLine in lines:
        print(currentLine.text)
        dataFrameList.append(currentLine.text)
        line += 1

    timeWaiting.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    timeWaiting.sleep(2)
    
    i += 1
    
else:
    print("End of extraction!")
    
fileExcel = pd.ExcelWriter('SiteExtraction.xlsx', engine='xlsxwriter')
fileExcel._save()

dataFrame = pd.DataFrame(dataFrameList, columns=['#;ID;Due Date;Invoice'])
fileExcel = pd.ExcelWriter('SiteExtraction.xlsx', engine='xlsxwriter')

dataFrame.to_excel(fileExcel, sheet_name='Sheet', index=False)

fileExcel._save()