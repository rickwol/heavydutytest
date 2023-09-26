import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import datetime, timedelta

st.set_page_config(page_title="Ritprofielen", page_icon="📈")

#st.sidebar.header("Ritprofielen")

st.title("Heavy Duty Elektrificatie tool")


st.write("Vul hier het rittenpatroon in voor een dag met een maximaal aantal kilometers")


Aantalritten =  st.number_input('Hoeveel ritten op 1 dag?', step = 1, min_value= 1)
time = [0]*Aantalritten
timeend = [0]*Aantalritten
kilometer = [0]*Aantalritten
locatie = [0]*Aantalritten
Laden = [0]*Aantalritten
df = pd.DataFrame([dict(Location="Depot", Start=pd.to_datetime('2023-01-01 0:00:00'), Finish=pd.to_datetime('2023-01-01 0:00:00'))])
for z in range(Aantalritten):

    date = str(datetime.datetime.strptime('2023-01-01', '%Y-%m-%d').date())

    col1, col2, col3, col4, col5 = st.columns([1, 1,1.2,1,1])

    with col1:
        time[z] =  st.time_input('Starttijd Rit ' + str(z) , datetime.time(8, 45))
 
    with col2:
        timeend[z] =  st.time_input('Eindtijd Rit ' + str(z) , datetime.time(9, 45))
      
    with col3:
        kilometer[z] = st.number_input('Aantal kilometers rit ' + str(z), step = 1)
        
    with col4:
        locatie[z] = st.selectbox("Locatie einde rit", ("Depot", "Klant/Elders"), key=str(z)+"select")

    with col5: 
        Laden[z] = st.checkbox("Mogelijkheid tot opladen einde rit", key=str(z)+"check")
    
    time[z] = pd.to_datetime(date + " " + (time[z].strftime("%H:%M")))
    timeend[z] = pd.to_datetime(date + " " + (timeend[z].strftime("%H:%M")))

    if z ==0: 
        df2 = pd.DataFrame([
                dict(Location="Rit", Start=time[z], Finish=timeend[z])])   
        df = df.append(df2)
        df = df.tail(-1)
        
    if z > -1: 
        #df = df.iloc[:-1]
        df2 = pd.DataFrame([
            dict(Location="Rit", Start=time[z], Finish=timeend[z]),
            dict(Location="Depot", Start=timeend[z-1], Finish=time[z]) ])   

        df = df.append(df2)
            

maxi = df["Finish"].max()
mini = df["Start"].min()

df3 = pd.DataFrame([dict(Location="Depot", Start=maxi, Finish='2023-01-01 23:59:59'),
                   dict(Location="Depot", Start='2023-01-01 0:00:00', Finish=mini),])
df = df.append(df3)

st.dataframe(df)

fig = px.timeline(df, x_start="Start", x_end="Finish" , y = "Location")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up

st.plotly_chart(fig)
