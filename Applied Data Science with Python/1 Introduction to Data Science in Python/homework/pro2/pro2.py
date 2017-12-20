import pandas as pd
import numpy as np

def get_energy():
    energy = pd.read_excel('Energy Indicators.xls')
    energy = energy.iloc[16:243, 2:]
    energy.rename(columns={'Environmental Indicators: Energy':'Country', 'Unnamed: 3':'Energy Supply', 'Unnamed: 4':'Energy Supply per Capita', 'Unnamed: 5':'% Renewable'}, inplace=True)

    for i in energy.index:
        try:
            energy.loc[i, 'Energy Supply'] = int(energy.loc[i, 'Energy Supply']) * 1000000
        except:
            energy.loc[i, 'Energy Supply'] = np.nan
            energy.loc[i, 'Energy Supply per Capita'] = np.nan

    for i in energy.index:
        while energy.loc[i, 'Country'][-1:].isnumeric():
            energy.loc[i, 'Country'] = energy.loc[i, 'Country'][:-1]
        try:
            energy.loc[i, 'Country'] = energy.loc[i, 'Country'].split(' (')[0]
        except:
            pass

    energy.loc[energy['Country'] == 'United States of America', 'Country'] = 'United States'
    energy.loc[energy['Country'] == 'United Kingdom of Great Britain and Northern Ireland', 'Country'] = 'United Kingdom'
    energy.loc[energy['Country'] == 'Republic of Korea', 'Country'] = 'South Korea'
    energy.loc[energy['Country'] == 'China, Hong Kong Special Administrative Region', 'Country'] = 'Hong Kong'
    return energy

def get_GDP():
    GDP = pd.read_csv('world_bank.csv')
    GDP.rename(columns = GDP.iloc[3], inplace = True)
    GDP = GDP.iloc[4:, :]

    GDP.loc[GDP['Country Name'] == 'Korea, Rep.', 'Country Name'] = 'South Korea'
    GDP.loc[GDP['Country Name'] == 'Iran, Islamic Rep.', 'Country Name'] = 'Iran'
    GDP.loc[GDP['Country Name'] == 'Hong Kong SAR, China', 'Country Name'] = 'Hong Kong'

    GDP.rename(columns = {'Country Name':'Country'}, inplace = True)
    GDP = GDP.set_index(['Country'])
    GDP = GDP.iloc[:, -10:]
    GDP = GDP.reset_index()
    return GDP

def get_ScimEn():
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    return ScimEn

def answer_one():
    energy = get_energy()
    GDP = get_GDP()
    ScimEn = get_ScimEn()

    dataset0 = pd.merge(ScimEn, energy, how='outer', on='Country')
    dataset0 = pd.merge(dataset0, GDP, how='outer', on='Country')
    dataset = dataset0.iloc[:15]
    dataset = dataset.set_index(['Country'])
    dataset = dataset.rename(columns={2006.0: '2006', 2007.0: '2007', 2008.0: '2008', 2009.0: '2009', 2010.0: '2010', 2011.0: '2011', 2012.0: '2012', 2013.0: '2013', 2014.0: '2014', 2015.0: '2015'})
    return dataset

answer_one()


def answer_two():
    energy = get_energy()
    GDP = get_GDP()
    ScimEn = get_ScimEn()

    dataset0 = pd.merge(ScimEn, energy, how='outer', on='Country')
    dataset0 = pd.merge(dataset0, GDP, how='outer', on='Country')
    x = len(dataset0.index) - 15
    return x

answer_two()


def answer_three():
    top15 = answer_one().iloc[:, -10:]
    avgGDP = top15.mean(axis = 1)
    avgGDP.sort(ascending = False)
    return avgGDP

answer_three()


def answer_four():
    top15 = answer_one().iloc[:, -10:]
    country6 = answer_three().index[5]
    span = top15['2015'] - top15['2006']
    return span[country6]

answer_four()


def answer_five():
    m = answer_one()['Energy Supply per Capita'].mean()
    return float(m)

answer_five()


def answer_six():
    re_list = answer_one().sort_values(by = '% Renewable', ascending = False)
    return (re_list.index[0], re_list.iloc[0, 9])

answer_six()


def answer_seven():
    ratio_list = answer_one()
    ratio_list['ratio'] = 0
    for i in ratio_list.index:
        ratio_list.loc[i, 'ratio'] = int(ratio_list.loc[i, 'Self-citations'])/int(ratio_list.loc[i, 'Citations'])
    ratio_list.sort_values(by='ratio', ascending = False)
    return (ratio_list.index[0], ratio_list.loc[ratio_list.index[0], 'ratio'])

answer_seven()


def answer_eight():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    pptop = Top15.sort('PopEst')
    return pptop.index[-3]

answer_eight()


def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.iloc[:, -1] = Top15.iloc[:, -1].astype('float64')
    Top15.loc[:, 'Energy Supply per Capita'] = Top15.loc[:, 'Energy Supply per Capita'].astype('float64')
    return Top15.loc[:, 'Energy Supply per Capita'].corr(Top15.iloc[:, -1])

answer_nine()


def answer_ten():
    import numpy as np
    Top15 = answer_one()
    Top15['HighRenew'] = np.nan
    Top15 = Top15.loc[:, ['% Renewable', 'HighRenew']]
    m = Top15.iloc[0].median()
    Top15.loc[Top15['% Renewable'] >= m, 'HighRenew'] = 1
    Top15.loc[Top15['% Renewable'] < m, 'HighRenew'] = 0
    return Top15.sort()['HighRenew']

answer_ten()


def answer_eleven():
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['count'] = 1
    Top15 = Top15.iloc[:, -2:]
    Top15.iloc[:, -2] = Top15.iloc[:, -2].astype('float64')
    group = Top15.groupby(by = ContinentDict)
    size = group['count'].sum()
    ppsum = group['PopEst'].sum()
    ppmean = group['PopEst'].mean()
    ppstd = group['PopEst'].std()
    df = pd.DataFrame({"1":size,"2":ppsum, "3":ppmean, "4":ppstd})
    df = df.rename(columns={'1': 'size', '2': 'sum', '3': 'mean', '4': 'std'})
    df.index.names = ['Continent']
    return df

answer_eleven()


def answer_twelve():
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
    Top15 = answer_one()
    cut = pd.cut(Top15['% Renewable'], 5)

    return cut
print(answer_twelve())


def answer_thirteen():
    x = list()
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    for i in Top15['PopEst']:
        a = str(i).split('.')[0]
        b = str(i).split('.')[1]
        if len(a) == 10:
            a = a[:-9] + ',' + a[-9:-6] + ',' + a[-6:-3] + ',' +a[-3:]
        elif 7 < len(a) < 10:
            a = a[-9:-6] + ',' + a[-6:-3] + ',' +a[-3:]
        i = a + '.' + b
        x.append(i)
    Top15['PopEst'] = x
    return Top15['PopEst']

answer_thirteen()


