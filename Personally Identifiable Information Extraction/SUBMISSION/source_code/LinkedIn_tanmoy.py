# Mohit Juneja - 2017067
# Aarish Chhabra - 2017212
# Preyansh Rastogi - 2017176

#!/usr/bin/env python
# coding: utf-8

# # LinkedIn Authentication

# In[1]:


from linkedin_api import Linkedin


# In[2]:


email = 'jaugastia@gmail.com'
password = 'psosm1234'


# In[3]:


# Authenticate using any Linkedin account credentials
api = Linkedin(email,password)


# In[4]:


username = 'tanmoy-chakraborty-89553324'


# In[5]:


# Get a profile
profile = api.get_profile(username)


# # Extract Experience

# In[6]:


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

# In[7]:


for a in profile['education'] :
    print ('School Name :', a['schoolName'])
    try :
        print ('Degree :',a['degreeName'])
    except :
        pass
    try :
        print ('Feild of Study :',a['fieldOfStudy'])
    except:
        pass
    try :
        print ('Year :', a['timePeriod']['startDate']['year'])
    except :
        pass
    print ()

