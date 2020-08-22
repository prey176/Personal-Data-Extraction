# Mohit Juneja - 2017067
# Aarish Chhabra - 2017212
# Preyansh Rastogi - 2017176

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scholarly


# In[2]:


username = 'TANMOY CHAKRABORTY'


# In[3]:


author = list(scholarly.search_author(username))[1].fill()


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
        print (a.bib['author'])
    except :
        pass
    print()


# # Co-Authors

# In[6]:


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
            if len(b) < len('TANMOY') or b[:len('TANMOY')] !='Tanmoy' :
                coauthors_.append(b)
    except :
        continue
    COAUTHORS[key_].extend(coauthors_)
    if len(coauthors_) == 0 : 
        coauthors_ = ['No Coauthors']


# In[7]:


COAUTHORS


# In[8]:


years = [2008,2009,2010,2011,2012,2013]
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


# # Jaccard Similarity

# In[9]:


import plotly.graph_objects as go


# In[10]:


fig1 = go.Figure()


# In[11]:


import numpy as np


# In[12]:


fig1.add_trace(go.Scatter(x = arr1,y = arr2,mode='lines'))


# In[13]:


fig1.update_layout(title = 'Jaccard Similarity of Co-authors of adjacent years', xaxis_title = 'Year', yaxis_title = 'Co-author Count')


# In[ ]:





# In[14]:


years = [2008,2009,2010,2011,2012,2013]
good = [len(COAUTHORS[a]) for a in years]


# In[15]:


import plotly.graph_objects as go

fig2 = go.Figure()

import numpy as np


# In[16]:


fig2.add_trace(go.Scatter(x = years,y = good,mode='lines'))


# In[17]:


fig2.add_trace(go.Scatter(x = years,y = good,mode='markers'))


# In[18]:


fig2.update_layout(title = 'Number of Co-authors vs Year', xaxis_title = 'Year', yaxis_title = 'Co-author Count')


# # Top 10 Co-Authors

# In[21]:


dict_ = {}
for a in COAUTHORS :
    for b in COAUTHORS[a] :
        if b not in dict_ :
            dict_[b] = 0
        dict_[b]+=1
LIST = []
for a in dict_.keys():
    LIST.append((a,dict_[a]))
LIST = sorted(LIST, key = lambda x: x[1], reverse=True)


# In[42]:


for i in range (10) :
    print (*LIST[i])


# # Year Wise Top Authors

# In[39]:


most_engage = {}
for a in COAUTHORS :
    if (a < 2014) :
        count_ = {}
        for b in COAUTHORS[a] :
            if b not in count_ :
                count_[b] = 0
            count_[b]+=1
        maxperson = []
        maxoccur = 0
        for b in count_ :
            if count_[b] > maxoccur :
                maxoccur = count_[b]
                maxperson = b
        most_engage[a] = (maxperson)


# In[40]:


most_engage

