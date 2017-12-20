
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d25/d035233802c307b63e773fd6d0b925b4f447b38691b74f670fcb4647.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Heiwajima, Tokyo, Japan**, and the stations the data comes from are shown on the map below.

# In[2]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(25,'d035233802c307b63e773fd6d0b925b4f447b38691b74f670fcb4647')


# In[130]:

import pandas as pd

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d25/d035233802c307b63e773fd6d0b925b4f447b38691b74f670fcb4647.csv')
df = df[df['Date'] != '2008-02-29']
df = df[df['Date'] != '2012-02-29']
df = df.sort('Date')[df['Date'] < '2015-01-01']

# seperate max and min from 2005-2014, df1 as max, df0 as min
df1 = df[df['Element'] == 'TMAX']
df1 = df1.groupby('Date').agg({'Data_Value':max})
df1 = df1.reset_index()

# change 'date' to datetime and remove the year from datetime
df1['Date'] = pd.to_datetime(df1['Date'])
df1['Date'] = df1['Date'].dt.strftime('%m-%d')
df1 = df1.groupby('Date').agg({'Data_Value':max})

# modify the columns name in the end
df1 = df1.rename(columns={'Data_Value':'TMAX'})
df1['TMAX'] = df1['TMAX'] / 10.0

# do the same to df0
df0 = df[df['Element'] == 'TMIN']
df0 = df0.groupby('Date').agg({'Data_Value':min})
df0 = df0.reset_index()
df0['Date'] = pd.to_datetime(df0['Date'])
df0['Date'] = df0['Date'].dt.strftime('%m-%d')
df0 = df0.groupby('Date').agg({'Data_Value':min})
df0 = df0.rename(columns={'Data_Value':'TMIN'})
df0['TMIN'] = df0['TMIN'] / 10.0

df2 = pd.merge(df1, df0, how='inner', left_index=True, right_index=True)
df2 = df2.reset_index()


# In[135]:

df15 = pd.read_csv('data/C2A2_data/BinnedCsvs_d25/d035233802c307b63e773fd6d0b925b4f447b38691b74f670fcb4647.csv')
df15 = df15[df15['Date'] >= '2015-01-01'].sort('Date')

df151 = df15[df15['Element'] == 'TMAX']
df151 = df151.groupby('Date').agg({'Data_Value':max})
df151['Data_Value'] = df151['Data_Value'] / 10.0
df151 = df151.reset_index()
df151['Date'] = pd.to_datetime(df151['Date'])
df151['Date'] = df151['Date'].dt.strftime('%m-%d')
df151 = df151.rename(columns={'Data_Value':'2015TMAX'})

df150 = df15[df15['Element'] == 'TMIN']
df150 = df150.groupby('Date').agg({'Data_Value':min})
df150['Data_Value'] = df150['Data_Value'] / 10.0
df150 = df150.reset_index()
df150['Date'] = pd.to_datetime(df150['Date'])
df150['Date'] = df150['Date'].dt.strftime('%m-%d')
df150 = df150.rename(columns={'Data_Value':'2015TMIN'})

# compare temperature in 2015 to 2005-2014
df1 = df1.reset_index()
cp1 = pd.merge(df151, df1, how='inner',left_on='Date',right_on='Date')
cp11 = cp1[cp1['2015TMAX'] > cp1['TMAX']]

df0 = df0.reset_index()
cp0 = pd.merge(df150, df0, how='inner',left_on='Date',right_on='Date')
cp00 = cp0[cp0['2015TMIN'] < cp0['TMIN']]


# In[169]:

get_ipython().magic('matplotlib notebook')

import matplotlib as mpl
import matplotlib.pyplot as plt

plt.figure(figsize=(16, 10))
plt.scatter(cp11.index, cp11['2015TMAX'], s=5, c='red', alpha=1)
plt.scatter(cp00.index, cp00['2015TMIN'], s=5, c='black', alpha=1)
plt.plot(df2['TMIN'], '-', df2['TMAX'], '-', alpha=0.5)
plt.gca().fill_between(range(365), df2['TMIN'], df2['TMAX'], facecolor='grey', alpha=0.1)
plt.legend(['MIN Temperature','MAX Temerature', 'Break points in 2015(MAX)', 'Break points in 2015(MIN)'], loc=(4), frameon=False)

month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
days = [1,32,60,91,121,152,182,213,244,274,305,335]
plt.xticks(days, month, alpha=1)

plt.title('MIN and MAX temperature from 2005 to 2014 with break points in 2015 near Heiwajima, Tokyo, Japan')


# In[ ]:



