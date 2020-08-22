# Mohit Juneja - 2017067
# Aarish Chhabra - 2017212
# Preyansh Rastogi - 2017176

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scholarly


# In[2]:


username = 'Sankha S. Basu'


# In[3]:


author = list(scholarly.search_author(username))[1].fill()


# In[11]:


author


# # Publications

# In[4]:


Publications = []
for a in author.publications :
    try :
        Publications.append(a.fill())
    except :
        pass


# In[5]:


for a in Publications :
    try :
        print ('Title :',a.bib['title'])
    except:
        pass
    try :
        print ('Year :',a.bib['year'])
    except :
        pass
    print()


# # Co-Authors

# In[9]:


COAUTHORS = {}
YEAR_FRIEND = {}
for a in Publications :
    try :
        key_ = a.bib['year']
    except :
        continue
    if key_ not in COAUTHORS :
        COAUTHORS[key_] = []
    coauthors_ = []
    try :
        for b in a.bib['author'].split(' and ') :
            if len(b) < len('Sankha') or b[:len('Sankha')] !='Sankha' :
                coauthors_.append(b)
    except :
        continue
    COAUTHORS[a.bib['year']].extend(coauthors_)
    if len(coauthors_) == 0 : 
        coauthors_ = ['No Coauthors']


# In[10]:


COAUTHORS


# In[19]:


COAUTHORS[2016][1] = 'Stephen G Simpson'


# In[20]:


years = [2013,2014,2016,2020]
good = [set(COAUTHORS[a]) for a in years]
arr1 = []
arr2 = []
for i in range(len(years)-1) :
    val1 = len(good[i]&good[i+1])
    val2 = len(good[i]|good[i+1])
    if val2 == 0 :
        continue
    arr1.append(years[i])
    arr2.append(val1/val2)


# # Jaccard Similarity Graph

# In[21]:


import plotly.graph_objects as go


# In[22]:


fig1 = go.Figure()


# In[23]:


import numpy as np


# In[26]:


fig1.add_trace(go.Scatter(x = arr1,y = arr2,mode='lines'))


# In[27]:


fig1.update_layout(title = 'Jaccard Similarity of Co-authors of adjacent years', xaxis_title = 'Year', yaxis_title = 'Co-author Count')


# # Year Wise Co-Authors

# In[28]:


years = [2013,2014,2016,2020]
good = [len(COAUTHORS[a]) for a in years]


# In[29]:


import plotly.graph_objects as go

fig2 = go.Figure()

import numpy as np


# In[30]:


fig2.add_trace(go.Scatter(x = years,y = good,mode='lines'))


# In[31]:


fig2.add_trace(go.Scatter(x = years,y = good,mode='markers'))


# In[32]:


fig2.update_layout(title = 'Number of Co-authors vs Year', xaxis_title = 'Year', yaxis_title = 'Co-author Count')


# In[ ]:


years = [2008,2009,2010,2011,2012,2013]
good = [len(COAUTHORS[a]) for a in years]

import plotly.graph_objects as go

fig2 = go.Figure()

import numpy as np

fig2.add_trace(go.Scatter(x = years,y = good,mode='lines'))

fig2.add_trace(go.Scatter(x = years,y = good,mode='markers'))

fig2.update_layout(title = 'Number of Co-authors vs Year', xaxis_title = 'Year', yaxis_title = 'Co-author Count')

