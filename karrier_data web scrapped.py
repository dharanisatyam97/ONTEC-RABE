#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


title = []
companies=[]
snippet=[]


# In[3]:


for page in range(1,100):
    my_url = "https://www.karriere.at/jobs/java-developers".format(page)
    res = requests.get(my_url).text
    soup = BeautifulSoup(res, "lxml")
    for container in soup.select(".m-jobsListItem__title"):
        title.append(container.text)
    for container in soup.select(".m-jobsListItem__companyName"):
        companies.append(container.text)
    for container in soup.select(".m-jobsListItem__snippet"):
        snippet.append(container.text)


# In[4]:


df_title = pd.DataFrame(title)
df_title


# In[5]:


df_company = pd.DataFrame(companies)
df_company


# In[6]:


df_snippet = pd.DataFrame(snippet)
df_snippet


# In[7]:


df_final = pd.concat([df_title, df_company,df_snippet], axis=1)
df_final.columns=["Job_titles","Company_Name","Description"]
df_final


# In[8]:


df_final.to_csv('karrier.csv')

