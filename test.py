import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create an URL object
url = 'https://www.worldometers.info/coronavirus/'
# Create object page
page = requests.get(url)
# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')
soup
# Obtain information from tag <table>
table1 = soup.find('table', id='main_table_countries_today')
table1
# Obtain every title of columns with tag <th>
headers = []
for i in table1.find_all('th'):
 title = i.text
 headers.append(title)
 print(headers)
 # Convert wrapped text in column 13 into one line text
headers[13] = 'Tests/1M pop'
# Create a dataframe
mydata = pd.DataFrame(columns = headers)
# Create a for loop to fill mydata
for j in table1.find_all('tr')[1:]:
 row_data = j.find_all('td')
 row = [i.text for i in row_data]
 length = len(mydata)
 mydata.loc[length] = row
 # Drop and clearing unnecessary rows
mydata.drop(mydata.index[0:7], inplace=True)
mydata.drop(mydata.index[222:229], inplace=True)
mydata.reset_index(inplace=True, drop=True)
# Drop “#” column
mydata.drop('#', inplace=True, axis=1)
# Export to csv
mydata.to_csv('covid_data.csv', index=False)
# Try to read csv
mydata2 = pd.read_csv('covid_data.csv')



import requests
from bs4 import BeautifulSoup
import pandas as pd




URL ="https://docs.fortinet.com/document/fortigate/7.0.9/fortios-release-notes/553516/change-log"
https://docs.fortinet.com/product/fortigate/7.0


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
    

   for i in range(len(fmt_dates)): 
    print(fmt_dates[i])
    for j in range(i + 1, len(fmt_dates)):
      print(fmt_dates[j])
      if fmt_dates[i] > fmt_dates[j] and fmt_dates[i] not in latest_date:
        latest_date.clear()
        latest_date.append(fmt_dates[i])