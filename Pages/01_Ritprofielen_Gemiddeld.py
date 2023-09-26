import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import datetime, timedelta

st.set_page_config(page_title="Ritprofielen", page_icon="📈")

#st.sidebar.header("Ritprofielen")

st.title("Heavy Duty Elektrificatie tool")


st.write("Vul hier het rittenpatroon in voor een gemiddelde dag")


Aantalritten =  st.number_input('Hoeveel ritten op 1 dag?', step = 1, min_value= 1) -1


df = pd.DataFrame(
    [
           {"Nummer rit": 1,"Starttijd Rit": "8:00", 'Eindtijd Rit' : "9:45", "Aantal kilometers": 10, "Kan laden op einde rit" : True, "Locatie einde rit: (Depot of Anders)" : "Depot"}
     
      
   ]
)  
if(Aantalritten > 0):
    for z in range(Aantalritten):
        df = df.append({"Nummer rit": z+2,"Starttijd Rit": "8:00", 'Eindtijd Rit' : "9:45", "Aantal kilometers": 10, "Kan laden op einde rit" : True, "Locatie einde rit: (Depot of Anders)" : "Depot"}, ignore_index=True)
        
 
edited_df = st.experimental_data_editor(df, num_rows="dynamic")

dfvis = pd.DataFrame([dict(Locatie="Depot", Start=pd.to_datetime('2023-01-01 0:00:00'), Finish=pd.to_datetime('2023-01-01 ' + df["Starttijd Rit"][0]))])

for z in range(len(df)):
    if z == 0:
         dfvis = dfvis.append( pd.DataFrame([dict(Locatie="Rit", Start=pd.to_datetime('2023-01-01 ' + df["Starttijd Rit"][z]), Finish=pd.to_datetime('2023-01-01 ' + df["Eindtijd Rit"][z]))]))
    else:
         dfvis = dfvis.append( pd.DataFrame([dict(Locatie=df["Locatie einde rit: (Depot of Anders)"][z], Start=pd.to_datetime('2023-01-01 ' + df["Eindtijd Rit"][z-1]), Finish=pd.to_datetime('2023-01-01 ' + df["Starttijd Rit"][z]))]))
         dfvis = dfvis.append( pd.DataFrame([dict(Locatie="Rit", Start=pd.to_datetime('2023-01-01 ' + df["Starttijd Rit"][z]), Finish=pd.to_datetime('2023-01-01 ' + df["Eindtijd Rit"][z]))]))
        

   
         

fig = px.timeline(dfvis, x_start="Start", x_end="Finish" , y = "Locatie")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up

st.plotly_chart(fig)
