import streamlit as st


from st_pages import Page, add_page_title, show_pages

"## Declaring the pages in your app:"

show_pages(
    [
        Page("Hello.py", "Home", "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("Pages/01_Ritprofielen_Gemiddeld.py", "Ritprofieel Gemiddeld"),
        Page("Pages/02_Ritprofielen_Maximaal.py", "Ritprofieel Gemiddeld"),
        Page("Pages/03_Voertuig_opties.py", "Ritprofieel Gemiddeld"),
        Page("Pages/04_Laadprofiel.py", "Ritprofieel Gemiddeld"),
        Page("Pages/05_Netaansluiting.py", "Netaansluiting"),

       
    ]
)


st.write("Welkom bij de Heavy Duty elektrificatie tool")

st.markdown(
    """
    De tool voor een geïntegreerd advies voor elektrische logistiek
"""
)