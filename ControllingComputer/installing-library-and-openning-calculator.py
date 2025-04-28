import pyautogui as positionMouse
import pyautogui as timeWaiting

#To find the position in a easy way, we can run this code: print(positionMouse.position())

# Making the program move thecalculator mouse to the Windows Button
positionMouse.moveTo(684, 1068)

# Time to click and open Windows
timeWaiting.sleep(2)
positionMouse.click(684,1068)

#Searching calculator
timeWaiting.sleep(2)
positionMouse.click(655,164)
positionMouse.typewrite('calculator')

# Opening Calculator
timeWaiting.sleep(5)
positionMouse.click(675,363)
