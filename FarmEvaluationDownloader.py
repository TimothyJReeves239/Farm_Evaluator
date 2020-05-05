import requests
from lxml import html
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from FarmEvalSecrets import cookie, agent

ur = "https://www.landandfarm.com/search/New-York-land-for-sale/?PropertyTypeIDs=4&PropertyTypeIDs=10&CurrentPage="
cookies = {"cookie":cookie}
dflist = []
for v in range(15):
    url = ur
    url = ur+str(v+1)
    page = requests.get(url, headers = agent, cookies = cookies).text
    tree = bs(page)
    temp = tree.find_all('div', class_="property-card--price")
    listoprices = []
    temp1 = tree.find_all('div', class_="property-card--quick-stats")
    listoacres = []
    temp2 = tree.find_all('div', class_="property-card--address")
    temp3 = tree.find_all('span', class_="addressflex")
    listocounties = []
    listozip = []
    #for x in temp3:
        #print(x.encode("utf-8", errors="ignore"))

    for x in temp3:
        listozip.append(x.text[-6:-1])

    for x in temp:
        if "$" in x.text:
            final = x.text.index(" ")
            listoprices.append(float((x.text[3:final]).replace(",", "")))
    for x in temp1:
        if "acres" in x.text:
            acres = x.text.index("acres")
            listoacres.append(float((x.text[1:acres]).replace(",", "")))
    for x in temp2:
        if "County" in x.text:
            start = x.text.index("(")
            end = x.text.index(")")

            listocounties.append(x.text[start+1:end-4])
    datalist = []
    for x in range(len(listoprices)):
        datalist.append([listoprices[x], listoacres[x], listocounties[x], listozip[x]])
    dflist.append((pd.DataFrame(datalist, columns = ["Price $", "Acres", "County", "Zip"])))
df = pd.concat(dflist).reset_index(drop=True)
df.to_csv("/Users/timreeves/Desktop/FarmEvaluator/data1.csv")
