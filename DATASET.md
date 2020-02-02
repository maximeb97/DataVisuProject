# Russian Demography Data

## Description

Dataset of Russian Demography from 1990 to 2017. It contains demographic features like natural population growth, birth rate, urbanization, etc.

## Format

The dataset (file location: `dataset/data.csv` contains:

- Several hundreds of lines ( 2380 )
- More than 6 attributes with unique id, separated by commas (8)
- Categorical features (`year`, `town`…)
- Correlated field (e.g: `npg` and `birth_rate`.)

## Content

Dataset has rows and 7 columns. Keys for columns:

- `id` : unique identifier.
- `year` : year, from 1990 to 2017.
- `region` : name of a federal subject of Russia. It could be oblast, republic, krai, autonomous okrug, federal city and a single autonomous oblast.
- `npg` : natural population growth by 1000 people. Calculating as the difference between birth rate and death rate.
- `birth_rate` : number of births by 1000 people.
- `death_rate` : number of deaths by 1000 people.
- `gdw` : general demographic weight (how many people of non-working age account for 100 people of working age). Working age for men 16-60 years, for women 16-55 years.
- `urbanization` : percentage of urban population.

## Source

[Russian Demography Data (1990 - 2017) - Maksim Zhdanov](https://www.kaggle.com/dwdkills/russian-demography)