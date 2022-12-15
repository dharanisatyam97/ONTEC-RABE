#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[8]:


title = []
companies=[]
snippet=[]


# In[16]:


for page in range(1,100):
    my_url = "https://www.itstellen.at/jobs?keywords=Java+developers&locations=".format(page)
    res = requests.get(my_url).text
    soup = BeautifulSoup(res, "lxml")
    for container in soup.select(".jobInformation.fLeft > h3 > a"):
        title.append(container.text)


    for container in soup.select(".company"):
        companies.append(container.text)

 



    for container in soup.select(".snippet"):
        snippet.append(container.text)


# In[17]:


df_title = pd.DataFrame(title)
df_title


# In[18]:


df_company = pd.DataFrame(companies)
df_company


# In[19]:


df_snippet = pd.DataFrame(snippet)
df_snippet


# In[20]:


df_final = pd.concat([df_title, df_company,df_snippet], axis=1)
df_final.columns=["Job_titles","Company_Name","Description"]
df_final


# In[21]:


df_final.to_csv('itstellen.csv')

