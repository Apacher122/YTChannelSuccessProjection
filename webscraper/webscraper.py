from csv import writer
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession

playlistcount = 33

# Web driver
url = "https://www.youtube.com/watch?v=-UJSd31nzqs&list=UUwG60McbuKGsj53_JLoY-9Q&index=1"
driver = webdriver.Firefox()
driver.get(url)
session = HTMLSession()
        response = session.get(url)
        response.html.render(sleep=1)
        soup = bs(response.html.html, "html.parser")



# os.remove('youtubeData.csv')

# with open('youtubeData.csv', 'a', newline ='') as f_obj:
#     writer = writer(f_obj)
#     for i in range(0, playlistcount):
#         time.sleep(3)
#         response = session.get(url)
#         response.html.render(sleep=1)
#         soup = bs(response.html.html, "html.parser")
        
#         # video category
#         # definition
#         # duration
#         # embeddable
#         # licenced?
#         # viewcount per video
#         # viewcount of channel
#         # number of videos on channel
#         # number of subscribers
#         # video description length
#         # number of tags in description
#         # video title length
#         # number of tags in title
#         # tags applied by publisher to video
#         # channel name length
#         # channel description length
#         # video age in months
#         # channel age in months
#         # day uploaded
#         # number of socialmedia links
        
        
        
        
#         viewCount = soup.find("meta",itemprop="interactionCount")['content']
#         upDate  = soup.find("meta",itemprop="datePublished")['content']
#         data = [upDate, viewCount]
#         writer.writerow(data)

#         button = driver.find_element(By.ID, 'movie_player')
#         button.send_keys(Keys.SHIFT, "N")
#         url = driver.current_url
#         print(url)
#     f_obj.close()

