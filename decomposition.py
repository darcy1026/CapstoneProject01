#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose


# In[60]:


# make key
def make_key(time):
    key = str(time.month) + "-" + str(time.day) + "-" + str(time.hour) 
    return key


# In[33]:


data = pd.read_csv('ten_airports_num_of_flights.csv', dtype='str')
data['time'] = pd.to_datetime(data['time'])


# In[34]:


data.shape


# In[35]:


data.head()


# In[36]:


airports = data['airport'].unique()


# In[147]:


def get_final_data(airport, weather, airport_name):
    # select the columns, add the key
    weather = weather[['icon', 'temperature', 'windSpeed', 'visibility', 'summary', 'time']]
    weather['time'] = pd.to_datetime(weather['time'])
    weather['key'] = weather['time'].apply(make_key)
    
    # add key
    airport['time'] = pd.to_datetime(airport['time'])
    airport['key'] = airport['time'].apply(make_key)
    
    # merge the airport flight data and weather
    merged = pd.merge(airport, weather, on='key', how='left')
    merged = merged.drop('key', axis=1)
    merged = merged.rename(columns={'time_x':'flight_time', 'time_y':'weather_time'})
    
    merged.to_csv('#of_flights_with_weather/'+airport_name+'_final_data1.csv', index=False)
    
    return merged


# In[128]:


airports = data['airport'].unique()
for airport in airports:
    df_sub = data[data['airport'] == airport]


# In[154]:


airports


# In[152]:


def get_weather(name):
    df = pd.read_csv('weather_data/'+name+'_weather.csv')
    return df


# In[153]:


for i in airports:
    weather = get_weather(i)
    airport_final_data = get_columns(data[data['airport'] == i], weather, i)


# # sample data selected randomly as DFW

# In[160]:


dfw = pd.read_csv('final_data/DFW_final_data1.csv')


# In[161]:


dfw


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




