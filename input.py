import time
import PIL
import pyautogui as pyautogui
from PIL import Image
# from predictigcp import get_prediction
import requests
import json
import base64

userinput = input('Enter stock name:')
stocklist = []
if userinput == all:
    stocklist = []
else:
    stocklist.append(userinput)
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
    img.save("data" + str(i) + ".jpeg")
    img.save("display.jpeg")
    i = i + 1

i = 1
for stockname in stocklist:
    picture = Image.open("data"+str(i)+".jpeg")
    for x in range(2670-600):
        for y in range(920-450):
           r,g,b = picture.getpixel( (x,y) )
           if g > 100 and b < 100:
               new_color = (255,255,255)
               picture.putpixel( (x,y), new_color)
    picture.save("data" + str(i) + ".jpeg")
    i = i+1

eventualjson ={"payload": {"image": { "imageBytes": ""}}}
with open("data1.jpeg", "rb") as imageFile:
    img64 = str(base64.b64encode(imageFile.read()))

eventualjson['payload']['image']['imageBytes'] = img64[2:-1]
# posturl = "https://automl.googleapis.com/v1beta1/projects/350941884379/locations/us-central1/models/ICN6202692537958793216:predict"
# filename = rs.SaveFileName("Save JSON file as", "request.json")
# with open(filename, 'w') as f:
#     json.dump(eventualjson, f)
with open("request2.json", 'w') as f:
    json.dump(eventualjson, f)
# head = {"Authorization": "Bearer ya29.c.Kl6bB6Tlkmb-wVYAoLKXZJ4o1s191gyKuj-eTZCdcpzMLgTBJvFb1QJRMU7xkl5bu6xUx387ghXNPwTxYnETpopwbRLj_q13nu9fc8b9KuFavf6OIlVNM-5-zseNKcE-"}
# print(json.dumps(eventualjson, indent = 4))
# rpost = requests.post(posturl, headers = head,json=json.dumps(eventualjson))
# print(rpost.text)
#
# print(rpost.text)
# jsonobject = get_prediction("data1.jpeg", "350941884379", "ICN6202692537958793216")

# print(json.dumps(jsonobject, indent = 4))
