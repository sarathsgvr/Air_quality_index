import pandas as pd
import matplotlib.pyplot as plt
import os

def avg_data(year):
    temp_i = 0
    average=[]
    for rows in pd.read_csv('Air_quality_index/Data/AQI/aqi{}.csv'.format(year),chunksize=24):
        add_hour=0
        avg=0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_hour=add_hour+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp = float(i)
                    add_hour = add_hour+temp
            
        avg = add_hour/24
        temp_i = temp_i+1
        average.append(avg)
    return average

if __name__=='__main__':
    lst_2013 = avg_data(2013)
    lst_2014 = avg_data(2014)
    lst_2015 = avg_data(2015)
    lst_2016 = avg_data(2016)
    lst_2017 = avg_data(2017)
    lst_2018 = avg_data(2018)
    #print(lst_2013)
    plt.plot(range(0,365),lst_2013,label="2013 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()



