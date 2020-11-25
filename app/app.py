# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:30:47 2020

@author: malat
"""
import streamlit as st

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import random

import time

import psycopg2

#HTML
#background
page_bg_img = '''
<style>
body {
background-image: url("https://wallpaperaccess.com/full/1674687.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

#title
title_html = """<div><p style="text-align:center; color:GoldenRod; font-size:40px"><b>T-20 Batting Stats</b>.</p></div>"""
st.markdown(title_html, unsafe_allow_html = True)



#csv

df = pd.read_csv("batsmen_top.csv")
print("Conneted to the csv")

#table Function

def bat_stats(ply,opp,year,stad):
    try :
        if opp == "All" and year == "All" and stad == "All":
            Mat = len(df[df["Batsmen"] == ply])
            runs_df = df[df["Batsmen"] == ply]
            runs_df = runs_df[(runs_df["Runs"] != "DNB") & (runs_df["Runs"] != 'sub') & (runs_df["Runs"] !='TDNB') & (runs_df["Runs"] !='absent')]
            runs_df["Runs"] = runs_df["Runs"].astype(int)
            runs_df["6's"] = runs_df["6's"].astype(int)
            runs_df["4's"] = runs_df["4's"].astype(int)
            runs_df["Balls"] = runs_df["Balls"].astype(int)
            runs_df["100's"] = runs_df["100's"].astype(int)
            runs_df["50's"] = runs_df["50's"].astype(int)
            runs_df["30's"] = runs_df["30's"].astype(int)
            runs = runs_df["Runs"].sum()
            Avg = round(runs_df["Runs"].sum()/runs_df["OUT"].sum(),2)
            if Avg == float('inf'):
                Avg = runs_df["Runs"].sum()*2
            else :
                Avg = round(runs_df["Runs"].sum()/runs_df["OUT"].sum(),2)
            sr = round((runs_df["Runs"].sum()/runs_df["Balls"].astype(float).sum())*100,2)
            review = runs_df[runs_df["Runs"] == runs_df["Runs"].max()]["OUT"]
            review.reset_index(inplace=True, drop=True)
            if review[0] == 0:
                hs = str(runs_df["Runs"].max()) + "*"
            else:
                hs = runs_df["Runs"].max()
            no = len(runs_df) - len(runs_df[runs_df["OUT"] == 1])
            four =  runs_df["4's"].astype(int).sum()
            six =  runs_df["6's"].astype(int).sum()
            cen = runs_df["100's"].sum()
            fif = runs_df["50's"].sum()
            thr = runs_df["30's"].sum()
            runs_df["date"] = pd.to_datetime(runs_df["date"])
            date = runs_df["date"].min()
            date = str(date.day) + " " + date.strftime("%b") + " " + str(date.year)
            return Mat, runs, Avg, sr, hs, no, four, six,cen, fif, thr, date, runs_df
        elif opp != "All" and year == "All" and stad == "All":
            runs_df = df[df["Batsmen"] == ply]
            runs_df = runs_df[runs_df["opp"] == opp]
            Mat = len(runs_df)
            runs_df = runs_df[(runs_df["Runs"] != "DNB") & (runs_df["Runs"] != 'sub') & (runs_df["Runs"] !='TDNB') & (runs_df["Runs"] !='absent')]
            runs_df["Runs"] = runs_df["Runs"].astype(int)
            runs_df["6's"] = runs_df["6's"].astype(int)
            runs_df["4's"] = runs_df["4's"].astype(int)
            runs_df["Balls"] = runs_df["Balls"].astype(int)
            runs = runs_df["Runs"].sum()
            Avg = round(runs_df["Runs"].sum()/runs_df["OUT"].sum(),2)
            if Avg == float('inf'):
                Avg = runs_df["Runs"].sum()*2
            else :
                Avg = round(runs_df["Runs"].sum()/runs_df["OUT"].sum(),2)
            sr = round((runs_df["Runs"].sum()/runs_df["Balls"].astype(float).sum())*100,2)
            review = runs_df[runs_df["Runs"] == runs_df["Runs"].max()]["OUT"]
            review.reset_index(inplace=True, drop=True)
            if review[0] == 0:
                hs = str(runs_df["Runs"].max()) + "*"
            else:
                hs = runs_df["Runs"].max()
            no = len(runs_df) - len(runs_df[runs_df["OUT"] == 1])
            four =  runs_df["4's"].astype(int).sum()
            six =  runs_df["6's"].astype(int).sum()
            cen = runs_df["100's"].sum()
            fif = runs_df["50's"].sum()
            thr = runs_df["30's"].sum()
            runs_df["date"] = pd.to_datetime(runs_df["date"])
            date = runs_df["date"].min()
            date = str(date.day) + " " + date.strftime("%b") + " " + str(date.year)
            return Mat, runs, Avg, sr, hs, no, four, six,cen, fif, thr, date, runs_df
        else :
            runs_df = df[df["Batsmen"] == ply]
            if opp == "All":
                pass
            else :
                runs_df = runs_df[runs_df["opp"] == opp]
            if year == "All":
                pass
            else :
                runs_df = runs_df[runs_df["Year"] == year]
            if stad == "All":
                pass
            else :
                runs_df = runs_df[runs_df["Stadium"] == stad]
            Mat = len(runs_df)
            runs_df = runs_df[(runs_df["Runs"] != "DNB") & (runs_df["Runs"] != 'sub') & (runs_df["Runs"] !='TDNB') & (runs_df["Runs"] !='absent')]
            runs_df["Runs"] = runs_df["Runs"].astype(int)
            runs_df["6's"] = runs_df["6's"].astype(int)
            runs_df["4's"] = runs_df["4's"].astype(int)
            runs_df["Balls"] = runs_df["Balls"].astype(int)
            runs = runs_df["Runs"].sum()
            Avg = round(runs_df["Runs"].sum()/runs_df["OUT"].sum(),2)
            if Avg == float('inf'):
                Avg = runs_df["Runs"].sum()*2
            else :
                Avg = round(runs_df["Runs"].sum()/runs_df["OUT"].sum(),2)
            sr = round((runs_df["Runs"].sum()/runs_df["Balls"].astype(float).sum())*100,2)
            review = runs_df[runs_df["Runs"] == runs_df["Runs"].max()]["OUT"]
            review.reset_index(inplace=True, drop=True)
            if review[0] == 0:
                hs = str(runs_df["Runs"].max()) + "*"
            else:
                hs = runs_df["Runs"].max()
            no = len(runs_df) - len(runs_df[runs_df["OUT"] == 1])
            four =  runs_df["4's"].astype(int).sum()
            six =  runs_df["6's"].astype(int).sum()
            cen = runs_df["100's"].sum()
            fif = runs_df["50's"].sum()
            thr = runs_df["30's"].sum()
            runs_df["date"] = pd.to_datetime(runs_df["date"])
            date = runs_df["date"].min()
            date = str(date.day) + " " + date.strftime("%b") + " " + str(date.year)
            return Mat, runs, Avg, sr, hs, no, four, six,cen, fif, thr, date, runs_df
    except:
        Mat = 0
        runs = 0
        Avg = 0
        sr =0
        hs =0
        no = 0
        four =0
        six =0
        cen =0
        fif =0
        thr =0
        date = 0
        runs_df["Runs"] = 0
        runs_df["Balls"] = 0
        runs_df["4's"] = 0
        runs_df["6's"] = 0
        runs_df["SR"] = 0
        runs_df["OUT"] = 0
        runs_df["inn"] = 0
        runs_df["100's"] = 0
        runs_df["50's"] = 0
        runs_df["30's"] = 0
        return Mat, runs, Avg, sr, hs, no, four, six,cen, fif, thr, date, runs_df
     


    
def recorder(player,Opponents,years,stad):
    localtime = time.asctime( time.localtime(time.time()))
    conn = psycopg2.connect(database = "d4p1j3ph7ovdpj", user = "ncanedrmvoiwrt",
                        password = "b57d5188229f2a87e436a3185fb69631b1c0d479ce8df57a16d64a4c1d101213", host = "ec2-23-20-205-19.compute-1.amazonaws.com", port = "5432",connect_timeout=5)
    mycursor = conn.cursor()

    sql = "INSERT INTO record (Player,Opponents,years,stad,time)VALUES (%s, %s, %s, %s,%s)"
    val = (player,Opponents,years,stad,localtime)
    mycursor.execute(sql, val)
    conn.commit()
    conn.close()
    

select_player = df["Batsmen"].unique().tolist()


#selection
player = st.sidebar.selectbox("Select batmen", select_player)

#option seelction
def options(ply):
    runs_df = df[df["Batsmen"] == ply]
    opp = runs_df["opp"].unique().tolist()
    opp.insert(0,"All")
    year = runs_df["Year"].unique().tolist()
    year.sort(reverse = True)
    year.insert(0, "All")
    sta = runs_df["Stadium"].unique().tolist()
    sta.insert(0, "All")
    return opp, year, sta

opp,year, sta  = options(player)



Opponents = st.sidebar.selectbox("Opponents", opp)
years = st.sidebar.selectbox("Year", year)
stad = st.sidebar.selectbox("Stadiums", sta)

st.sidebar.subheader("Visualization")


#selection
metrics = st.sidebar.selectbox("Select the Metrics(to plot on graph)", ("Runs", "Average", "Strike rate", "Not Out's" , "Matches", "Sixers", "Fours"))

#update
space = st.sidebar.title("  ")
update_key = st.sidebar.text_input("Key (ignore this is for internal propuse)",type="password")


st.title(player)

#generator
Mat, runs, Avg, sr, hs, no, four, six,cen, fif, thr, date, runs_df = bat_stats(player,Opponents,years,stad)



#table Html
html_url = """
<table style="width:100%;">
<tr style="color:Orange; font-size:20px">
<th>
Total Runs
</th>
<th>
Macthes
</th>
<th>
Average
</th>
</tr>
  <tr style= "font-size:20px">
    <td><b>{runs}</b></td>
    <td><b>{mat}</b></td>
    <td><b>{Avg}</b></td>
  </tr>
  <br>
  <tr style="color:Orange; font-size:20px">
