import plotly.express as px
import pandas
import matplotlib.pyplot as plt

labels = {
    "year": "Year",
    "npg": "NPG",
    "birth_rate": "Birth rate",
    "death_rate": "Death rate",
    "gdw": "Demographic weight",
    "urbanization": "Urbanization"
}


def main():
    visu = select_visu()
    while (visu not in ["1", "2", "3"]):
        print("Undefined visualization, please select among the possible visualizations.")
        visu = select_visu()
    if (visu == "1"): 
        print("Parallel Coordinates")
    elif (visu == "2"):
        print("TODO")
    elif (visu == "3"):
        print("TODO")
    exit(0)

def select_visu():
    print("[Russian Demography Data]")
    print("----------------------------------------------------")
    print("Enter one of the following number to visualize data:")
    print("1 - Display the parallel coordinates")
    print("2 - ")
    print("----------------------------------------------------")
    return input()


if __name__ == "__main__":
    main()

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
