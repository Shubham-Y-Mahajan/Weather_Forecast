import requests
import streamlit as st
import plotly.express as px
# plotly and bokeh are data visualization library

def get_forecast(location,start_date,end_date):
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" \
          f"{location}/{start_date}/{end_date}?" \
          "unitGroup=metric&include=hours&key=TH7SK4KJAV5P93FANMYBGWEGZ&contentType=json"

    request=requests.get(url)
    content=request.json()

    return content


#content=get_forecast(place,"2023-06-30","2023-07-1")

def display(content,number_of_days,option,place):
    temperature_data = []
    sky_data = []
    datetime_data = []
    conditions_data = []
    date_data = []
    for i in range(number_of_days):
        date_data.append(content['days'][i]['datetime'])
        for j in range(24):  # treating 24:00 as the next day
            temperature_data.append(content['days'][i]['hours'][j]['temp'])
            sky_data.append(content['days'][i]['hours'][j]['icon'])
            datetime_data.append(content['days'][i]['hours'][j]['datetime'])
            conditions_data.append(content['days'][i]['hours'][j]['conditions'])

    st.subheader(f"{option} for next {number_of_days} days in {place}")
    if (option == "Temperature"):
        for i in range(number_of_days):
            with st.expander(date_data[i]):
                st.plotly_chart(
                    px.line(x=datetime_data[i * 24:((i + 1) * 24)], y=temperature_data[i * 24:((i + 1) * 24)],
                            title=date_data[i], labels={"x": "Hours", "y": "Temperature"}))

    else:
        for i in range(number_of_days):
            with st.expander(date_data[i]):

                for hour in range(i * 24,((i + 1) * 24),6):
                    col1, col2, col3, col4, col5, col6 = st.columns(6)  # .columns(n) will create n column objects


                    with col1:  # opens the column space
                       st.image(f"images/{sky_data[hour]}.png",caption=f"{datetime_data[hour]}")

                    with col2:  # opens the column space
                        st.image(f"images/{sky_data[hour]}.png", caption=f"{datetime_data[hour+1]}")

                    with col3:  # opens the column space
                        st.image(f"images/{sky_data[hour]}.png", caption=f"{datetime_data[hour+2]}")

                    with col4:  # opens the column space
                        st.image(f"images/{sky_data[hour]}.png", caption=f"{datetime_data[hour+3]}")

                    with col5:  # opens the column space
                        st.image(f"images/{sky_data[hour]}.png", caption=f"{datetime_data[hour+4]}")

                    with col6:  # opens the column space
                        st.image(f"images/{sky_data[hour]}.png", caption=f"{datetime_data[hour+5]}")





