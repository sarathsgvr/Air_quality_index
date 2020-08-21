from plot_aqi import avg_data
import requests
import sys
import os
import pandas as pd
from bs4 import BeautifulSoup as bs

def met_data(month, year):
    file_html= open("Air_quality_index/Data/html_data/{}/{}.html".format(year,month), 'rb')
    plain_text = file_html.read()
    tempdata = []
    finaldata = []
    soup = bs(plain_text, 'lxml')
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a= tr.get_text()
                tempdata.append(a)
    rows = len(tempdata)/15

    for i in range(round(rows)):
        print(i)

met_data(1,2013)

    
    


    

    
    