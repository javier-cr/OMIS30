#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Name: Javier Ramirez
# Date: 11/28/18
# Purpose: Find a better solution to the world_pop problem


# In[2]:


import pandas as pd


# In[3]:


world_pop = pd.read_csv('world_pop.csv')


# In[4]:


world_pop_list = []
for row in world_pop.values:
    world_pop_list.append(list(row))


# In[5]:


import time

top_countries = []
continents = set(x[1] for x in world_pop_list)
operation_count = 0
start_time = time.time()

# Create a list for each continent
Asia = []
Africa = []
Americas = []
Europe = []
Oceania = []

# Sort countries into their respective country lists
for row in world_pop_list:
    if row[1] == 'Asia':
        Asia.append(row)
        operation_count += 1
    elif row[1] == 'Africa':
        Africa.append(row)
        operation_count += 1
    elif row[1] == 'Americas':
        Americas.append(row)
        operation_count += 1
    elif row[1] == 'Europe':
        Europe.append(row)
        operation_count += 1
    elif row[1] == 'Oceania':
        Oceania.append(row)
        operation_count += 1

# Find max of each continent
top_countries = []
top_countries.append(max(Asia, key=lambda e: int(e[2])))
operation_count += 1
top_countries.append(max(Europe, key=lambda e: int(e[2])))
operation_count += 1
top_countries.append(max(Americas, key=lambda e: int(e[2])))
operation_count += 1
top_countries.append(max(Oceania, key=lambda e: int(e[2])))
operation_count += 1
top_countries.append(max(Africa, key=lambda e: int(e[2])))
operation_count += 1

# Print results
end_time = time.time()
time_it_took = end_time - start_time
print('There are ' + str(len(world_pop_list)) + ' countries.')
print('It took this method ' + str(operation_count) + ' operations to get to our answer.')
print('It took ' + str(time_it_took) + ' seconds to run.')
top_countries

