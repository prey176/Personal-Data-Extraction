# Mohit Juneja - 2017067
# Aarish Chhabra - 2017212
# Preyansh Rastogi - 2017176

#!/usr/bin/env python
# coding: utf-8

# # LinkedIn Authentication

# In[2]:


from linkedin_api import Linkedin


# In[3]:


email = 'jaugastia@gmail.com'
password = 'psosm1234'


# In[4]:


# Authenticate using any Linkedin account credentials
api = Linkedin(email,password)


# In[5]:


username = 'sankha-basu-157333aa'


# In[6]:


# Get a profile
profile = api.get_profile(username)


# # Extract Experience

# In[7]:


for a in profile['experience'] :
    print ('Company Name :',a['companyName'])
    print ('Title :',a['title'])
    print ('TimePeriod :',str(a['timePeriod']['startDate']['year']))
    try :
        print ('Description :', a['description'])
    except :
            pass
    print()


# # Extract Education

# In[8]:


for a in profile['education'] :
    print ('School Name :', a['schoolName'])
    print ('Degree :',a['degreeName'])
    print ('Feild of Study :',a['fieldOfStudy'])
    try :
        print ('Year :', a['timePeriod']['startDate']['year'])
    except :
        pass
    print ()


# In[9]:


profile

