
# coding: utf-8

# In[1]:

import pandas as pd

province = {'湖北':'Hubei', '湖南':'Hunan', '广东':'Guangdong', '广西':'Guangxi', '河北':'Hebei', '河南':'Henan', 
            '山西':'Shanxi', '山东':'Shandong', '江苏':'Jiangsu', '江西':'Jiangxi', '浙江':'Zhejiang', '黑龙江':'Heilongjiang',
            '新疆':'Xinjiang', '云南':'Yunnan', '贵州':'Guizhou', '福建':'Fujian', '吉林':'Jilin', '安徽':'Anhui',
            '四川':'Sichuan', '西藏':'Tibet', '宁夏':'Ningxia', '辽宁':'Liaoning', '青海':'Qinghai', '甘肃':'Gansu',
            '陕西':'Shaanxi', '内蒙古':'Inner Mongolia', '台湾':'Taiwan', '北京':'Beijing', '上海':'Shanghai', '天津':'Tianjin',
            '海南':'Hainan', '重庆':'Chongqing'}


# In[57]:

df1 = pd.read_csv('hospital.csv')
df1 = df1.drop(['hospital','hospital_id','city', 'char', 'telephone', 'longitude', 'latitude', 'route', 'address'], axis = 1)
df1['count'] = 1
df1 = df1[df1['level'] == '三甲']
df1 = df1.replace(province)
df1.head()


# In[58]:

df2 = pd.read_excel('population.xls', skiprows = 3)
df2 = df2.drop([31, 32])
df2 = df2.iloc[:, :2]
for i in df2.index:
    if df2['地区'][i] == '内蒙古自治区':
        df2['地区'][i] = '内蒙古'
    elif df2['地区'][i] == '黑龙江省':
        df2['地区'][i] = '黑龙江'
    else:
        df2['地区'][i] = df2['地区'][i][:2]
df2 = df2.replace(province)
df2 = df2.rename(columns={'地区':'province', '2015年':'population'})

df2.head()


# In[255]:

hsp_sum = df1.groupby('province').agg(sum)
hsp_sum = hsp_sum.reset_index()
hsp = pd.merge(hsp_sum, df2, how='outer', on='province')
hsp['avg'] = hsp['count']/(hsp['population']/10)
hsp = hsp.sort_values(by='count', axis=0, ascending=False)
hsp = hsp.reset_index()

print(hsp['count'].sum())

hsp['str'] = hsp['province']
for i in hsp.index:
    hsp['str'][i] = str(hsp['count'][i]) + '\n' + hsp['str'][i]

hsp.head()


# In[150]:

hsp_avg = hsp['count'].mean()
def rank_avg():
    for i in range(0, len(hsp.index)-1):
        if hsp.loc[i, 'count'] > hsp_avg > hsp.loc[i+1, 'count']:
            return i
rank_avg = rank_avg() + 0.5
print(rank_avg)


# In[272]:

get_ipython().magic('matplotlib notebook')

import numpy as np
import matplotlib.pyplot as plt

N = 31

r = np.array(hsp['avg'])


theta = np.linspace(0, N, N, endpoint=False)


area = np.array(hsp['count'])**3/1200

colors = theta

plt.figure(figsize=(25,5))
plt.title('Top hospital distribution in China', alpha=0.8, fontsize = 20)
plt.xlabel('Rank of hospital number of different provinces (-- average line)', alpha=0.8)
plt.ylabel('Top hospital number per million people\n(-- average line)', alpha=0.8)


plt.axhline(y=round(hsp['avg'].mean(), 2), color='black', linestyle='--', alpha=0.8)

plt.axvline(x=rank_avg, color='black', linestyle='--', alpha=0.8)

pic = plt.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.8)

plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='on', labelbottom='on')
plt.xticks(theta, np.array(hsp['str']), rotation=72, alpha=0.8) 

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_yticklabels(['0', '', '', '', '', '', '', '', '0.40'], alpha=0.8)
ax.set_yticklabels([round(hsp['avg'].mean(), 2)], minor=True)
ax.set_yticks([round(hsp['avg'].mean(), 2)], minor=True)



plt.subplots_adjust(bottom=0.35)

plt.show()

