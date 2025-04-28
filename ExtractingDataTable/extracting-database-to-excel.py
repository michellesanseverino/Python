from selenium import webdriver as settingsSelenium
from selenium.webdriver.common.by import By

import pandas as pd

browser = settingsSelenium.Chrome()

browser.get("https://rpachallengeocr.azurewebsites.net/")

elementTable = browser.find_element(By.XPATH, '//*[@id="tableSandbox"]')

lines = elementTable.find_elements(By.TAG_NAME, "tr")
columns = elementTable.find_elements(By.TAG_NAME, "td")

dataFrameList = []

line = 1

for i in lines:
    print(i.text)
    dataFrameList.append(i.text)
    line += 1

fileExcel = pd.ExcelWriter('SiteData.xlsx', engine='xlsxwriter')
fileExcel._save()

dataFrame = pd.DataFrame(dataFrameList, columns=['Column_Data'])

fileExcel = pd.ExcelWriter('SiteData.xlsx', engine='xlsxwriter')

dataFrame.to_excel(fileExcel, sheet_name='Sheet1',index=True)

fileExcel._save()