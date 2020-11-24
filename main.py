import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from airtable.auth import AirtableAuth
from airtable.airtable import Airtable
from twilio.rest import Client


import requests

def checkForPlayStation():
    print('navigation starts')
    try:
        time.sleep(2)
        time.sleep(2)
    except NoSuchElementException:
        return False
    return True


def alertUser():
    message = client.messages.create(
    to="+33617224683",
    from_="+18014163691",
    body="Amazon PS5 DISPOOOOOOOO !"
)


def init(count):
    if ((count % 2) < 1):
        browser.get('https://www.amazon.fr/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H98GVK8/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=27L3HGT7Q2K9U&dchild=1&keywords=play%2Bstation%2B%2B5&qid=1606176118&sprefix=play%2Bstat%2Caps%2C176&sr=8-1&th=1')
    else:
        browser.get('https://www.amazon.fr/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H93ZRK9/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=27L3HGT7Q2K9U&dchild=1&keywords=play%2Bstation%2B%2B5&qid=1606176118&sprefix=play%2Bstat%2Caps%2C176&sr=8-1&th=1')

account_sid = "ACc21106bd7655a710c2cf0cd30d266743"
auth_token  = "27c7948e235ee6af7047b442d1e1f218"
client = Client(account_sid, auth_token)
count = 1
ps5 = False
while ps5 != True:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    init(count)
    try:
        addCartButton = browser.find_element_by_xpath("//*[@id='add-to-cart-button']")
        alertUser();
        ps5 = True;
    except NoSuchElementException:
        browser.close();
        print(count)
        time.sleep(2)
    count = count + 1
