
# coding: utf-8

# In[1]:

# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df


# In[2]:

get_ipython().magic('matplotlib notebook')
import matplotlib.pyplot as plt
from scipy import stats

des = df.transpose().describe()
des_mean = des.loc['mean']

x = des_mean.index
y = des_mean.values
des_sigma = des.loc['std']
sigma = des_sigma / np.sqrt(len(df.columns))
conf_int = stats.norm.interval(0.95, loc=y, scale=sigma)
conf_yerr = [y-conf_int[0],conf_int[1]-y]
conf_yerr


# In[4]:

def plot(ydata):
    barchart = plt.bar(x,y, width=0.8, yerr=conf_yerr)
    plt.title('Sample mean and 95% confidence intervals for 1992-1995')
    ax = plt.gca()
    ax.set_xticks(x)
    plt.tick_params('both', bottom=False, left=False)
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    color(ydata,barchart)
    plt.axhline(ydata, color='gray', linewidth=1)
    ax.text(barchart[-1].get_x()+0.9, ydata+1000, 'y = ' + str(int(ydata)), color = '#000000',fontsize=10, ha ='left')
    
def color(ydata,barchart):
    below = x[ydata<conf_int[0]]
    above = x[ydata>conf_int[1]]
    for bar in barchart:
        if int(bar.get_x()+0.5) in below:
            bar.set_color('#7E91B5')
        elif int(bar.get_x()+0.5) in above:
            bar.set_color('#B57E7E')
        else:
            bar.set_color('#B2B2B2')
    
def onclick(event):
    plt.cla()
    plot(event.ydata)

plt.gcf().canvas.mpl_connect('button_press_event', onclick)

plot(np.mean(y))


# In[ ]:



