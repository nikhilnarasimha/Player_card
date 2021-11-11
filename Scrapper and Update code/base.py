# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:43:08 2020

@author: NIkhil Narasimha
"""
import seaborn as sns

import matplotlib.pyplot as plt

import pandas as pd

from bokeh.plotting import figure

df = pd.read_csv("batsmen_top.csv")

df.dtypes

df["opp"].unique()

df["Batsmen"] = df["Batsmen"].astype(str)

df["Batsmen"] = df["Batsmen"].apply(lambda x: x.strip())

df["opp"] = df["opp"].apply(lambda x: x.strip())

df.to_csv("aa.csv")




#Matches
len(df[df["Batsmen"] == "KL Rahul"])

#runs
runs_df = df[df["Batsmen"] == "KL Rahul"]

runs_df = runs_df[(runs_df["Runs"] != "DNB") & (runs_df["Runs"] != 'sub')& (runs_df["Runs"] !='TDNB')& (runs_df["Runs"] !='absent')]

runs_df["Runs"] = runs_df["Runs"].astype(int)
runs_df["6's"] = runs_df["6's"].astype(int)
runs_df["4's"] = runs_df["4's"].astype(int)
runs_df["Balls"] = runs_df["Balls"].astype(int)
runs_df["Runs"].sum()

#Average
avg = runs_df["Runs"].sum()/runs_df["OUT"].sum()
if avg == float(avg):
    avg = runs_df["Runs"].sum()*2
else :
    avg = runs_df["Runs"].sum()/runs_df["OUT"].sum()
    
 
#Strike Rate
(runs_df["Runs"].sum()/runs_df["Balls"].astype(float).sum())*100

#highest Score
review = runs_df[runs_df["Runs"] == runs_df["Runs"].max()]["OUT"]
review.reset_index(inplace=True, drop=True)
if review[0] == 1:
    hs = str(runs_df["Runs"].max()) + "*"
else:
    hs = runs_df["Runs"].max()

#Not OUTs

len(runs_df) - len(runs_df[runs_df["OUT"] == 1])

#No of 4's
runs_df["4's"].astype(int).sum()


#No of 6's
runs_df["6's"].astype(int).sum()

#No. of 100, 100+ score
runs_df["100's"].sum()

#No. of 50, 50+ score
runs_df["50's"].sum()

#No. of 30, 30+ score
runs_df["30's"].sum()

#debut match
runs_df["date"] = pd.to_datetime(runs_df["date"])
date = runs_df["date"].min()
date = str(date.day) + " " + date.strftime("%B") + " " + str(date.year)



opp = runs_df["opp"].to_list()
runs = runs_df["Runs"].to_list()

# Initializing the plot
p = figure( plot_height=300, 
           title="Measles in the USA 2000-2015",
          tools=TOOLS)
#Plotting
p.vbar(opp,                            #categories
      top = runs,                      #bar heights
       width = .9,
       fill_alpha = .5,
       fill_color = 'salmon',
       line_alpha = .5,
       line_color='green',
       line_dash='dashed'
      
  )
#Signing the axis
p.xaxis.axis_label="Years"
p.yaxis.axis_label="Measles stats"
show(p)

import pandas as pd
from bokeh.charts import Bar
from bokeh.io import output_notebook, show
from bokeh.charts import Bar, output_file, show
output_notebook()
dict = {'values': {u'A': 10, u'B': 20}}
dff = runs_df[["Runs", "opp",]]
df['label'] = df.index
dff
p = Bar(df, values='values',label='label')
show(p)

from bokeh.plotting import figure, output_file, show
output_file("gfg.html")
graph = figure(title = "Bokeh Vertical Bar Graph")    
# x-coordinates to be plotted 
x = [1, 2, 3, 4, 5] 
   
# x-coordinates of the top edges 
top = [1, 2, 3, 4, 5] 
   
# width / thickness of the bars  
width = 0.5
   
# plotting the graph 
graph.vbar(runs, 
           top = opp , 
           width = width) 
   
# displaying the model 
show(graph) 


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

#Grpahs
runs_df = runs_df.groupby("opp").sum()





#Runs

new_df = runs_df.groupby("opp").sum()
fig = px.bar(df, y=new_df["Runs"], x=new_df.index, text=new_df["Runs"],labels={'y':'Runs Scored by Batsman','x' : 'Opponent', 'text' : 'Runs'},height=500)
fig.update_traces(texttemplate='%{text:.s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='blue')


st.plotly_chart(fig)

#Matches

new_df = runs_df.groupby("opp").count()
fig = px.bar(df, y=new_df["Runs"], x=new_df.index, text=new_df["Runs"],labels={'y':'Macthes Played by Batsman','x' : 'Opponent', 'text' : 'Macthes'},title="Country-wise Runs Scored ",height=500)
fig.update_traces(texttemplate='%{text:.s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='blue')


#Not outs

new_df2 = runs_df.groupby("opp").sum()
new_df1 = runs_df.groupby("opp").count()
new_df2["OUT"] = new_df2["OUT"] - new_df1["OUT"]
fig = px.bar(new_df, y=new_df["OUT"], x=new_df.index, text=new_df["OUT"],labels={'y':'No. of times the batsmen was Not outs','x' : 'Opponent', 'text' : 'Not Out'},height=500, hover_data=[new_df1["OUT"]])
fig.update_traces(texttemplate='%{text:.s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='green')

#6,s
new_df = runs_df.groupby("opp").sum()
fig = px.bar(df, y=new_df["6's"], x=new_df.index, text=new_df["6's"],labels={'y':'Sixers hit by Batsman','x' : 'Opponent', 'text' : 'Sixers'},height=500)
fig.update_traces(texttemplate='%{text:.s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='blue')


#4's
new_df = runs_df.groupby("opp").sum()
fig = px.bar(df, y=new_df["4's"], x=new_df.index, text=new_df["4's"],labels={'y':'Fous hit by Batsman','x' : 'Opponent', 'text' : 'Fours'},height=500)
fig.update_traces(texttemplate='%{text:.s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='blue')


#avg
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

#SR
new_df = runs_df.groupby("opp").sum()
new_df["SR"] = new_df["Runs"]/new_df["Balls"]
fig = px.bar(df, y=new_df["SR"], x=new_df.index, text=new_df["SR"],labels={'y':'Batsman"s Srtike rate','x' : 'Opponent', 'text' : 'SR'},height=500)
fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='red')

#Line Chart
#runs
new_df = runs_df.groupby("Year").sum()
fig = px.line(df, y=new_df["Runs"], x=new_df.index, text=new_df["Runs"],labels={'y':'Runs Scored by Batsman','x' : 'Year', 'text' : 'Runs'})
fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
fig.update_traces(marker_color='blue')

#Matches

new_df = runs_df.groupby("Year").count()
fig = px.line(df, y=new_df["Runs"], x=new_df.index, text=new_df["Runs"],labels={'y':'Macthes Played by Batsman','x' : 'Year', 'text' : 'Macthes'},title="Country-wise Runs Scored ",height=500)
fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='blue')

#Not outs

new_df2 = runs_df.groupby("Year").sum()
new_df1 = runs_df.groupby("Year").count()
new_df2["OUT"] = new_df2["OUT"] - new_df1["OUT"]
fig = px.line(new_df, y=new_df["OUT"], x=new_df.index, text=new_df["OUT"],labels={'y':'No. of times the batsmen was Not outs','x' : 'Year', 'text' : 'Not Out'},height=500, hover_data=[new_df1["OUT"]])
fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='green')

#6,s
new_df = runs_df.groupby("Year").sum()
fig = px.bar(df, y=new_df["6's"], x=new_df.index, text=new_df["6's"],labels={'y':'Sixers hit by Batsman','x' : 'Year', 'text' : 'Sixers'},height=500)
fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='blue')


#4's
new_df = runs_df.groupby("Year").sum()
fig = px.bar(df, y=new_df["4's"], x=new_df.index, text=new_df["4's"],labels={'y':'Fous hit by Batsman','x' : 'Year', 'text' : 'Fours'},height=500)
fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='blue')


#avg
new_df = runs_df.groupby("Year").sum()
new_df["avg"] = new_df["Runs"]/new_df["OUT"]
for n, i in zip(new_df.index,new_df["avg"]):
    if i == float("inf"):
        inf = new_df.loc[n]["Runs"]*2
        new_df = new_df.replace(to_replace =[float("inf")],  
                            value =inf)
        
fig = px.bar(df, y=new_df["Year"], x=new_df.index, text=new_df["avg"],labels={'y':'Batsman"s Average','x' : 'Year', 'text' : 'AVG'},title="Country-wise Runs Scored ",height=500)
fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='red')

#SR
new_df = runs_df.groupby("Year").sum()
new_df["SR"] = new_df["Runs"]/new_df["Balls"]
fig = px.bar(df, y=new_df["SR"], x=new_df.index, text=new_df["SR"],labels={'y':'Batsman"s Strike rate','x' : 'Year', 'text' : 'SR'},title="Country-wise Runs Scored ",height=500)
fig.update_traces(texttemplate='%{text:.s}', textposition='top left')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_traces(marker_color='red')



from geopy.geocoders import Nominatim 

def geo(place):
    geolocator = Nominatim(user_agent = "geoapiExercises")
    location = geolocator.geocode(place) 
    return location


df["stad"] = df["ground"].apply(lambda x: geo(x))



geo('Bengaluru')

a = df1["stadium"][1]

df1["stad"] = "hi"


a.address.rsplit(",",1)[1]

df["ground"] = df["ground"].astype(str)

df1 = df1[df1["ground"] != "Mumbai (BS)" ]
df1 = df1[df1["ground"] != "Dubai (DSC)" ]
df1 = df1[df1["ground"] != "Tolerance Oval" ]
df1 = df1[df1["ground"] != "Colombo (RPS)" ]
df1["stad"] = df1["stad"].apply(lambda x: x._address.rsplit(",",1)[1])

new_row = {'ground':'Tolerance Oval', 'stad':' Sri Lanka'}

df1 = df1.append(new_row, ignore_index=True)

df1 = df1.drop(columns = ["stad"])
df1["ground"][80] = "Mumbai (BS)" 

df1["stadium"] = df1["stadium"].apply(lambda x: x.strip())


Left_join = pd.merge(df,  
                     df1,  
                     on ='ground',  
                     how ='left') 

import pycountry_convert as pc

country_code = pc.country_name_to_country_alpha2("england", cn_name_format="default")
print(country_code)
continent_name = pc.country_alpha2_to_continent_code(country_code)
print(continent_name)

df["con_code"] = df["Stadium"].apply(lambda x: pc.country_alpha2_to_continent_code(pc.country_name_to_country_alpha2(x, cn_name_format="default")) )


runs_df.dtypes


import plotly.express as px
import numpy as np
df = px.data.gapminder().query("year == 2007")
new_df = runs_df.groupby(["ground","Stadium","cont"]).sum()
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)
fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium', 'ground'], values='Runs',
                  color='Runs', hover_data=['Runs'])
fig.show()

img_bytes = fig.to_image(format="png")


#tree map

#Runs
new_df = runs_df.groupby(["ground","Stadium","cont"]).sum()
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)

fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground'],
                 labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values='Runs',color = 'Stadium', height=600,width= 700)
fig.data[0].textinfo = 'label+text'
fig.data[0].hovertemplate = '%{label}<br>Runs = %{value}'
fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
st.plotly_chart(fig)

##Matches
new_df = runs_df.groupby(["ground","Stadium","cont"]).count()
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)

fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground'],
                 labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values='Runs',color = 'Stadium', height=600,width= 700)
fig.data[0].textinfo = 'label+text'
fig.data[0].hovertemplate = '%{label}<br>Runs = %{value}'
fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
st.plotly_chart(fig)

##Not outs

new_df2 = runs_df.groupby(["Stadium"]).count()
new_df1 = runs_df.groupby(["Stadium"]).sum()
new_df2["OUT"] = new_df2["OUT"] - new_df1["OUT"]
new_df = new_df2
new_df.reset_index(level=0, inplace=True)


fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground'],
                 labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values='OUTS',color = 'Stadium', height=600,width= 700)
fig.data[0].textinfo = 'label+text'
fig.data[0].hovertemplate = '%{label}<br>Runs = %{value}'
fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
st.plotly_chart(fig)

#6's
new_df = runs_df.groupby(["ground","Stadium","cont"]).sum()
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)

fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground'],
                 labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values="6's",color = 'Stadium', height=600,width= 700)
fig.data[0].textinfo = 'label+text'
fig.data[0].hovertemplate = '%{label}<br>Runs = %{value}'
fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
st.plotly_chart(fig)

#4's
new_df = runs_df.groupby(["ground","Stadium","cont"]).sum()
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)

fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground'],
                 labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values="4's",color = 'Stadium', height=600,width= 700)
fig.data[0].textinfo = 'label+text'
fig.data[0].hovertemplate = '%{label}<br>Runs = %{value}'
fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
st.plotly_chart(fig)

#Avg
new_df = runs_df.groupby(["ground","Stadium","cont"]).sum()
        new_df["avg"] = new_df["Runs"]/new_df["OUT"]
        for n, i in zip(new_df.index,new_df["avg"]):
            if i == float("inf"):
                inf = new_df.loc[n]["Runs"]*2
                new_df = new_df.replace(to_replace =[float("inf")],  
                                    value =inf)
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)

fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground'],
                 labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values="avg",color = 'Stadium', height=600,width= 700)
fig.data[0].textinfo = 'label+text'
fig.data[0].hovertemplate = '%{label}<br>Runs = %{value}'
fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
st.plotly_chart(fig)

#SR
new_df = runs_df.groupby(["ground","Stadium","cont"]).sum()
new_df["SR"] = (new_df["Runs"]/new_df["Balls"])*100
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)
new_df.reset_index(level=0, inplace=True)

fig = px.treemap(new_df, path=[px.Constant('world'), 'cont', 'Stadium','ground'],
                 labels={'labels':'Stadium' ,'parent' : 'continent', 'Stadium' : 'Country'}, values="SR",color = 'Stadium', height=600,width= 700)
fig.data[0].textinfo = 'label+text'
fig.data[0].hovertemplate = '%{label}<br>Runs = %{value}'
fig.update_traces(marker_colors=["pink", "royalblue", "yellow", "orange", "lightblue"])
st.plotly_chart(fig)


#options
import numpy as np
opp = runs_df["opp"].unique().tolist()
opp.insert(0,"All")

np.append(opp, "All")


year = runs_df["Year"].unique().tolist()
year.sort()


runs_df = runs_df[runs_df["opp"] == "England"]

#DYK
#last match_date
list_sen = []
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
lm_s = lm.format(con = con, ply = ply, grou = grou)
list_sen.append(lm_s)



#last 5 matches - SR_d
runs_df_5 = runs_df.sort_values(by='date', ascending=False)
runs_df_5 = runs_df_5.head()
SR_d = (runs_df_5["Runs"].sum()/runs_df_5["Balls"].sum())*100
text_SR = '{ply} Strike rate was {SR_d} in his last five matches'
text_SR = text_SR.format(SR_d = SR_d, ply = ply)
list_sen.append(text_SR)



#last 5 matches - Avg_d
runs_df_5 = runs_df.sort_values(by='date', ascending=False)
runs_df_5 = runs_df_5.head()
avg_d = runs_df_5["Runs"].sum()/runs_df_5["OUT"].sum()
if avg_d == float("inf"):
    avg_d = runs_df_5["Runs"].sum()*2
else :
    avg_d = runs_df_5["Runs"].sum()/runs_df_5["OUT"].sum()
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



#Runs percentage 
runs_c = runs_df.groupby("Stadium").sum()
stad_d = runs_c[runs_c["Runs"] == runs_c["Runs"].max()].index[0]
per = round(runs_c["Runs"].max()/runs_c["Runs"].sum()*100).astype(int)
text_per = "{ply} has scorced more than {per}% of his Total Carrer runs in {stad_d} Picthes"
text_per = text_per.format(ply = ply, per = per, stad_d = stad_d)
list_sen.append(text_per)


#played aganist teams
runs_m = runs_df.groupby("opp").count()
nteams = runs_df["opp"].nunique()
text_opp = "{ply} has played [nteams] different Oppenents in his whole career."
text_opp = text_opp.format(ply = ply, nteams = nteams)
list_sen.append(text_opp)


#6's AVG
six_count = (runs_df["6's"].sum()/runs_df["Balls"].sum())*20
text_sixs = '{ply} hits {six_count} Sixs in every 20 Balls he plays'
text_sixs = text_sixs.format(ply = ply, six_count = six_count)
list_sen.append(text_sixs)

#4's AVG
per = round((runs_df["4's"].sum()/runs_df["Balls"].sum())*20).astype(int)
ply.split()[1]
text_fours = "{ply} will hit {per} Fours in every 20 Balls he plays"
text_fours = text_fours.format(ply = ply.split()[1], per = per)
list_sen.append(text_fours)

#run's Percentage_min
runs_c = runs_df.groupby("Stadium").sum()
stad_d = runs_c[runs_c["Runs"] == runs_c["Runs"].min()].index[0]
per = round(runs_c["Runs"].min()/runs_c["Runs"].sum()*100).astype(int)
text_per_min = "{ply} has scorced Only {per}% of his Total Carrer runs in {stad_d} Picthes"
text_per_min = text_per_min.format(ply = ply, per = per, stad_d = stad_d)
list_sen.append(text_per_min)

import random
sentenses = random.sample(list_sen,3)










