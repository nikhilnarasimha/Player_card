# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:35:09 2020

@author: malat
"""
import pandas as pd

import requests

from bs4 import BeautifulSoup

#batting 

for i in range(1, 485):
    link = base_url+str(i)+last_url
    res = requests.get(link)
    c = res.content
    soup = BeautifulSoup(c,"html.parser")
    all = soup.find_all("tr",{"class":"data1"})
    for player in all:
        d = {}
        d["Batsmen"] = (player.find_all("td")[0].text)
        d["Runs"] = (player.find_all("td")[1].text)
        d["Mins"] = (player.find_all("td")[2].text)
        d["Balls"] = (player.find_all("td")[3].text)
        d["4's"] = (player.find_all("td")[4].text)
        d["6's"] = (player.find_all("td")[5].text)
        d["SR"] = (player.find_all("td")[6].text)
        d["inn"] = (player.find_all("td")[7].text)
        d["opp"] = (player.find_all("td")[9].text)
        d["ground"] = (player.find_all("td")[10].text)
        d["date"] = (player.find_all("td")[11].text)
        d["dummy"] = (player.find_all("td")[8].text)
        l.append(d)


df = pd.DataFrame(l)
df



#blowing

base_url = "https://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;home_or_away=1;home_or_away=2;home_or_away=3;page="
last_url = ";result=1;result=2;result=3;result=5;template=results;type=bowling;view=innings"

l = []
for i in range(1, 485):
    link = base_url+str(i)+last_url
    res = requests.get(link)
    c = res.content
    soup = BeautifulSoup(c,"html.parser")
    all = soup.find_all("tr",{"class":"data1"})
    for player in all:
        d = {}
        d["Blower"] = (player.find_all("td")[0].text)
        d["Overs"] = (player.find_all("td")[1].text)
        d["mds"] = (player.find_all("td")[2].text)
        d["Runs"] = (player.find_all("td")[3].text)
        d["Wkts"] = (player.find_all("td")[4].text)
        d["Econ"] = (player.find_all("td")[5].text)
        d["Inns"] = (player.find_all("td")[6].text)
        d["opp"] = (player.find_all("td")[8].text)
        d["ground"] = (player.find_all("td")[9].text)
        d["date"] = (player.find_all("td")[10].text)
        l.append(d)

df = pd.DataFrame(l)
df

df.to_csv("blower_data.csv")

