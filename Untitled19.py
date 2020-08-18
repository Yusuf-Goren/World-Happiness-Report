#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt 


# In[3]:


df = pd.read_csv("2019.csv")
df.head()


# In[4]:


plt.plot('Score','Social support',data=df,marker='o', color='mediumvioletred')


# In[5]:


data = df.drop("Country or region",axis=1)
data = df.drop("Score",axis=1)
sns.heatmap(data.corr(),annot=True,linewidth = 0.5, cmap='coolwarm')


# 2019 yılı verilerine bakarsak en mutlu ükle Finlandiya olarak görülmektedir.

# Bunu etkileyen etkenlerde ısı haritasındanda görüldüğü gibi Gayri Safi Milli Hasıla gelmektedir. Daha sonra ise Sosyal destek ve sağlıklı yaşam beklentisi gelmektedir.

# In[6]:


li = []
all_files=["2015.csv", "2016.csv", "2017.csv", "2018.csv", "2019.csv"]


# In[7]:


for filename in all_files:
    df = pd.read_csv(filename, index_col=None)
    li.append(df)


# In[8]:


frame = pd.concat(li, axis=0, sort = True)


# In[9]:


frame.head()


# In[10]:


select_tr = frame.loc[lambda frame: frame['Country'] == 'Turkey']
print (select_tr.Family)


# In[11]:


tr_2015 = pd.read_csv("2015.csv")
tr_2016 = pd.read_csv("2016.csv")
tr_2017 = pd.read_csv("2017.csv")
tr_2018 = pd.read_csv("2018.csv")
tr_2018.rename(columns={'Country or region': 'Country'}, inplace=True)
tr_2019 = pd.read_csv("2019.csv")
tr_2019.rename(columns={'Country or region': 'Country'}, inplace=True)


# In[12]:


tr_2015 = tr_2015.loc[lambda frame: frame['Country'] == 'Turkey']
print(tr_2015)
tr_2016 = tr_2016.loc[lambda frame: frame['Country'] == 'Turkey']
print(tr_2016)
tr_2017 = tr_2017.loc[lambda frame: frame['Country'] == 'Turkey']
print(tr_2017)
tr_2018 = tr_2018.loc[lambda frame: frame['Country'] == 'Turkey']
print(tr_2018)
tr_2019 = tr_2019.loc[lambda frame: frame['Country'] == 'Turkey']
print(tr_2019)
tr = [tr_2015, tr_2016, tr_2017, tr_2018, tr_2019]


# In[13]:


tr_df = {'Rank':[75, 77, 68, 73, 78],
         'Score':[5.332, 5.389, 5.5, 5.483, 5.373],
         'Generossity':[0.12253, 0.04707, 0.046693, 0.106, 0.083],
         'Freedom':[0.22815, 0.23889, 0.300741, 0.324, 0.195],
         'Healthy life expectancy':[0.73172, 0.64718, 0.637606, 0.686, 0.808],
         'Trust':[0.15746, 0.12348, 0.099672, 0.109, 0.106],
         'GDP':[1.06098, 1.16492, 1.198274, 1.148, 1.183],
         'Year':[2015,2016,2017,2018,2019]}


# In[15]:


df_tr=pd.DataFrame(tr_df)
df_tr.head()


# Yukarıda 5 yılın verileri daha derli toplu bir hale gelmiştir.
# Veriler daha dikkatli incelendiği zaman en yüksek puana 2017 yılında ulaşılmıştır. 

# 2017 senesinde GDP  yılın en yüksek seviyesinden olduğu gibi mutluluk skoruda aynı zamanda en yüksek puanındadır.

# Bu verilere bakılarak genel ile doğru orantılı olarak Gayri Milli Safi Hasılanın etkili olduğu görülmektedir.

# In[51]:


f,ax = plt.subplots(figsize = (9,5))
labels = ["Freedom","GDP","Trust","Healthy life expectancy","Generossity"]
x=df_tr["Year"]
ax.plot_date(x = x, y = df_tr["Freedom"], linestyle = '-.', color='red', label="Freedom") 
ax.plot_date(x = x, y = df_tr["GDP"], linestyle = '-.', color='black', label="GDP") 
ax.plot_date(x = x, y = df_tr["Trust"], linestyle = '-.', color ='blue', label="Trust" ) 
ax.plot_date(x = x, y = df_tr["Healthy life expectancy"], linestyle = '-.', color ='green', label="Trust" ) 
ax.plot_date(x = x, y = df_tr["Generossity"], linestyle = '-.', color ='orange', label="Trust" ) 
# show the plot
ax.legend(labels=labels)
plt.show() 


# Bu grafikte verilerin yıllara göre değişimi daha net görülmektedir.

# In[52]:


plt.plot('Year','Score',data=df_tr,marker='o', color='mediumvioletred')


# In[53]:


plt.plot('Year','GDP',data=df_tr,marker='o', color='mediumvioletred')


# In[54]:


df_tr = df_tr.drop('Year',axis=1)
df_tr = df_tr.drop('Rank',axis=1)
sns.heatmap(df_tr.corr(),annot=True,linewidth = 0.5, cmap='coolwarm')


# In[ ]:





# In[ ]:




