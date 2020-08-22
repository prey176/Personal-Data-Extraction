# Mohit Juneja - 2017067
# Aarish Chhabra - 2017212
# Preyansh Rastogi - 2017176

#!/usr/bin/env python
# coding: utf-8

# # Twitter Authentication

# In[1]:


import tweepy

#Consumer Key (API Key), Consumer Secret (API Secret)
auth = tweepy.OAuthHandler('s9iqHQMCnqbRSTYLZijznltjj', 
                           'edpnKGn7l90SPKoFBc5eiBi2kEjb5sFe5CfH2vZ4O51g1lvfXw')
# Access Token, Access Token Secret
auth.set_access_token('914187849875914752-DEpIlQagvnjUdJ8vvKwe2IxF8luSUab', 
                      '8NyTquzkP9i7XX2dSUDPrO6u157i5FMNK7JwsibtyOCFS')

api = tweepy.API(auth)
if (not api):
    print("Authentication failed :(")
else:
    print("Authentication successfull!!! :D")


# In[4]:


import datetime

tweets = []

for tweet in tweepy.Cursor(api.user_timeline,screen_name="Tanmoy_Chak").items():
    tweets.append(tweet)
print(len(tweets))


# # Favourite Count

# In[ ]:


engagement = {}

import datetime
import time

endDate = datetime.datetime.today()

curDate = tweets[-1].created_at
increase = datetime.timedelta(days=180)
COUNT_EVERY_30_DAYS = []
while (curDate < endDate) :
    nextDate = curDate + increase
    likes = 0
    for tweet in tweets :
        if tweet.created_at < nextDate and tweet.created_at > curDate:
            try:
                likes += tweet.favorite_count
                    
            except:
                pass
    
    arr = str(curDate).split(" ")
    date = arr[0]
    
    engagement[date] = likes
                
    curDate = nextDate
    

print(tweets[-1].favorite_count)


# In[ ]:


print(engagement)


# # Graph - Favourite Count

# In[ ]:


import plotly.graph_objects as go

count = []
dates = []

for key in sorted(engagement.keys()):
    dates.append(key)
    count.append(engagement[key])
    
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=dates, y=count,
    mode='lines+markers',marker_size=10)
)
fig.update_layout(title="Favorite Count in span of 6 months",xaxis_title = "Start Date", yaxis_title = "count")
fig.update_xaxes(tickangle=45)
fig.show()

print(dates)


# # User Mentions

# In[7]:


engagement_mentions = {}

import datetime
import time

endDate = datetime.datetime.today()

curDate = tweets[-1].created_at
increase = datetime.timedelta(days=180)
COUNT_EVERY_30_DAYS = []
while (curDate < endDate) :
    nextDate = curDate + increase
    users = []
    for tweet in tweets :
        if tweet.created_at < nextDate and tweet.created_at > curDate:
            try:
                for user in tweet.entities["user_mentions"]:
                    users.append(user["screen_name"])
                    
            except:
                pass
    
    arr = str(curDate).split(" ")
    date = arr[0]
    
    engagement_mentions[date] = users
                
    curDate = nextDate


# In[8]:


print(engagement_mentions)


# # Graph - User Mentions

# In[ ]:


count = []
dates = []

for key in sorted(engagement_mentions.keys()):
    dates.append(key)
    count.append(len(engagement_mentions[key]))
    
fig = go.Figure(data=[go.Scatter(
    x=dates, y=count,
    mode='lines+markers',marker_size=10)
])
fig.update_layout(title="User Mention Count in span of 6 months",xaxis_title = "Start Date", yaxis_title = "count")
fig.update_xaxes(tickangle=45)
fig.show()

print(dates)


# # Jaccard Similarity - User Mentions

# In[ ]:


ind = 0
dates = []
jaccard_ratio = []

for key in sorted(engagement_mentions.keys()):
    if(ind==0):
        prev = set(engagement_mentions[key])
        
    else:
        if(ind>1):
            prev = curr
        curr = set(engagement_mentions[key])
        dates.append(key)
        jaccard_ratio.append(len(prev & curr)/len(prev | curr))
    
    ind+=1

    
fig = go.Figure(data=[go.Scatter(
    x=dates, y=jaccard_ratio,
    mode='lines+markers',marker_size=10)
])
fig.update_layout(title="Jaccard Similarity between User Mentions on tweets",xaxis_title = "Year", yaxis_title = "jaccard ratio")
fig.update_xaxes(tickangle=45)
fig.show()  


# In[ ]:


for key in engagement_mentions:
    print(key)
    print(", ".join(engagement_mentions[key]))
    print()


# # Top 10 User Mentions

# In[ ]:


# Finding top 10 user mentions 

count = {}

for key in engagement_mentions:
    for user in engagement_mentions[key]:
        if(user in count):
            count[user]+=1
        else:
            count[user]=1

print(sorted(count.items(), key = 
             lambda kv:(kv[1], kv[0]),reverse = True)) 


# # Top Mentioned Users in span of 6 months

# In[9]:


dict = {}

for key in engagement_mentions:
    counter = {}
    for user in engagement_mentions[key]:
        if(user not in counter):
            counter[user]=1
        else:
            counter[user]+=1
            
    max = 0
    final_user = ""
    for user in counter:
        if(counter[user] > max):
            max = counter[user]
            final_user = user
            dict[key] = user
            
print(dict)


# # Profile Updates

# In[ ]:


updates = {}

with open("./../database/Tanmoy_profileUpdate.txt",'r') as file:
    for line in file:
        year = line.split(",")[0][-2:]
        if(year in updates):
            updates[year]+=1
        else:
            updates[year]=1
            

            
