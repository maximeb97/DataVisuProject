import plotly.express as px
import pandas
import matplotlib.pyplot as plt

labels = {
    "year": "Année",
    "npg": "npg",
    "birth_rate": "Taux de naissance",
    "death_rate": "Taux de decès",
    "gdw": "Poids démographique",
    "urbanization": "Urbanisation"
}

df = pandas.read_csv("russian_demography.csv", usecols=[
                     "year", "birth_rate", "death_rate", "gdw", "urbanization"])

fig = px.parallel_coordinates(df,
                              color="year",
                              labels=labels,
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=2,
                              range_color=[1990, 2017])
fig.show()
# fig.write_image("parallel_coordinate_plot.pdf")


def print_help():
    print("[Russian Demogaphy Data]")
    print("----------------------------------------------------")
    print("Enter one of the following number to visualize data:")
    print("1 - Display the parallel coordinates")
    print("2 - ")
    print("----------------------------------------------------")
    return input()
