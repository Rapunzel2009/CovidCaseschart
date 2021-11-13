import pandas as pd
import plotly.express as px

df = pd.read_csv("CovidData.csv")

figure=px.scatter(df,x="date",y="cases", color="country")

figure.show()