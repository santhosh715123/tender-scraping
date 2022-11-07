#!/usr/bin/env python
# coding: utf-8

# In[6]:


#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import plotly.express as px
import time
import os
import wget
import pandas as pd
from bs4 import BeautifulSoup
chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_experimental_option("prefs",prefs)
wd=webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
wd.get("https://opentender.eu/start")
time.sleep(5)
class Scrapper:
    tenders = []
    tender = wd.find_elements_by_xpath("//li[@class='portal-link']")
    for t in tender:
        tenders.append(t.text)
    list2 = [x.replace('\n', ' - ') for x in tenders]
    dataset1 = pd.DataFrame(list2,columns=['NUMBER OF TENDERS'])
    dataset1.to_csv("C:/Users/Santhosh Kumar/OneDrive/Desktop/digit_recog/tenders4.csv",sep=',', index=False)
Sc = Scrapper()

