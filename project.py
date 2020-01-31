import plotly.express as px
import pandas
import matplotlib.pyplot as plt

labels={"year": "Year", "npg": "npg", "birth_rate": "Taux de naissance", "death_rate": "Taux de decès"}

df = pandas.read_csv("russian_demography.csv", usecols=["year", "birth_rate", "death_rate", "gdw", "urbanization"])

fig = px.parallel_coordinates(df,
                              color="year",
                              labels=labels,
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=2,
                              range_color=[1990, 2017])
fig.show()
# fig.write_image("parallel_coordinate_plot.pdf")
