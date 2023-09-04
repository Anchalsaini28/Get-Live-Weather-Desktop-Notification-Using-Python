#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from bs4 import BeautifulSoup


# In[9]:


pip install win10Toast


# In[10]:


from win10toast import ToastNotifier


# In[11]:


#Create an object of ToastNotifier class.
n = ToastNotifier()


# In[12]:


#Define a function for getting data from the given url.

def getdata(url):
    r = requests.get(url)
    return r.text


# In[13]:


#Now pass the URL into the getdata function and Convert that data into HTML code.
htmldata = getdata("https://weather.com/en-IN/weather/today/l/8942645b881fd43fc86ed2d932370e550513245460cabb6a48b38a3089406d92")
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup.prettify())


# In[14]:


#Find the required details and filter them 
current_temp = soup.find_all("span", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
  
chances_rain = soup.find_all("div", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
  
temp = (str(current_temp))
  
temp_rain = str(chances_rain)


result = "current_temp " + temp[128:-9] + " in Thane, Maharashtra" + "\n" + temp_rain[131:-14]
n.show_toast("live Weather update", 
             result, duration = 10)


# In[ ]:





# In[ ]:





# In[ ]:




