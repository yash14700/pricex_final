from art import *
import wand
import time
import json
from PIL import Image


with open('final.json') as json_file:
    data = json.load(json_file)
    tprint(str(data["payload"][0]["displayName"]))
    acc = data["payload"][0]["classification"]["score"]
    print("Likely accuracy: " + str(acc))

time.sleep(3)
image = Image.open('display.jpeg')
image.show()
