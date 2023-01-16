
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime
import openpyxl 


URL ="https://docs.fortinet.com/product/fortigate/7.0"
URL2='https://docs.fortinet.com'
path = "C:/Users/P1350392/OneDrive - NCS Pte Ltd/work proj files/SSOE2 Software Inventory - Network (Tab 9).xlsx"

page = requests.get(URL)
soup = BeautifulSoup(page.text,'lxml')
soup

mainpage=[]
subpage=[]
dates=[]
dict={}
final_date=["1000-10-1"]


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

#part of the code to get the dates
for x in subpage:
  page3=requests.get(x)
  soup3=BeautifulSoup(page3.text,'lxml')
  for date in soup3.find('td',{'class':'TableStyle-FortinetTable-BodyE-Column1-Body1'}):
    if date.text != '\n':
      dates.append(date.text)

  
# creating a new dictionary key value pair with the key being the link and the value being the date
for key1 in subpage:
  for key2 in dates:
    dict[key1]=key2
    dates.remove(key2)
    break



# finding the latest date the latest date
for values in dict.values():

  try:
    from_value = datetime.strptime(values, '%Y-%m-%d')
    latest_date= datetime.strptime(final_date[0],'%Y-%m-%d')
   
    if from_value > latest_date :
      final_date.clear()
      final_date.append(values)
  except ValueError as message:
    print('A value error is raised because :', message)

#after getting the value we append into the file 
final_date=final_date[0]
final_link = list(filter(lambda x: dict[x] == final_date, dict))[0]

page4=requests.get(final_link)
soup4=BeautifulSoup(page4.text,'lxml')

latest_version=soup4.find('span',{'class':'current-version'}).text



wb_obj = openpyxl.load_workbook(path) 
sheet= wb_obj.active 
#slotting in the latest market verion avail
cell = sheet['L10']
cell.value= latest_version
#slotting in market version latest release date
cell2 =sheet['M10']
cell2.value=final_date
#latest release version support
cell2a=sheet['N10']
cell2a.value=final_date
#slotting in the link into the file
cell3=sheet['F10']
cell3.value=final_link

#updating remarks 
cellremarks=sheet['Y10']
today = datetime.today()
d2 = today.strftime("%Y-%m-%d")
current_time = datetime.now()
fmt_current_time=current_time.strftime("%H:%M:%S")
cellremarks.value=d2+" "+ fmt_current_time + " (bot) : Updated by bot at this time"
wb_obj.save(filename="sample.xlsx")
         

            
        



    

   