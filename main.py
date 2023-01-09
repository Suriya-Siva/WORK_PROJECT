
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re




URL ="https://docs.fortinet.com/product/fortigate/7.0"
URL2='https://docs.fortinet.com'


page = requests.get(URL)
soup = BeautifulSoup(page.text,'lxml')
soup

mainpage=[]
subpage=[]

## getting all links from webpage
for z in soup.findAll('a',{'class':"version-item-external"}):
    dir=z.get('href')
    
## searching only for release notes
    if re.search('fortios-release-notes$',dir):
      mainpage.append(URL2+dir)


for i in mainpage:
  page2=requests.get(i)
  soup2=BeautifulSoup(page2.text,'lxml')

# ## getting all links from release notes page
  for a in soup2.findAll('a',{'class':"toc"}):

## wanting only change log page   
    dir2=a.get('href')
    if (re.search('change-log$',dir2)) and (URL2+dir2 not in subpage) :
      subpage.append(URL2+dir2)
print(subpage)

#third part of the code to compare the dates
for x in subpage:
  page3=requests.get(x)
  soup3=BeautifulSoup(page3.text,'lxml')
  date=soup3.find('td',{'class':'TableStyle-FortinetTable-BodyE-Column1-Body1'})
  
  print(date)


    

            
        



    

   