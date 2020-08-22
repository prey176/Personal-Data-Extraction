# Mohit Juneja - 2017067
# Aarish Chhabra - 2017212
# Preyansh Rastogi - 2017176

#!/usr/bin/env python
# coding: utf-8

# # Google Scholar

# In[20]:


import scholarly
username = "Vikram Goyal"


# # Extract Publications

# In[21]:


# extracting yaer-wise publications for analysing event timeline

author = next(scholarly.search_author('Vikram Goyal')).fill()

event_timeline = {}

for publication in author.publications:
    
    year = publication.bib["year"]
    title = publication.bib["title"]
    
    if year not in event_timeline:
        event_timeline[year] = [title]
        
    else:
        event_timeline[year].append(title)
        
    


# In[22]:


print(event_timeline)


# In[23]:


for key in event_timeline:
    print(key)
    for pubs in event_timeline[key]:
        print(pubs)
    print()


# # Year-wise Co-Authors

# In[25]:


# Extracting year-wise engagement using co-authors of various publications

connections = {}

for publication in author.publications:
    
    try:
        publication = publication.fill()
        
    except:
        pass
    
    try:
        year = publication.bib["year"]
        coAuthor = publication.bib["author"]
        
        coAuthor = coAuthor.split(" and ")
        coAuthor.remove(username)
        
    except: 
        pass
    
    
    
    if year not in connections:
        connections[year] = []
        for auth in coAuthor:
            connections[year].append(auth)
            
    else:
        for auth in coAuthor:
            connections[year].append(auth)
    
    


# In[6]:


for key in connections:
    print(key)
    print(', '.join(connections[key]))
    print()


# # Graph - YearWise CoAuthors

# In[27]:


import plotly.graph_objects as go

yearly_count = []
dates = []
for key in sorted(connections.keys()):
    yearly_count.append(len(connections[key]))
    dates.append(key)

    
fig = go.Figure(data=[go.Scatter(
    x=dates, y=yearly_count,
    mode='lines+markers',marker_size=10)
])
fig.update_layout(title="Number of CoAuthors Yearly",xaxis_title = "Year", yaxis_title = "Count")
fig.update_xaxes(tickangle=45)
fig.show()


# # Jaccard Similarity - Graph

# In[28]:


ind = 0
dates = []
jaccard_ratio = []

for key in sorted(connections.keys()):
    if(ind==0):
        prev = set(connections[key])
        
    else:
        if(ind>1):
            prev = curr
        curr = set(connections[key])
        dates.append(key)
        jaccard_ratio.append(len(prev & curr)/len(prev | curr))
    
    ind+=1
    
fig = go.Figure(data=[go.Scatter(
    x=dates, y=jaccard_ratio,
    mode='lines+markers',marker_size=10)
])
fig.update_layout(title="Jaccard Similarity between CoAuthors",xaxis_title = "Year", yaxis_title = "jaccard ratio")
fig.update_xaxes(tickangle=45)
fig.show()  
    


# # Top 10 Co-Authors

# In[29]:


# Finding Top 10 CoAuthors

count = {}

for key in connections:
    for auth in connections[key]:
        if(auth in count):
            count[auth]+=1
        else:
            count[auth]=1

print(sorted(count.items(), key = 
             lambda kv:(kv[1], kv[0]),reverse = True)) 


# # Year Wise Top Co-Authors

# In[32]:


# Findng year wise most CoAuthored Person

dict = {}

for key in sorted(connections.keys()):
    counter = {}
    for auth in connections[key]:
        if auth not in counter:
            counter[auth] = 1
        else:
            counter[auth] += 1
    
    max = 0
    author = ""
    for auth in counter:
        
        if(counter[auth]>max):
            max = counter[auth]
            author = auth
            dict[key] = author
            
print(dict)


# # Facebook Friends Analysis - Vikram Goyal

# In[4]:


import plotly.graph_objects as go
from plotly.offline import iplot, init_notebook_mode

current_city = 0 
hometown = 0
others = 0
total = 0
with open("./../database/facebook_vikram/Current City Friends.txt",'r') as file:
    for line in file:
        current_city+=1

with open("./../database/facebook_vikram/Hometown Friends.txt",'r') as file:
    for line in file:
        hometown += 1

with open("./../database/facebook_vikram/All Friends.txt",'r') as file:
    for line in file:
        total += 1
        
others = total - (current_city + hometown)

init_notebook_mode()

labels = ["Current City","Hometown","Others"]
values = [current_city,hometown,others]

common_props = dict(labels=labels,
                    values=values,)

trace1 = go.Pie(
    **common_props,
    textinfo='percent',
    textposition='outside')

trace2 = go.Pie(
    **common_props,
    textinfo='label',
    textposition='inside')

iplot([trace1, trace2], filename='basic_pie_chart')


# # # Facebook Friends Analysis - Sankha Basu

# In[5]:


current_city = 0 
hometown = 0
others = 0
total = 0


with open("./../database/facebook_sankha/Current City Friends.txt",'r') as file:
    for line in file:
        current_city+=1

with open("./../database/facebook_sankha/Hometown Friends.txt",'r') as file:
    for line in file:
        hometown += 1

with open("./../database/facebook_sankha/All Friends.txt",'r') as file:
    for line in file:
        total += 1
        
    
others = total - (current_city + hometown)


init_notebook_mode()

labels = ["Current City","Hometown","Others"]
values = [current_city,hometown,others]

common_props = dict(labels=labels,
                    values=values,)

trace1 = go.Pie(
    **common_props,
    textinfo='percent',
    textposition='outside')

trace2 = go.Pie(
    **common_props,
    textinfo='label',
    textposition='inside')

iplot([trace1, trace2], filename='basic_pie_chart')


# # LinkedIn

# In[9]:


from linkedin_api import Linkedin
api = Linkedin("jaugastia@gmail.com","psosm1234")


# In[2]:


username = "vikram-goyal-7a684213"


# # Extract Education

# In[3]:


profile = api.get_profile(username)              # returns a dictionary
edu = profile["education"]                       # returns list of dictionaries


# In[4]:


# extracting education for analysing event timeline

req = ["schoolName","degreeName","timePeriod","fieldOfStudy"]

for entity in edu:
    for requirement in req:
        if requirement in entity:
            print(requirement,":"," ",entity[requirement])
    print()


# # Extract Experience

# In[5]:


# extracting experience for analysing event timeline

req = ["locationName","companyName","timePeriod","title","description"]

for exp in profile["experience"]:
    for requirement in req:
        if requirement in exp:
            if requirement != "timePeriod":
                print(requirement,":"," ",exp[requirement])
            else:
                print(requirement,":" " ",exp[requirement]["startDate"]["year"])
    print()

