#!/usr/bin/env python
# coding: utf-8

# In[77]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[78]:


title = []
companies=[]
snippet=[]


# In[79]:


for page in range(1,100):
    my_url = "https://www.metajob.at/java%20developer".format(page)
    res = requests.get(my_url).text
    soup = BeautifulSoup(res, "lxml")
    for container in soup.select(".rTitle"):
        title.append(container.text)
    for container in soup.select(".rUrl"):
        companies.append(container.text)
    for container in soup.select(".snippet.hyphenate"):
        snippet.append(container.text)


# In[80]:


df_title = pd.DataFrame(title)
df_title


# In[81]:


df_company = pd.DataFrame(companies)
df_company


# In[82]:


df_snippet = pd.DataFrame(snippet)
df_snippet


# In[83]:


df_final = pd.concat([df_title, df_company,df_snippet], axis=1)
df_final.columns=["Job_titles","Company_Name","Description"]
df_final


# In[85]:


df_final.to_csv('meta.csv')

