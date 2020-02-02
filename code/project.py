from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv("russian_demography.csv", usecols=[
    "year", "birth_rate", "death_rate", "gdw", "urbanization", "npg", "region"])

for i in df.year.unique():
    fig = plt.figure(num=None, figsize=(15, 6), dpi=100,
                     facecolor='w', edgecolor='k')
    sns.catplot(x="region", y="npg", data=df[df['year'] == i])
    plt.ylim(-15, 20)
    plt.xticks(fontsize=5)
    plt.xticks(rotation=90)
    plt.savefig(f"render/scatter_plot_{i}.png")
    plt.close()


exit(0)


def main():
    visu = select_visu()
    while (visu not in ["1", "2", "3"]):
        print("Undefined visualization, please select among the possible visualizations.")
        visu = select_visu()
    if (visu == "1"):
        visu_parallel_coordinates()
    elif (visu == "2"):
        print("TODO")
    elif (visu == "3"):
        print("TODO")
    exit(0)


def visu_parallel_coordinates():
    labels = {
        "year": "Année",
        "npg": "Variation naturelle",
        "birth_rate": "Taux de naissance",
        "death_rate": "Taux de decès",
        "gdw": "Poids démographique",
        "urbanization": "Urbanisation"
    }
    df = pandas.read_csv("russian_demography.csv", usecols=[
        "year", "birth_rate", "death_rate", "gdw", "urbanization", "npg"])

    fig = px.parallel_coordinates(df,
                                  color="year",
                                  labels=labels,
                                  color_continuous_scale=px.colors.diverging.Tealrose,
                                  color_continuous_midpoint=2,
                                  range_color=[1990, 2017])
    fig.show()


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