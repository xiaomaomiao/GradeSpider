from selenium import webdriver
from PIL import Image
import os
import sys
def disposeImage():

    img=Image.open(sys.path[1]+"/educationSystem/verifyImage/verifyResource.png")

    region=(170,205,249,249)

    newimg=img.crop(region)
    newimg.save(sys.path[1]+"/educationSystem/verifyImage/verifyCode.jpg")
