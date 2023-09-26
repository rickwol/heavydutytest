import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import datetime, timedelta

st.set_page_config(page_title="Ritprofielen", page_icon="📈")

#st.sidebar.header("Ritprofielen")

st.title("Heavy Duty Elektrificatie tool")


st.write("Op basis van uw input zijn dit drie trucks en laadstrategiëen")

col1, col2, col3, = st.columns(3)

with col1:
    st.header("Alleen depot laden")
    st.image("https://media.istockphoto.com/id/1306857153/nl/foto/het-laadstation-van-elektrische-voertuigen-op-een-achtergrond-van-een-vrachtwagen.jpg?s=612x612&w=0&k=20&c=kF5jroBqGmPsn_6zup2ahw1R2W6xNb6dNibQqlf-KGM=")
    st.text("Accu: 350 kWh")
    st.text("Range: 200km")
    st.text("Oplaadcapaciteit: 100kW")
with col2:
    st.header("Af en toe onderweg laden")
    st.image("https://media.istockphoto.com/id/1306857153/nl/foto/het-laadstation-van-elektrische-voertuigen-op-een-achtergrond-van-een-vrachtwagen.jpg?s=612x612&w=0&k=20&c=kF5jroBqGmPsn_6zup2ahw1R2W6xNb6dNibQqlf-KGM=")
    st.text("Accu: 300 kWh")
    st.text("Range: 180km")
    st.text("Oplaadcapaciteit: 120kW")
with col3:
    st.header("Frequent laden")
    st.image("https://media.istockphoto.com/id/1306857153/nl/foto/het-laadstation-van-elektrische-voertuigen-op-een-achtergrond-van-een-vrachtwagen.jpg?s=612x612&w=0&k=20&c=kF5jroBqGmPsn_6zup2ahw1R2W6xNb6dNibQqlf-KGM=")
    st.text("Accu: 200 kWh")
    st.text("Range: 120km")
    st.text("Oplaadcapaciteit: 150kW")

st.text("Gebruik deze input voor een verkenning van welke specifieke truck dit kan zijn in de ZETI tool:")
url = "https://globaldrivetozero.org/tools/zeti/"
st.write("Klik [hier](%s) voor de tool" % url)

truckinput = st.selectbox("Welke optie kiest u?", ("Alleen depot laden", "Af en toe onderweg", "Frequent laden"))