fig = go.Figure(data=[go.Scatter(
    x=list(updates.keys()), y=list(updates.values()),
    mode='lines+markers',marker_size=10)
])
fig.update_layout(title="Year-Wise Updates",xaxis_title = "Year", yaxis_title = "Count")
fig.update_xaxes(tickangle=45)
fig.show() 


# In[ ]:


import tweepy
import datetime
import time


# In[ ]:


ACCESS_TOKEN ="1008440742816067584-3qoAe6npYlB5KRNW4fnNmG6AjteqHP"
ACCESS_TOKEN_SECRET="NRBehYexj56v7HnMTIFrkxW7JlCkOpjMt2SQn0RSwTURI"
CONSUMER_KEY="vgr02kOoSOI1skzNZ9O8ENJQv"
CONSUMER_SECRET="V4F40uptgWfHdxVpPsWyvMukmSH3ydMSYtltEsj6BExBniJIP0"


# In[ ]:


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)


# In[ ]:


api = tweepy.API(auth)
if (not api):
    print("Authentication failed :(")
else:
    print("Authentication successfull!!! :D")

try:
    api.verify_credentials()
except:
    pass


# In[ ]:


user = '@tanmoy_chak'


# In[ ]:


import pickle, datetime
tweets = []
for tweet in tweepy.Cursor(api.user_timeline, id=user, tweet_mode='extended').items():
    tweets.append(tweet)


# In[ ]:


# We dumped the retweets so that we don't have to run the api query again
# And they are limited in a time window
# So we commented the code for making the api queries, so that we could run the file multiple times
# Without wasting time 


# In[ ]:


# retweets = []
# for a in tweets:
#     if a.retweet_count == 0 :
#         continue
#     try :
#         retweets.append(api.retweets(a.id))
#     except:
#         time.sleep(16*60)
#         retweets.append(api.retweets(a.id))


# In[12]:


import pickle


# # Load Data

# In[13]:


def loadData():  
    dbfile = open('../database/TANMOY_RETWEETS', 'rb')      
    D = pickle.load(dbfile)
    return D


# # Retweets Count

# In[14]:


retweets = loadData()
print(len(retweets))


# In[18]:


time_tweets = []
for tweet in tweets :
    if tweet.retweet_count == 0 :
        continue
    time_tweets.append(tweet.created_at)


# In[ ]:


print (len(time_tweets))


# In[ ]:


retweets[0][0].user.screen_name


# In[16]:


date_ = tweets[-1].created_at
date_ = str(date_).split(' ')[0]
date_


# In[15]:


import time
import datetime


# # Retweeters Extraction

# In[19]:


curDate = tweets[-1].created_at
endDate = tweets[0].created_at
increase = datetime.timedelta(days=180)
engagement = {}
while (curDate <= endDate) :
    nextDate = curDate + increase
    names = []
    for i in range (len(retweets)) :
        if time_tweets[i] < nextDate and time_tweets[i] > curDate :
            for j in retweets[i] :
                names.append(j.user.screen_name)
#     names = list(set(names))
    date_ = str(curDate).split(' ')[0]
    engagement[date_] = names 
    curDate = nextDate


# In[ ]:


for a in engagement :
    print (a)
    print(', '.join(engagement[a]))
    print ()


# In[ ]:


import plotly.graph_objects as go


# In[ ]:


fig1 = go.Figure()


# In[ ]:


import numpy as np


# # Graph - Retweeters

# In[ ]:


arr1 = [a for a in engagement]
arr2 = [len(engagement[a]) for a in engagement]
fig1.add_trace(go.Scatter(x = arr1,y = arr2,mode='markers'))


# In[ ]:


fig1.update_layout(title = 'Number of Retweets per 6 Months', xaxis_title = 'Year', yaxis_title = 'Retweets Count')


# # Jaccard Similarity - Graph

# In[ ]:


fig2 = go.Figure()

arr1 = [a for a in engagement]
arr2 = [set(engagement[a]) for a in arr1]
arr3 = []
arr4 = []
for i in range (len(arr2)-1) :
    val1 = len(arr2[i+1]&arr2[i])
    val2 = len(arr2[i+1]|arr2[i])
    if (val2 == 0) :
        print (arr1[i])
        continue
    arr4.append(arr1[i])
    arr3.append(val1/val2)

fig2.update_layout(title = 'Jaccard Similarity between 2 adjacent 6 month period', xaxis_title = 'Year', yaxis_title = 'Jaccard Similarity')


# In[ ]:


fig2.add_trace(go.Scatter(x = arr4,y = arr3,mode='markers'))


# # Top 10 Retweeters

# In[ ]:


dict_ = {}
for a in engagement :
    for b in engagement[a]:
        if b not in dict_ :
            dict_[b]=0
        dict_[b]+=1
print (dict_)


# In[ ]:


LIST = []
for a in dict_.keys():
    LIST.append((a,dict_[a]))
LIST = sorted(LIST, key = lambda x: x[1], reverse=True)


# In[ ]:



for a in range(10):
    print (*LIST[a])


# # Top retweeters in span of 6 months

# In[20]:


dict = {}

for key in engagement:
    counter = {}
    for user in engagement[key]:
        if(user not in counter):
            counter[user]=1
        else:
            counter[user]+=1
            
    max = 0
    final_user = ""
    for user in counter:
        if(counter[user] > max):
            max = counter[user]
            final_user = user
            dict[key] = user
            
print(dict)


# # Sample Tweets

# In[ ]:


for i in range (10) :
    print (tweets[i].full_text)
    print (tweets[i].created_at)
    print()


# In[ ]:




