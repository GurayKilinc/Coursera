def answer_one():
    df.sort(columns = 'Gold', ascending = False, inplace = True)
    return df.iloc[0].name
answer_one()

def answer_two():
    summer_g = df['Gold']
    winter_g = df['Gold.1']
    dif = summer_g - winter_g
    dif.sort(ascending = False)
    if dif[0] + dif[-1] > 0:
        return dif.head(1).index[0]
    else:
        return dif.tail(1).index[0]
answer_two()

def answer_three():
    gold = df[df['Gold']>0][df['Gold.1']>0]
    dif = (gold['Gold'] - gold['Gold.1'])/gold['Gold.2']
    dif.sort(ascending = False)
    if dif[0] + dif[-1] > 0:
        return dif.head(1).index[0]
    else:
        return dif.tail(1).index[0]
answer_three()

def answer_four():
    metal = df.loc[:, ['Gold.2', 'Silver.2', 'Bronze.2']]
    metal['Gold.2'] = metal['Gold.2'] * 3
    metal['Silver.2'] = metal['Silver.2'] * 2
    metal['Bronze.2'] = metal['Bronze.2'] * 1
    metal['total'] = metal['Gold.2'] + metal['Silver.2'] + metal['Bronze.2']
    Points = metal.loc[:, ['total']]
    return Points
answer_four()

import pandas as pd
def answer_five():
    census_df = pd.read_csv('census.csv')
    count = census_df.where(census_df['SUMLEV'] == 40)
    count = count.dropna().loc[:, ['SUMLEV', 'STNAME']]
    num = list()
    for i in range(len(count.index)):
        num.append(count.index[i])
    num.append(census_df.index[-1])
    num2 = list()
    for i in range(len(num)-1):
        num2.append(num[i+1] - num[i])
    count['NUM'] = 0
    count.index = range(len(num2))
    for i in range(len(num2)):
        count['NUM'][i] = num2[i]
    count = count.set_index('NUM')
    count = count.sort()
    count.index = range(len(num2))
    return count['STNAME'][len(num2)-1]
answer_five()

import pandas as pd
def answer_six():
    census = pd.read_csv('census.csv')
    count = census.loc[:, ['SUMLEV', 'STATE', 'STNAME', 'CENSUS2010POP']]
    count1 = count.where(count['SUMLEV'] == 50).dropna()
    count1['SORT'] = count1['CENSUS2010POP'].groupby(count1['STATE']).rank()

    count2 = count1.where(count1['SORT'] < 4).dropna()
    count_sum = count2['CENSUS2010POP'].groupby(count2['STATE']).sum()
    count_rank3 = count_sum.nlargest(3)

    state = count.where(count['SUMLEV'] == 40).dropna()
    rank3 = list()
    state = state.set_index('STATE')
    for i in count_rank3.index:
        global rank3
        rank3.append(state.loc[i,'STNAME'])
    return rank3
answer_six()

import pandas as pd
def answer_seven():
    census = pd.read_csv('census.csv')
    census = census.where(census['SUMLEV'] == 50).dropna()
    county = census.loc[:, ['CTYNAME', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']]
    county['DIF'] = 0
    for i in county.index:
        cNum = county.loc[i, ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']]
        cDif = cNum.max() - cNum.min()
        county.loc[i, ['DIF']] = cDif
    county = county.sort(columns = 'DIF', ascending=False)
    county = county.set_index([county.index, 'DIF'])
    return county.iloc[0:1,0:1].values[0][0]
answer_seven()

import pandas as pd
def answer_eight():
    census = pd.read_csv('census.csv')
    county = census.where(census['SUMLEV'] == 50).dropna()
    county = county.loc[:, ['STNAME', 'CTYNAME', 'REGION', 'POPESTIMATE2014', 'POPESTIMATE2015']]
    county = county.where((county['REGION'] == 1) | (county['REGION'] == 2)).dropna()
    county = county.where(county['POPESTIMATE2015'] > county['POPESTIMATE2014']).dropna()
    county = county.loc[:, ['STNAME', 'CTYNAME']]

    for i in county.index:
        if county.loc[i]['CTYNAME'][:10] == 'Washington':
            pass
        else:
            county = county.drop(i)

    return county
answer_eight()