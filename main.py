import streamlit as st
import datetime
import requests
from backend import get_forecast
from backend import display

st.title("Weather Forecast ")
place=st.text_input("Place:",help="Type an existing District/City (example- Thane, Bhilai , Durg)")



number_of_days = st.slider("Forecast Days:", min_value=1,max_value=5,
                 help="Select The number of forecasted days")

start_date=datetime.date.today()
d = datetime.timedelta(days = number_of_days)
end_date=start_date+d

option = st.selectbox("Select data to view:",
                      ("Temperature","Sky"))

if place:
    try:
        content=get_forecast(place,str(start_date),str(end_date))
        display(content, number_of_days, option, place)
    except requests.exceptions.JSONDecodeError:
        st.info("Please Enter a valid Place Argument")








