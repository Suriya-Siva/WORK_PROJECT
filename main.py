
import requests
from bs4 import BeautifulSoup
import smtplib
import pandas as pd



headers = {
    "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

URL ="https://software.cisco.com/download/home/286289286/type/282487503/release/10.6.3?catid=278875243"

def ciscotest():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    version_info = soup.find_all('div', class_='row single-image-container')
    print(len(version_info))
    for i in version_info:
        print((soup.find('span', {'class':'pointer fileDescOuter'})).text)
        


    

    # price
    
    
ciscotest()