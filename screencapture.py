#Python get image after searching factset
import PIL.ImageGrab
from PIL import Image
import json
import pyautogui
import time

# import cv2
# import numpy as np

goodlist = [ "ABT", "ACN", "ATVI", "ADBE", "AAP", "AES",  "A", "APD", "AKAM", "ARE",  "ALGN", "ALLE", "AEP", "AXP", "AME", "AMGN", "APH", "ADI", "ANSS", "ANSS", "AIV", "ARNC", "ANET", "AJG", "AIZ", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "BLL", "BAX", "BBY",  "BA", "BSX", "AVGO", "BR",  "CDNS"]
stocklist = ["MMM", "ABBV", "ABMD-US", "AMD", "AMG", "AFL", "ALK", "ALB", "ALXN", "AGN", "ADS", "LNT",  "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AIG", "AMT", "AWK", "AMP", "ABC", "ANSS", "APA", "AAPL", "AMT", "APTV", "ADM","T", "BHGE", "BAC", "BK", "BBT", "BDX", "BRK.B", "BIIB", "BLK", "HRB", "BKNG", "BWA", "BXP", "BMY", "BF.B", "CHRW", "COG" ]
#
pyautogui.moveTo(2500, 9)
pyautogui.click()
i = 1
for stockname in stocklist:
    pyautogui.moveTo(150,200)
    pyautogui.click()
    pyautogui.dragTo(20,200)
    pyautogui.typewrite(stockname)
    pyautogui.moveTo(55,340)
    time.sleep(2)
    pyautogui.click()
    time.sleep(3)
    img = PIL.ImageGrab.grab(bbox=(600,450, 2670, 920))
    img.save("test" + str(i) + ".jpeg")
    i = i + 1

i = 1
for stockname in stocklist:
    picture = Image.open("test"+str(i)+".jpeg")
    for x in range(2670-600):
        for y in range(920-450):
           r,g,b = picture.getpixel( (x,y) )
           if g > 100 and b < 100:
               new_color = (255,255,255)
               picture.putpixel( (x,y), new_color)
    picture.save("test" + str(i) + ".jpeg")
    i = i+1
