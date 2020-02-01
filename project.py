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


def main():
    visu = select_visu()
    while (visu not in ["1", "2", "3"]):
        print("Undefined visualization, please select amoung the possible visualizations")
        visu = select_visu()
    if (visu == "1"):
        print("visu 1")
    elif (visu == "2"):
        print("visu 2")
    elif (visu == "3"):
        print("visu 3")
    exit(0)


# df = pandas.read_csv("russian_demography.csv", usecols=[
#     "year", "birth_rate", "death_rate", "gdw", "urbanization"])

# fig = px.parallel_coordinates(df,
#                               color="year",
#                               labels=labels,
#                               color_continuous_scale=px.colors.diverging.Tealrose,
#                               color_continuous_midpoint=2,
#                               range_color=[1990, 2017])
# fig.show()
# # fig.write_image("parallel_coordinate_plot.pdf")


def select_visu():
    print("[Russian Demogaphy Data]")
    print("----------------------------------------------------")
    print("Enter one of the following number to visualize data:")
    print("1 - Display the parallel coordinates")
    print("2 - ")
    print("----------------------------------------------------")
    return input()


if __name__ == "__main__":
    main()
