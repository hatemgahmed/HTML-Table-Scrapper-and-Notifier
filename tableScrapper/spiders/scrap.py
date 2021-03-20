
import scrapy
from bs4 import BeautifulSoup
import pandas as pd
import shelve
import os
import Notification
import json

def scrapHTML(html):
    soup=BeautifulSoup(html,"html.parser")
    tableRows=soup.find_all("tr")
    # print(tableRows[1])
    dataframe=[]
    # [1:]
    tableRows=tableRows[1:]
    for tr in tableRows:
        # print(tr)
        # print('_'*100)
        td=tr.find_all("td")
        row = [cell.text for cell in td]
        dataframe.append(row)
    return dataframe
param1 = []
param2 = []
filename=''
cols=[]
with open("scraper_parameters.json",'r') as file:
    parameters=json.loads(file.read())
    param1 = parameters["allowed_domains"]
    param2 = parameters["start_urls"]
    filename = parameters["filename"]
    cols = parameters["cols"]
class ScrapSpider(scrapy.Spider):
    name = 'scrap'
    allowed_domains = param1
    start_urls = param2


    def parse(self, response):
        # pass
        print('_'*100)
        f=shelve.open("Query_Length")
        scrapped=scrapHTML(response.body)
        if not 'length' in f.keys():
            # Initialize the query length
            f['length']=-1
        change=f['length']-len(scrapped)
        if change!=0:
            print("Change Happened!!!")
            # Update
            dataframe = pd.DataFrame(scrapped, columns=cols)
            f['data']= dataframe
            dataframe.to_csv(os.path.join('Data', filename + '.csv'))
        else:
            print("No Change")
        f.close()
        print('_'*100)
        # print(response.body)