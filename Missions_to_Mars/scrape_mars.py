#!/usr/bin/env python
# coding: utf-8

# # NASA Mars News

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.by import By
import time

# In[2]:

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    #browser = Browser('chrome', **executable_path, headless=False)
    return Browser('chrome', **executable_path, headless=False)

# In[3]:

def scrape():
    browser=init_browser()
    url = 'https://redplanetscience.com/'
    time.sleep(5)
    browser.visit(url)
   
    # In[4]:  

# In[5]:

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('div', class_='list_text')


    # In[6]:


    news_title_all=[]
    news_p_all=[]

    for result in results:

        title=result.find('div', class_='content_title')
        news_title_all.append(title)
        para=result.find('div', class_='article_teaser_body')
        news_p_all.append(para)

    news_title=news_title_all[0].text
    #print(news_title)
    news_p =news_p_all[0].text
    #print(news_p)


    # In[7]:


    browser.quit()
    
    # # JPL Mars Space Images - Featured Image

    # In[8]:


#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)


    # In[9]:

    browser=init_browser()
    url='https://spaceimages-mars.com/' 
    browser.visit(url)
    time.sleep(1)

    # In[10]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[11]:


    results=soup.find('img', class_='headerimage')
    image_url=results['src']
    featured_image_url=url+image_url


    # In[12]:


    #print(featured_image_url)


    # In[13]:


    browser.quit()


    # # Mars Facts

    # In[14]:


    url='https://galaxyfacts-mars.com'
    table=pd.read_html(url)


    # In[15]:


    #table


    # In[16]:


    planetfacts_df=table[1]
    planetfacts_df.columns=['Description','Values']


    # In[17]:


    planetfacts_df


    # In[18]:


    #planetfacts_df.to_html("../Output/Mars_Facts.html",index=False)


    # In[19]:


    Mars_facts=planetfacts_df.to_html()
    #print(Mars_facts)


    # # Mars Hemispheres

    # In[20]:


#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)


    # In[21]:

    browser=init_browser()
    url='https://marshemispheres.com/' 
    browser.visit(url)
    time.sleep(1)

    # In[22]:


    html=browser.html
    soup=BeautifulSoup(html,'html.parser')


    # In[23]:


    results=soup.find_all('div',class_='item')


    # In[24]:


    hemisphere_image_urls = []

    for result in results:
        #Getting the title
        x=result.find('h3').text
        title1=x.strip('Enhanced')

        #Getting the image URL
        first_page=result.find('a')
        first_page_src=first_page['href']
        first_page_url=url+first_page_src
        browser.visit(first_page_url)
        html=browser.html
        soup=BeautifulSoup(html,'html.parser')
        full_img=soup.find('img',class_='wide-image')
        full_img_url=url+full_img['src']

        hemisphere_image_urls.append({
        'title':title1,
        'img_url':full_img_url})



    # In[25]:


    hemisphere_image_urls


    # In[26]:


    browser.quit()


    # In[27]:


    # Create empty dictionary for all Mars Data.
    mars_data = {}

    # Append news_title and news_paragraph to mars_data.
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p
    # Append featured_image_url to mars_data.
    mars_data['featured_image_url'] = featured_image_url
    # Append mars_facts to mars_data.
    mars_data['Mars_facts'] = Mars_facts
    # Append hemisphere_image_urls to mars_data.
    mars_data['hemisphere_image_urls'] = hemisphere_image_urls
    mars_data

    return mars_data
    # In[ ]:




