#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import seaborn as sns
df = pd.read_csv(r'C:\Users\USER\Downloads\data\projectdata.csv')


# In[52]:


df.head(50)


# In[53]:


df.dtypes


# In[54]:


#cleaning up data 


# In[55]:


# step 1 show mi, k


# In[56]:


df[df['Event distance/length'] == '50km']


# In[57]:


df[df['Event distance/length'].isin(['50km', '50mi'])]


# In[58]:


df[(df['Event distance/length'].isin(['50km', '50mi']))  & (df['Year of event']  == 2018) ]


# In[59]:


df[df['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)


# In[60]:


df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA']


# In[61]:


#combine all the filters 


# In[62]:


df[(df['Event distance/length'].isin(['50km', '50mi']))  & (df['Year of event']  == 2018)  & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]


# In[63]:


df2 = df[(df['Event distance/length'].isin(['50km', '50mi']))  & (df['Year of event']  == 2018)  & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]


# In[64]:


df2.head(10)


# In[65]:


#remove USA from event name 


# In[66]:


df2['Event name'] = df2['Event name'].str.split('(').str.get(0)


# In[67]:


df2.head(10)


# In[68]:


df2['Year of event'] == 2020 - df2['Athlete year of birth']


# In[69]:


df2.head(10)


# In[70]:


# removing h from Athlete performance


# In[71]:


df2['Athlete performance'] = df2['Athlete performance'].str.split(' ').str.get(0)


# In[72]:


df2.head(10)


# In[73]:


#droping some colums Athlete club, Athlete country, Athlete year of birth, and Athlete age category


# In[74]:


df2 = df2.drop(['Athlete club', 'Athlete country', 'Athlete year of birth',  'Athlete age category'], axis = 1)


# In[75]:


df2.head(10)


# In[76]:


#clean up null values


# In[77]:


df2.isna().sum()


# In[78]:


#checking for dublicate values


# In[79]:


df2[df2.duplicated() == True]


# In[80]:


#reset index


# In[81]:


df2.reset_index(drop = True)


# In[82]:


df2.dtypes


# In[83]:


df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)


# In[84]:


df2.dtypes


# In[85]:


#remane columes


# In[97]:


df3 = df2.rename(columns = {'Year of event' : 'year',
    'Event dates': 'race_day',
     'Event name': 'race_name',
    'Event distance/length':'race_length' ,
    'Event number of finishers': 'race_number_of_finishers' ,
    'Athlete performance' : 'athlete_performance' ,
    'Athlete gender' : 'athlete_gender',
    'Athlete average speed': 'athlete_average_speed',
    'Athlete ID': 'athlete_id' ,
})


# In[87]:


df3.head(10)


# In[88]:


#reorder columes


# In[98]:


df3[['race_day','race_name','race_length', 'race_number_of_finishers','athlete_id', 'athlete_gender' , 'athlete_average_speed', 'athlete_performance']]


# In[90]:


#find 2 race i ran in 2018 -sarasota|Everglands 


# In[103]:


df3[df3['race_name'] == 'Everglades 50 Mile Ultra Run ']


# In[108]:


df3[df3['athlete_id'] == 222509]


# In[109]:


#charts and graphs 


# In[111]:


sns.histplot(df3['race_length'])


# In[114]:


sns.histplot(df3, x = 'race_length', hue = 'athlete_gender')


# In[115]:


sns.displot(df3[df3['race_length'] == '50mi'] ['athlete_average_speed'])


# In[128]:


sns.violinplot(data=df3, x='race_length', y='athlete_average_speed', split=True, inner='quartiles', linewidth=2)


# In[129]:


sns.violinplot(data=df3, x='race_length', y='athlete_average_speed', hue='athlete_gender', split=True, inner='quartiles')


# In[130]:


print(df3['athlete_gender'].value_counts())


# In[131]:


# Categorize "X" values based on majority gender
majority_gender = df3['athlete_gender'].mode()[0]  # Get the majority gender
df3.loc[df3['athlete_gender'] == 'X', 'athlete_gender'] = majority_gender  # Replace "X" values with majority gender


# In[132]:


sns.violinplot(data=df3, x='race_length', y='athlete_average_speed', hue='athlete_gender', split=True, inner='quartiles')


# In[133]:


#questions i want to find out from the dataset


# In[134]:


#difference in speed for the 50k, 50mi male to female


# In[137]:


df3.groupby(['race_length', 'athlete_gender'])  ['athlete_average_speed'].mean().sort_value('mean', ascending = False  )


# In[138]:


#what age group are the best 50m race (20 + races min )


# In[139]:


df3.query('race_length == "50m" ').groupby('athlete_age')['athlete_average_speed'].agg(['mean', 'count']).query('count>19')


# In[ ]:




