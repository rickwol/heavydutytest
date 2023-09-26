import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import datetime, timedelta

st.set_page_config(page_title="Ritprofielen", page_icon="📈")

#st.sidebar.header("Ritprofielen")

st.title("Heavy Duty Elektrificatie tool")


st.write("Vul hier het rittenpatroon in voor een dag met een maximaal aantal kilometers")


Aantaltrucks=  st.number_input('Hoeveel trucks verwacht u in 2030 te elektrificeren?', step = 1, min_value= 1)

st.write("Op basis van uw eerdere input zou uw laadprofiel erg ongeveer zo uit komen te zien")

df2 = pd.read_csv("profiel.csv", sep=";")
date = "2023-01-01"


df2["Tijdstip"] = pd.to_datetime(df2["Tijdstip"])
df2["Load(kW)"] = df2["Load(kW)"]*Aantaltrucks
fig = px.line(df2, x="Tijdstip", y="Load(kW)", title= "Laadprofiel")


st.plotly_chart(fig)

