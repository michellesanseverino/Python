import pyautogui as positionMouse
import pyautogui as timeWaiting

timeWaiting.sleep(5)
positionMouse.moveTo(1028,1041)
positionMouse.click(1028,1041)

timeWaiting.sleep(2)
positionMouse.typewrite('dollar currency today')
positionMouse.press('enter')