from plot_aqi import avg_data
import requests
import sys
import os
import csv
import pandas as pd
from bs4 import BeautifulSoup as bs

def met_data(month, year):
    file_html= open("Air_quality_index/Data/Html_Data/{}/{}.html".format(year,month), 'rb')
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
        newtemp = []
        for j in range(15):
            newtemp.append(tempdata[0])
            tempdata.pop(0)
        finaldata.append(newtemp)
    
    length = len(finaldata)

    finaldata.pop(length - 1)
    finaldata.pop(0)

    finaldata.pop(0)
    finaldata.pop(6)
    finaldata.pop(10)
    finaldata.pop(11)
    finaldata.pop(12)
    finaldata.pop(13)

def data_combine(year, cs):
    for a in pd.read_csv('Air_quality_index/Data/finaldata/' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist
            
if __name__ == "__main__":
    if not os.path.exists("Air_quality_index/Data/finaldata/"):
        os.makedirs("Air_quality_index/Data/finaldata/")
    for year in range(2013,2020):
        actual_data = []
        with open("Air_quality_index/Data/finaldata/{}".format(str(year))+".csv", 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in range(1,13):
            temp = met_data(month, year)
            actual_data = actual_data + temp

        pm = getattr(sys.modules[__name__], 'avg_data'(year))

        for i in range(len(actual_data) - 1):
            actual_data[i].insert(8, pm[i])
        
        with open('Air_quality_index/Data/finaldata/' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
    data_2017 = data_combine(2017, 600)
    data_2018 = data_combine(2018, 600)


    total=data_2013+data_2014+data_2015+data_2016+data_2017+data_2018

    with open('Air_quality_index/Data/finaldata/Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
df=pd.read_csv('Air_quality_index/Data/finaldata/Combine.csv')
                

    
    


    

    
    