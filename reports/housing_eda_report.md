# Exploratory Data Analysis (EDA) Report

## Housing Price Prediction Dataset

---

# 1. Introduction

Exploratory Data Analysis (EDA) was conducted to understand the structure, quality, and characteristics of the housing dataset before developing any predictive model. The analysis involved examining both numerical and categorical variables, identifying missing values and duplicates, studying variable distributions, exploring relationships between variables, and determining the most influential features affecting house prices.

---

# 2. Dataset Overview

The dataset contains **545 observations** and **13 variables**, describing different characteristics of residential houses.

| Variable | Description |
|-----------|-------------|
| price | Selling price of the house (Target Variable) |
| area | Total floor area of the house |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| stories | Number of floors |
| mainroad | Access to the main road |
| guestroom | Availability of a guest room |
| basement | Availability of a basement |
| hotwaterheating | Availability of hot water heating |
| airconditioning | Availability of air conditioning |
| parking | Number of parking spaces |
| prefarea | Whether the house is located in a preferred residential area |
| furnishingstatus | Furnishing condition of the house |

---

# 3. Data Cleaning

## Missing Values

The dataset was inspected for missing values.

**Observation**

No missing values were found.

---

## Duplicate Values

Duplicate records were checked.

**Observation**

No duplicate records were identified.

---

# 4. Univariate Analysis

Univariate analysis was performed to understand the distribution of individual variables.

## Numerical Variables

The following numerical variables were analysed:

- Price
- Area
- Bedrooms
- Bathrooms
- Stories
- Parking

The analysis included:

- Descriptive statistics
- Histograms
- Kernel Density Estimation (KDE)
- Boxplots
- Skewness analysis

### Price

House prices ranged from **1,750,000** to **13,300,000**, with an average selling price of approximately **4.77 million**.

The distribution is **positively skewed (Skewness = 1.21)**, indicating that most houses are moderately priced while a relatively small number of luxury houses have very high prices.

The boxplot identified several high-value outliers, which are expected in real estate datasets.

---

### Area

House area also exhibited a positively skewed distribution, with larger houses appearing less frequently than smaller and medium-sized houses.

---

### Bedrooms

Most houses contain **3 bedrooms**, with relatively few houses containing 5 or 6 bedrooms.

---

### Bathrooms

Most houses contain **1 bathroom**, while houses with multiple bathrooms are less common.

---

### Stories

The majority of houses contain either **1 or 2 stories**, while 3- and 4-storey houses occur less frequently.

---

### Parking

Most houses have **no parking spaces**, while fewer houses provide one, two, or three parking spaces.

---

# Categorical Variables

The following categorical variables were analysed using frequency tables and count plots.

## Main Road

Approximately **85.87%** of houses have access to the main road, while **14.13%** do not.

---

## Guest Room

Approximately **82.20%** of houses do not have a guest room, whereas **17.80%** do.

---

## Basement

Approximately **64.95%** of houses do not contain a basement, while **35.05%** have one.

---

## Hot Water Heating

Hot water heating is uncommon within the dataset.

Approximately **95.41%** of houses do not have hot water heating, while only **4.59%** do.

---

## Air Conditioning

Approximately **68.44%** of houses do not have air conditioning, whereas **31.56%** do.

---

## Preferred Area

Approximately **76.51%** of houses are not located in preferred residential areas, while **23.49%** are.

---

## Furnishing Status

The majority of houses are **semi-furnished (41.65%)**, followed by **unfurnished (32.66%)**, while **25.69%** are fully furnished.

---

# 5. Bivariate Analysis

Relationships between house price and other variables were examined using scatter plots, boxplots, boxen plots, bar charts, and grouped summary statistics.

## Price vs Area

A scatter plot revealed a clear positive relationship between house area and selling price.

Generally, larger houses tend to command higher market prices, although some variability exists due to other housing characteristics.

---

## Price vs Bedrooms

Average house prices increase as the number of bedrooms increases.

However, houses with five and six bedrooms are relatively few, making their averages less reliable.

---

## Price vs Bathrooms

House prices increase consistently with the number of bathrooms.

Properties with multiple bathrooms generally command substantially higher prices than those with only one bathroom.

---

## Price vs Stories

Houses with more stories generally have higher selling prices.

Four-storey houses exhibit the highest average prices within the dataset.

---

## Price vs Parking

House prices generally increase as parking availability increases.

Houses with two parking spaces exhibit the highest average prices.

---

## Price vs Main Road

Houses connected to the main road are considerably more expensive than those without direct access.

---

## Price vs Guest Room

Properties with guest rooms generally sell for higher prices than those without.

---

## Price vs Basement

Houses with basements exhibit higher average selling prices than houses without basements.

---

## Price vs Hot Water Heating

Houses with hot water heating have higher average prices.

However, only a small number of houses possess this feature, making the observed relationship less reliable.

---

## Price vs Air Conditioning

Air-conditioned houses command significantly higher prices than houses without air conditioning.

---

## Price vs Preferred Area

Properties located within preferred residential areas have substantially higher selling prices than houses outside preferred locations.

---

## Price vs Furnishing Status

Fully furnished houses exhibit the highest average prices, followed by semi-furnished houses, while unfurnished houses have the lowest average selling prices.

---

# 6. Correlation Analysis

Pearson correlation analysis was conducted to measure the strength of the linear relationship between house price and the predictor variables.

## Correlation with Price

| Feature | Correlation |
|----------|------------:|
| Area | 0.536 |
| Bathrooms | 0.518 |
| Air Conditioning | 0.453 |
| Stories | 0.421 |
| Parking | 0.384 |
| Bedrooms | 0.366 |
| Preferred Area | 0.330 |
| Furnishing Status | 0.305 |
| Main Road | 0.297 |
| Guest Room | 0.256 |
| Basement | 0.187 |
| Hot Water Heating | 0.093 |

The analysis indicates that **Area**, **Bathrooms**, **Air Conditioning**, and **Stories** are the variables most strongly associated with house prices.

No strong negative correlations were observed.

---

# 7. Important Features

Based on the correlation analysis and bivariate visualizations, the most influential variables affecting house price are:

1. Area
2. Bathrooms
3. Air Conditioning
4. Stories
5. Parking
6. Bedrooms
7. Preferred Area
8. Furnishing Status
9. Main Road
10. Guest Room
11. Basement
12. Hot Water Heating

These variables are expected to contribute differently during predictive modeling, with area providing the strongest influence.

---

# 8. Key Findings

- The dataset is complete, with no missing values or duplicate records.
- House prices are positively skewed, with several high-value outliers.
- Larger houses generally command higher selling prices.
- Houses with more bathrooms, stories, parking spaces, and bedrooms tend to be more expensive.
- Air conditioning, preferred residential areas, and furnishing status positively influence house prices.
- Hot water heating has only a weak relationship with house price.
- Area is the strongest predictor of housing prices within the dataset.

---

# 9. Conclusion

The exploratory data analysis provided valuable insights into the housing dataset and identified the major factors influencing house prices. Structural characteristics such as area, number of bathrooms, stories, parking spaces, and air conditioning demonstrated the strongest relationships with the target variable. The dataset is well-structured and suitable for predictive modeling. The findings from this analysis will guide feature selection and model development in the subsequent stages of the project.