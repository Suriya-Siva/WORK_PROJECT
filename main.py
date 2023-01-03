
import requests
from bs4 import BeautifulSoup
import pandas as pd




URL ="https://docs.fortinet.com/document/fortigate/7.0.9/fortios-release-notes/553516/change-log"



page = requests.get(URL)
soup = BeautifulSoup(page.text,'lxml')
soup
table1 = soup.find('thead')
table1

headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)
         

print (headers)
    

   