import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

def get_list_of_university_towns():
    file = open("university_towns.txt").readlines()
    stname = list()
    state = list()
    region = list()
    for item in file:
        if '[edit]' in item:
            stname.append(item.split('[', 1)[0])
        else:
            region.append(item.split('\n')[0].split(' (', 1)[0])
            state.append(stname[-1])
    df = pd.DataFrame({'State': state, 'RegionName': region}, columns=['State', 'RegionName'])
    return df

def get_recession_start():
    gdp = pd.read_excel('gdplev.xls')
    gdp = gdp.iloc[-66:, -4:-2]
    r = list()
    for i in range(len(gdp.index)-1):
        if gdp.iloc[i-1, -1] > gdp.iloc[i, -1] > gdp.iloc[i+1, -1]:
            r.append(gdp.iloc[i-1, 0])
    return r[0]

def get_recession_end():
    gdp = pd.read_excel('gdplev.xls')
    gdp = gdp.iloc[-66:, -4:-2]
    r = list()
    rr = list()
    for i in range(len(gdp.index)-1):
        if gdp.iloc[i-1, -1] < gdp.iloc[i, -1] < gdp.iloc[i+1, -1]:
            r.append(gdp.iloc[i+1, 0])
    for item in r:
        if item > get_recession_start():
            rr.append(item)
    return rr[0]

def get_recession_bottom():
    gdp = pd.read_excel('gdplev.xls')
    gdp = gdp.iloc[-66:, -4:-2]
    n = list()
    bottom = list()
    for i in range(len(gdp.index)):
        if gdp.iloc[i, 0] == '2008q3':
            n.append(i)
        if gdp.iloc[i, 0] == '2009q4':
            n.append(i)
    gdp = gdp.iloc[n[0]:n[1], :]
    for i in range(len(gdp.index)):
        if gdp.iloc[i, -1] == min(gdp.iloc[:, -1]):
            bottom.append(gdp.iloc[i, 0])
    return bottom[0]

def convert_housing_data_to_quarters():
    home = pd.read_csv('City_Zhvi_AllHomes.csv')
    home = home.drop(['RegionID', 'Metro', 'CountyName', 'SizeRank'],axis=1)
    h1 = home.iloc[:, :2]
    h2 = home.iloc[:, 47:]
    h3 = pd.DataFrame()
    for i in range(10):
        h3.loc[:, '200'+str(i)+'q1'] = h2.iloc[:, (i*12):(i*12+3)].mean(axis=1, skipna=True)
        h3.loc[:, '200'+str(i)+'q2'] = h2.iloc[:, (i*12+3):(i*12+6)].mean(axis=1, skipna=True)
        h3.loc[:, '200'+str(i)+'q3'] = h2.iloc[:, (i*12+6):(i*12+9)].mean(axis=1, skipna=True)
        h3.loc[:, '200'+str(i)+'q4'] = h2.iloc[:, (i*12+9):(i*12+12)].mean(axis=1, skipna=True)
    for i in range(10, 17):
        h3.loc[:, '20'+str(i)+'q1'] = h2.iloc[:, (i*12):(i*12+3)].mean(axis=1, skipna=True)
        h3.loc[:, '20'+str(i)+'q2'] = h2.iloc[:, (i*12+3):(i*12+6)].mean(axis=1, skipna=True)
        h3.loc[:, '20'+str(i)+'q3'] = h2.iloc[:, (i*12+6):(i*12+9)].mean(axis=1, skipna=True)
        h3.loc[:, '20'+str(i)+'q4'] = h2.iloc[:, (i*12+9):(i*12+12)].mean(axis=1, skipna=True)
    h3 = h3.iloc[:, :-1]
    home2 = pd.concat([h1, h3], axis=1)
    home2['State'] = home2['State'].replace(states)
    home2 = home2.set_index(['State', 'RegionName'])
    return home2

def run_ttest():
    hdf = convert_housing_data_to_quarters().loc[:, ['2008q2', '2009q2']]
    hdf.loc[:, 'ratio'] = hdf.loc[:, '2008q2'].div(hdf.loc[:, '2009q2'])
    hdf = hdf.reset_index()
    uni = get_list_of_university_towns()
    uni['uniTown'] = 'True'


    UT = pd.merge(hdf, uni, how='inner')
    NUT = pd.merge(hdf, uni, how='left')
    NUT = NUT[NUT['uniTown'] != 'True']
    NUT['uniTown'] = 'False'

    t, p = ttest_ind(UT['ratio'], NUT['ratio'], nan_policy='omit')

    if p < 0.01:
        result = (True, p, "non-university town")
        return result


