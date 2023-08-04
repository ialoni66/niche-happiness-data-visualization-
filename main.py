import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
# ("country", "happiness", "gdp", "social_support", "life_expectancy",
#                "freedom_to_make_life_choices", "generosity", "corruption")

plot1 = st.selectbox("Select data for the x axis",
              ("happiness", "gdp", "social_support", "life_expectancy",
               "freedom_to_make_life_choices", "generosity", "corruption"))
plot2 = st.selectbox("Select data for the y axis",
              ("happiness", "gdp", "social_support", "life_expectancy",
               "freedom_to_make_life_choices", "generosity", "corruption"))
st.subheader(f"{plot1.capitalize()} and {plot2.capitalize()}")


def get_data(plot1, plot2):
    df = pd.read_csv("happy.csv")
    for df["country"] in df:
        b = df[plot1]
        m = df[plot2]
    return b, m

b, m = get_data(plot1, plot2)

figure = px.scatter(x=b, y=m, labels={"x": f"{plot1}", "y": f"{plot2}"})
st.plotly_chart(figure)