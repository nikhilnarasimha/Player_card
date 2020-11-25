# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:07:23 2020

@author: NIKHIL NARASIMHA
"""
import pandas as pd

import requests

from bs4 import BeautifulSoup

import json
base_url = input("first url:")
last_url = input("second url:")
n = input("No. of Pages :")

#base_url = "https://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;page="
#last_url = ";template=results;type=batting;view=innings"
l = []

print("Scrapping Started")

for i in range(1, n):
    try:
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
    except:
        pass

df = pd.DataFrame(l)

print(df.shape)

print("Pre Processing data")

#Batsmen country
Country_code = json.load( open( "country_code.json" ) )
country_code = pd.read_excel("country_code.xlsx", index_col="Code")
df['Batsmen2'], df['Country'] = df['Batsmen'].str.split('(', 1).str
df['Country'], a = df['Country'].str.split(')', 1).str
del a
for i in df.index:
    try:
        df['Country'][i] = Country_code["Country"][df['Country'][i]]
    except:
        df['Country'][i] = "None"
#filiter

df = df[(df["Country"] == "South Africa") | (df["Country"] == "INDIA" ) | (df["Country"] == "Australia" ) | (df["Country"] == "West Indies" )
   | (df["Country"] == "New Zealand" ) | (df["Country"] == "England" )]


#OUT

df["OUT"] = 1

for i in df.index:
    met = df["Runs"][i].isnumeric()
    if met == True:
        df["OUT"][i] = 1
    else:
        df["OUT"][i] = 0


        
#Runs
df["Runs"] = df["Runs"].apply(lambda x: x.split("*",1)[0])

#Opp
df["opp"] = df["opp"].apply(lambda x: x.split(" ",1)[1])

#Year
df["date"] = pd.to_datetime(df["date"])
df["Year"] = df["date"].apply(lambda x: x.year)


#stadium
df["Stadium"] = 1
df["cont"] = 1
stadium = json.load( open( "stadium.json" ) )
cont = json.load( open( "cont.json" ) )
for i in df.index:
    try:
        df["Stadium"][i] = stadium["Stadium"][df["ground"][i]]
    except:
        df["Stadium"][i] = "None"

for i in df.index:
    try:
        df["cont"][i] = cont["cont"][df["Stadium"][i]]
    except:
        df["cont"][i] = "None"

#100's , 50's, 30's 

df["100's"] = 1
df["50's"] = 1
df["30's"] = 1

for i in df.index:
    try:
        if int(df["Runs"][i]) > 100:
            df["100's"][i] = 1
        else :
            df["100's"][i] = 0
    except :
        df["100's"][i] = 0


for i in df.index:
    try:
        if int(df["Runs"][i]) > 50:
            df["50's"][i] = 1
        else :
            df["50's"][i] = 0
    except :
        df["50's"][i] = 0


for i in df.index:
    try:
        if int(df["Runs"][i]) > 30:
            df["30's"][i] = 1
        else :
            df["30's"][i] = 0
    except :
        df["30's"][i] = 0

df["Batsmen"] = df["Batsmen2"].astype(str)

df["Batsmen"] = df["Batsmen"].apply(lambda x: x.strip())

df["opp"] = df["opp"].apply(lambda x: x.strip())

df.drop(columns = ["Batsmen2", "dummy"], inplace = True)

print("CSV Saved")

df.to_csv("new_dataset.csv")

"""
import psycopg2

conn = psycopg2.connect(database = "d32gl7op7ncsq5", user = "susveekexpdauj",
                        password = "0d2414ccf42b143b02c85804f1ec87e1e98656c9cfbf414ec130f5467a8e8eb9", host = "ec2-54-166-251-173.compute-1.amazonaws.com", port = "5432")
print ("Opened database successfully")

mycursor = conn.cursor()

sql = "INSERT INTO Batsman (Batsmen,Country,Runs,OUT,Mins,Balls,fours,sixs,SR,inn,opp,ground,date,Year,cen,fif,thir,Stadium,cont) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"

count = 0

for i in df.index:
    try:
        sql = "INSERT INTO Batsman (Batsmen,Country,Runs,OUT,Mins,Balls,fours,sixs,SR,inn,opp,ground,date,Year,cen,fif,thir,Stadium,cont) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"
        batsmen = str(df["Batsmen"][i])
        Country = str(df["Country"][i])
        Runs = str(df["Runs"][i])
        OUT = int(df["OUT"][i])
        Mins = str(df["Mins"][i])
        Balls = str(df["Balls"][i])
        fours = int(df["4's"][i])
        sixs = int(df["6's"][i])
        SR = str(df["SR"][i])
        inn = str(df["inn"][i])
        opp = str(df["opp"][i])
        ground = str(df["ground"][i])
        date = str(df["date"][i])
        Year = int(df["Year"][i])
        cen = int(df["100's"][i])
        fif = int(df["50's"][i])
        thir = int(df["30's"][i])
        Stadium = str(df["Stadium"][i])
        cont = str(df["cont"][i])
        val = (batsmen, Country, Runs, OUT, Mins, Balls,fours,sixs,SR,inn,opp,ground,date,Year,cen,fif,thir,Stadium,cont)
        mycursor.execute(sql, val)
        conn.commit()
        count =  count +  mycursor.rowcount
        print(count, "record inserted.")
    except :
        pass

print(count, "Records Added in Total")

"""


try:
    import psycopg2
    import pandas.io.sql as psql
     
    # get connected to the database
    conn = psycopg2.connect(database = "d32gl7op7ncsq5", user = "susveekexpdauj",
                            password = "0d2414ccf42b143b02c85804f1ec87e1e98656c9cfbf414ec130f5467a8e8eb9", host = "ec2-54-166-251-173.compute-1.amazonaws.com", port = "5432",connect_timeout=1)
     
    df = psql.read_sql("SELECT * FROM batsman", conn)
except :
    df = pd.read_csv("batsmen_top.csv")
finally:
    if (conn):
            conn.close()




