<th>
Highest Score
</th>
<th>
Strike Rate
</th>
<th>
Not Out's
</th>
</tr>
  <tr style= "font-size:20px">
    <td><b>{hs}</b></td>
    <td><b>{sr}</b></td>
    <td><b>{no}</b></td>
  </tr>
  <br>
  <tr style="color:Orange; font-size:20px">
<th>
100's & 100+ 
</th>
<th>
50's & 50+
</th>
<th>
30's & 30+
</th>
</tr>
  <tr style= "font-size:20px">
    <td><b>{cen}</b></td>
    <td><b>{fif}</b></td>
    <td><b>{thr}</b></td>
  </tr>
  <br>
  <tr style="color:Orange; font-size:20px">
<th>
4's 
</th>
<th>
6's
</th>
<th>
Debut
</th>
</tr>
  <tr style= "font-size:20px">
    <td><b>{four}</b></td>
    <td><b>{six}</b></td>
    <td><b>{date}</b></td>
  </tr>
</table>
"""
html_url1 = html_url.format(runs = runs, mat = Mat, Avg = Avg, hs = hs, sr = sr, no = no, cen = cen, fif = fif, thr = thr, four = four, six= six, date = date )
st.markdown(html_url1, unsafe_allow_html = True)

st.title(" ")


#Bar Gragh Function
def Barchart(metrics):
    try:
        if metrics == "Runs":
            st.header("Country-wise Runs Scored")
            new_df = runs_df.groupby("opp").sum()
            fig = px.bar(df, y=new_df["Runs"], x=new_df.index, text=new_df["Runs"],labels={'y':'Runs Scored by Batsman','x' : 'Opponent', 'text' : 'Runs'},height=500)
            fig.update_traces(texttemplate='%{text:.s}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            fig.update_traces(marker_color='blue')
            return fig
        elif metrics == "Matches":
            st.header("Country-wise Macthes Played")
            new_df = runs_df.groupby("opp").count()
            fig = px.bar(df, y=new_df["Runs"], x=new_df.index, text=new_df["Runs"],labels={'y':'Macthes Played by Batsman','x' : 'Opponent', 'text' : 'Macthes'},title="Country-wise Runs Scored ",height=500)
            fig.update_traces(texttemplate='%{text:.s}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            fig.update_traces(marker_color='blue')
            return fig
        elif metrics == "Strike rate":
            st.header("Country-wise Batsman Strike rate")
            new_df = runs_df.groupby("opp").sum()
            new_df["SR"] = (new_df["Runs"]/new_df["Balls"])*100
            fig = px.bar(df, y=new_df["SR"], x=new_df.index, text=new_df["SR"],labels={'y':'Batsman"s Srtike rate','x' : 'Opponent', 'text' : 'SR'},height=500)
            fig.update_traces(texttemplate='%{text:.4s}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            fig.update_traces(marker_color='red')
            return fig
        elif metrics == "Not Out's":
            st.header("Country-wise Not Outs")
            new_df2 = runs_df.groupby("opp").sum()
            new_df1 = runs_df.groupby("opp").count()
            new_df2["OUT"] = new_df1["OUT"] - new_df2["OUT"]
            new_df = new_df2
            fig = px.bar(new_df, y=new_df["OUT"], x=new_df.index, text=new_df["OUT"],hover_data=[new_df1["OUT"]],labels={'y':'No. of times the batsmen was Not outs','x' : 'Opponent', 'text' : 'Not Out','hover_data_0':'Macthes played',"OUT" : "Not Out"},height=500)
            fig.update_traces(texttemplate='%{text:.s}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            fig.update_traces(marker_color='green')
            return fig
        elif metrics == "Average":
            st.header("Country-wise Average")
            new_df = runs_df.groupby("opp").sum()
            new_df["avg"] = new_df["Runs"]/new_df["OUT"]
            for n, i in zip(new_df.index,new_df["avg"]):
                if i == float("inf"):
                    inf = new_df.loc[n]["Runs"]*2
                    new_df = new_df.replace(to_replace =[float("inf")],  
                                            value =inf)
            fig = px.bar(df, y=new_df["avg"], x=new_df.index, text=new_df["avg"],labels={'y':'Batsman"s Average','x' : 'Opponent', 'text' : 'AVG'},height=500)
            fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            fig.update_traces(marker_color='red')
            return fig
        elif metrics == "Sixers":
            st.header("Country-wise Sixers Scored")
            new_df = runs_df.groupby("opp").sum()
            fig = px.bar(df, y=new_df["6's"], x=new_df.index, text=new_df["6's"],labels={'y':'Sixers hit by Batsman','x' : 'Opponent', 'text' : 'Sixers'},height=500)
            fig.update_traces(texttemplate='%{text:.s}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            fig.update_traces(marker_color='blue')
            return fig
        elif metrics == "Fours":
            st.header("Country-wise Fours Scored")
            new_df = runs_df.groupby("opp").sum()
            fig = px.bar(df, y=new_df["4's"], x=new_df.index, text=new_df["4's"],labels={'y':'Fours hit by Batsman','x' : 'Opponent', 'text' : 'Fours'},height=500)
            fig.update_traces(texttemplate='%{text:.s}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            fig.update_traces(marker_color='blue')
            return fig
    except:
        animals=['No Macthes Played']
        fig = go.Figure(data=[
            go.Bar(x=animals, y=[0]),
        ])
        return fig
            
            

#Bar generator
bar_fig = Barchart(metrics)
st.plotly_chart(bar_fig)

st.title(" ")

#Line Chart
def Linechart(metrics):
        try: 
            if metrics == "Runs":
                st.header("Year-wise Runs Scored")
                new_df = runs_df.groupby("Year").sum()
                fig = px.line(df, y=new_df["Runs"], x=new_df.index, text=new_df["Runs"],labels={'y':'Runs Scored by Batsman','x' : 'Year', 'text' : 'Runs'})
                fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
                fig.update_traces(marker_color='blue')
                return fig
            elif metrics == "Matches":
                st.header("Year-wise Macthes Played")
                new_df = runs_df.groupby("Year").count()
                fig = px.line(df, y=new_df["Runs"], x=new_df.index, text=new_df["Runs"],labels={'y':'Macthes Played by Batsman','x' : 'Year', 'text' : 'Macthes'},title="Country-wise Runs Scored ",height=500)
                fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
                fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                fig.update_traces(marker_color='blue')
                return fig
            elif metrics == "Strike rate":
                st.header("Year-wise Batsman Strike rate")
                new_df = runs_df.groupby("Year").sum()
                new_df["SR"] = (new_df["Runs"]/new_df["Balls"])*100
                fig = px.line(df, y=new_df["SR"], x=new_df.index, text=new_df["SR"],labels={'y':'Batsman"s Strike rate','x' : 'Year', 'text' : 'SR'},title="Country-wise Runs Scored ",height=500)
                fig.update_traces(texttemplate='%{text:.4s}', textposition='top left')
                fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                fig.update_traces(marker_color='red')
                return fig
            elif metrics == "Not Out's":
                st.header("Year-wise Not Outs")
                new_df2 = runs_df.groupby("Year").sum()
                new_df1 = runs_df.groupby("Year").count()
                new_df2["OUT"] = new_df1["OUT"] - new_df2["OUT"]
                new_df = new_df2
                fig = px.line(new_df2, y=new_df["OUT"], x=new_df.index, text=new_df["OUT"],labels={'y':'No. of times the batsmen was Not outs',"OUT" : "Not Out",'x' : 'Year', 'text' : 'Not Out','hover_data_0':'Macthes played'},height=500, hover_data=[new_df1["OUT"]])
                fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
                fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                fig.update_traces(marker_color='green')
                return fig
            elif metrics == "Average":
                st.header("Year-wise Average")
                new_df = runs_df.groupby("Year").sum()
                new_df["avg"] = new_df["Runs"]/new_df["OUT"]
                for n, i in zip(new_df.index,new_df["avg"]):
                    if i == float("inf"):
                        inf = new_df.loc[n]["Runs"]*2
                        new_df = new_df.replace(to_replace =[float("inf")],  
                                            value =inf)
                        
                fig = px.line(df, y=new_df["avg"], x=new_df.index, text=new_df["avg"],labels={'y':'Batsman"s Average','x' : 'Year', 'text' : 'AVG'},height=500)
                fig.update_traces(texttemplate='%{text:.3s}', textposition='top left')
                fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                fig.update_traces(marker_color='red')
                return fig
            elif metrics == "Sixers":
                st.header("Year-wise Sixers Scored")
                new_df = runs_df.groupby("Year").sum()
                fig = px.line(df, y=new_df["6's"], x=new_df.index, text=new_df["6's"],labels={'y':'Sixers hit by Batsman','x' : 'Year', 'text' : 'Sixers'},height=500)
                fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
                fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                fig.update_traces(marker_color='blue')
        
                return fig
            elif metrics == "Fours":
                st.header("Year-wise Fours Scored")
                new_df = runs_df.groupby("Year").sum()
                fig = px.line(df, y=new_df["4's"], x=new_df.index, text=new_df["4's"],labels={'y':'Fous hit by Batsman','x' : 'Year', 'text' : 'Fours'},height=500)
                fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
                fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                fig.update_traces(marker_color='blue')
                return fig
        except:
            animals=['No Macthes Played']
            fig = go.Figure(data=[
            go.Bar(x=animals, y=[0]),
                ])
            return fig


#line generator
line_fig = Linechart(metrics)
st.plotly_chart(line_fig)


#tree map function
def treemap(metrics):
    try:
        if metrics == "Runs":
            st.header("Stadium-wise Runs Scored")
            new_df = runs_df.groupby(["ground","Stadium","cont"]).sum()
            new_df.reset_index(level=0, inplace=True)
            new_df.reset_index(level=0, inplace=True)
            new_df.reset_index(level=0, inplace=True)
            
            fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground'],
                             labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values='Runs',color = 'Stadium', height=600,width= 700)
            fig.data[0].textinfo = 'label+text'
            fig.data[0].hovertemplate = '%{label}<br>Runs = %{value}'
            fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
            return fig
        elif metrics == "Matches":
            st.header("Stadium-wise Macthes Played")
            new_df = runs_df.groupby(["ground","Stadium","cont"]).count()
            new_df.reset_index(level=0, inplace=True)
            new_df.reset_index(level=0, inplace=True)
            new_df.reset_index(level=0, inplace=True)
            
            fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground']
                             , values='Runs',color = 'Stadium', height=600,width= 700)
            fig.data[0].textinfo = 'label+text'
            fig.data[0].hovertemplate = '%{label}<br>Matches = %{value}'
            fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
            return fig
        elif metrics == "Not Out's":
             st.header("Stadium-wise Not Outs")    
             new_df2 = runs_df.groupby(["Stadium"]).count()
             new_df1 = runs_df.groupby(["Stadium"]).sum()
             new_df2["OUT"] = new_df2["OUT"] - new_df1["OUT"]
             new_df = new_df2
             new_df.reset_index(level=0, inplace=True)
             fig = px.treemap(new_df, path=[px.Constant('world'), 'Stadium'],
                             labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values='OUT', height=600,width= 700)
             fig.data[0].textinfo = 'label+text'
             fig.data[0].hovertemplate = '%{label}<br>Not Outs = %{value}'
             fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
             return fig
        elif metrics == "Average":
             st.header("Stadium-wise Average")
             new_df = runs_df.groupby("Stadium").sum()
             new_df["avg"] = new_df["Runs"]/new_df["OUT"]
             for n, i in zip(new_df.index,new_df["avg"]):
                 if i == float("inf"):
                     inf = new_df.loc[n]["Runs"]*2
                     new_df = new_df.replace(to_replace =[float("inf")],  
                                        value =inf)
             new_df.reset_index(level=0, inplace=True)        
             fig = px.treemap(new_df, path=[px.Constant('world'), 'Stadium'],
                             labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values="avg",color = 'Stadium', height=600,width= 700)
             fig.data[0].textinfo = 'label+text'
             fig.data[0].hovertemplate = '%{label}<br>Avg = %{value:.4s}'
             fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
             return fig
        elif metrics == "Sixers":
             st.header("Stadium-wise Sixers Scored")
             new_df = runs_df.groupby(["ground","Stadium","cont"]).sum()
             new_df.reset_index(level=0, inplace=True)
             new_df.reset_index(level=0, inplace=True)
             new_df.reset_index(level=0, inplace=True)
            
             fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground'],
                             labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values="6's",color = 'Stadium', height=600,width= 700)
             fig.data[0].textinfo = 'label+text'
             fig.data[0].hovertemplate = '%{label}<br>Sixs = %{value}'
             fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
             return fig
        elif metrics == "Strike rate":
            st.header("Stadium-wise Batsman Strike rate")
            new_df = runs_df.groupby(["Stadium"]).sum()
            new_df["SR"] = (new_df["Runs"]/new_df["Balls"])*100
            new_df.reset_index(level=0, inplace=True)
            new_df.reset_index(level=0, inplace=True)
            new_df.reset_index(level=0, inplace=True)
          
            fig = px.treemap(new_df, path=['Stadium'],
                           labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values="SR",color = 'Stadium', height=600,width= 700)
            fig.data[0].textinfo = 'label+text'
            fig.data[0].hovertemplate = '%{label}<br>SR = %{value:.4s}'
            fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
            return fig
        elif metrics == "Fours":
             st.header("Stadium-wise Fours Scored")
             new_df = runs_df.groupby(["ground","Stadium","cont"]).sum()
             new_df.reset_index(level=0, inplace=True)
             new_df.reset_index(level=0, inplace=True)
             new_df.reset_index(level=0, inplace=True)
            
             fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground'],
                             labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values="4's",color = 'Stadium', height=600,width= 700)
             fig.data[0].textinfo = 'label+text'
             fig.data[0].hovertemplate = '%{label}<br>Fours = %{value}'
             fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
             return fig
    except:  
        animals=['No Macthes Played']
        fig = go.Figure(data=[
        go.Bar(x=animals, y=[0]),])
        return fig   

#tree map
tree_fig = treemap(metrics)
st.plotly_chart(tree_fig)


refresh_html = """<meta http-equiv="refresh" content="3">"""


#Update Key

if update_key:
    if update_key == "Nikhil_update":
        import psycopg2
        import pandas.io.sql as psql
        conn = psycopg2.connect(database = "d32gl7op7ncsq5", user = "susveekexpdauj",
                            password = "0d2414ccf42b143b02c85804f1ec87e1e98656c9cfbf414ec130f5467a8e8eb9", host = "ec2-54-166-251-173.compute-1.amazonaws.com", port = "5432",connect_timeout=5)    
        df_update = psql.read_sql("SELECT * FROM batsman", conn)
        df_update.to_csv("batsmen_top.csv")
        st.sidebar.success("success")
        st.markdown(refresh_html, unsafe_allow_html = True)
    else :
        st.sidebar.warning("Failed")
else:
    pass



#DYK
def DYK():
    list_sen = []
    #last match_date
    ply = runs_df["Batsmen"].unique().tolist()[0]
    runs_df["date"] = pd.to_datetime(runs_df["date"])
    date = runs_df["date"].max()
    g_in= runs_df[runs_df["date"] == date].index
    g_in = g_in[0]
    grou= runs_df[runs_df["date"] == date]["ground"][g_in]
    date = str(date.day) + " " + date.strftime("%B") + " " + str(date.year)
    lm = '{ply} played his last match on {date} in {grou}'
    lm = lm.format(date = date, ply = ply, grou = grou)
    list_sen.append(lm)
    
    
    #last match_stadium
    ply = runs_df["Batsmen"].unique().tolist()[0]
    runs_df["date"] = pd.to_datetime(runs_df["date"])
    date = runs_df["date"].max()
    g_in= runs_df[runs_df["date"] == date].index
    g_in = g_in[0]
    grou= runs_df[runs_df["date"] == date]["Stadium"][g_in]
    con= runs_df[runs_df["date"] == date]["opp"][g_in]
    lm_s = '{ply} played his last match aganist {con} in {grou}'
    lm_s = lm_s.format(con = con, ply = ply, grou = grou)
    list_sen.append(lm_s)
    
    
    
    #last 5 matches - SR_d
    runs_df_5 = runs_df.sort_values(by='date', ascending=False)
    runs_df_5 = runs_df_5.head()
    SR_d = round((runs_df_5["Runs"].sum()/runs_df_5["Balls"].sum())*100,2)
    text_SR = '{ply} Strike rate was {SR_d} in his last five matches'
    text_SR = text_SR.format(SR_d = SR_d, ply = ply)
    list_sen.append(text_SR)
    
    
    
    #last 5 matches - Avg_d
    runs_df_5 = runs_df.sort_values(by='date', ascending=False)
    runs_df_5 = runs_df_5.head()
    avg_d = runs_df_5["Runs"].sum()/runs_df_5["OUT"].sum()
    if avg_d == float("inf"):
        avg_d = round(runs_df_5["Runs"].sum()*2,2)
    else :
        avg_d = round(runs_df_5["Runs"].sum()/runs_df_5["OUT"].sum(),2)
    text_AVG = '{ply}"s average was {avg_d} in his last five matches'
    text_AVG = text_AVG.format(ply = ply, avg_d = avg_d)
    list_sen.append(text_AVG)
    
    #last 5 matches - Runs_d
    runs_df_5 = runs_df.sort_values(by='date', ascending=False)
    runs_df_5 = runs_df_5.head()
    runs_d = runs_df_5["Runs"].sum()
    text_runs = '{ply} has scored  {runs_d}  runs in his last five matches'
    text_runs = text_runs.format(ply = ply, runs_d = runs_d)
    list_sen.append(text_runs)
    
    
    
    #Runs percentage_max
    runs_c = runs_df.groupby("Stadium").sum()
    stad_d = runs_c[runs_c["Runs"] == runs_c["Runs"].max()].index[0]
    per = int(round(runs_c["Runs"].max()/runs_c["Runs"].sum()*100))
    text_per = "{ply} has scorced more than {per}% of his Total Carrer runs in {stad_d} Picthes"
    text_per = text_per.format(ply = ply, per = per, stad_d = stad_d)
    list_sen.append(text_per)
    
    #run's Percentage_min
    runs_c = runs_df.groupby("Stadium").sum()
    stad_d = runs_c[runs_c["Runs"] == runs_c["Runs"].min()].index[0]
    per = int(round(runs_c["Runs"].min()/runs_c["Runs"].sum()*100))
    if per == 0:
        per = 1
    text_per_min = "{ply} has scorced Only {per}% of his Total Carrer runs in {stad_d} Picthes"
    text_per_min = text_per_min.format(ply = ply, per = per, stad_d = stad_d)
    list_sen.append(text_per_min)
    
    #played aganist teams
    runs_m = runs_df.groupby("opp").count()
    nteams = runs_df["opp"].nunique()
    text_opp = "{ply} has played {nteams} different Oppenents in his whole career."
    text_opp = text_opp.format(ply = ply, nteams = nteams)
    list_sen.append(text_opp)
    
    
    #6's AVG
    six_count = int(round((runs_df["6's"].sum()/runs_df["Balls"].sum())*20))
    text_sixs = '{ply} hits {six_count} Sixs in every 20 Balls he plays'
    text_sixs = text_sixs.format(ply = ply, six_count = six_count)
    list_sen.append(text_sixs)
    
    #4's AVG
    per = int(round((runs_df["4's"].sum()/runs_df["Balls"].sum())*20))
    ply.split()[1]
    text_fours = "{ply} will hit {per} Fours in every 20 Balls he plays"
    text_fours = text_fours.format(ply = ply.split()[1], per = per)
    list_sen.append(text_fours)
    sentenses = random.sample(list_sen,3)
    

    #first match score
    ply = runs_df["Batsmen"].unique().tolist()[0]
    runs_df["date"] = pd.to_datetime(runs_df["date"])
    date = runs_df["date"].min()
    g_in= runs_df[runs_df["date"] == date].index
    g_in = g_in[0]
    runs_f= runs_df[runs_df["date"] == date]["Runs"][g_in]
    date = str(date.day) + " " + date.strftime("%B") + " " + str(date.year)
    fm_s = '{ply} has Scored {runs_f} in his first Every T20I'
    fm_s = fm_s.format(ply = ply, runs_f = runs_f)
    list_sen.append(fm_s)
    return sentenses



#table for DYK
html_url_dyk = """
<h2><b>Do You Know</b></h2>
<body style="background-image: url('https://image.shutterstock.com/image-photo/white-background-paper-show-patterns-260nw-255421642.jpg');">	
      <ul type = "disc">
         <li style="font-size:25px">{sen1}</li>
         <li style="font-size:25px">{sen2}</li>
         <li style="font-size:25px">{sen3}</li>
      </ul>
</body>"""

#formatting
sentenses = DYK()
html_url_dyk = html_url_dyk.format(sen1 = sentenses[0],sen2 = sentenses[1],sen3 = sentenses[2])
st.markdown(html_url_dyk, unsafe_allow_html = True)

#recoder
try:
    recorder(player, Opponents, years, stad)
    print("Record Inserted")
except:
    pass


#Disclaimer
st.markdown("*Country-wise data was plotted on Bar Chart , Year-wise data was plotted on Line Chart, Stadium - Wise data was plotted on Area Chart. - Thank you 'Nikhil Narasimha'")














