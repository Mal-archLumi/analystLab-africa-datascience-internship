#Titanic Dataset Exploratory Data Analysis (EDA) Report

1. Introduction

The objective of this analysis was to explore the Titanic dataset, identify patterns within the data, clean missing values, perform exploratory data analysis, and determine the most important features influencing passenger survival. The analysis included data cleaning, univariate analysis, bivariate analysis, and correlation analysis using Python, Pandas, Matplotlib, and Seaborn.

2. Dataset Overview.

The Titanic dataset contains 891 passenger records and 12 variables describing passenger demographics, ticket information, family relationships, and survival status.

The variables include:

PassengerId
Survived
Pclass
Name
Sex
Age
SibSp
Parch
Ticket
Fare
Cabin
Embarked

3. Data Cleaning
Missing Values

Three variables contained missing values:

Column	Missing Values	Percentage	Action Taken
Age	177	19.87%	Missing values were replaced with the mean age because the distribution exhibited only a slight positive skew.
Cabin	687	77.10%	The column was removed from the analysis because the proportion of missing values was too high for reliable imputation.
Embarked	2	0.22%	Missing values were replaced using the mode ("S"), the most frequent embarkation port.
Duplicate Values

No duplicate records were identified in the dataset.

4. Univariate Analysis

The distribution of each variable was examined individually.

Survival
Approximately 61.62% of passengers did not survive.
Approximately 38.38% survived.
Passenger Class
Third-class passengers formed the majority of the dataset.
First-class passengers represented the smallest proportion.
Sex
Male passengers outnumbered female passengers.
Age
Passenger ages ranged from 0.42 to 80 years.
The average age was approximately 29.7 years.
The distribution exhibited a slight positive skew with several older-age outliers.
SibSp
Most passengers travelled without siblings or spouses.
The distribution was highly positively skewed.
Parch
Most passengers travelled without parents or children.
The variable also exhibited a strong positive skew.
Fare
Ticket fares ranged from 0 to 512.33.
Fare exhibited a highly right-skewed distribution with numerous high-value outliers.
Embarked
Most passengers embarked from Southampton (S), followed by Cherbourg (C) and Queenstown (Q).
5. Bivariate Analysis

Relationships between Survival and other variables were investigated.

Passenger Class and Survival

Passenger class strongly influenced survival.

First-class passengers had the highest survival rate.
Third-class passengers had the lowest survival rate.
Sex and Survival

Sex exhibited the strongest relationship with survival.

Female passengers experienced substantially higher survival rates than male passengers.
Age and Survival

Age demonstrated only a weak relationship with survival.

Although survivors were slightly younger on average, the age distributions of survivors and non-survivors overlapped considerably.

SibSp and Survival

Passengers travelling with one sibling or spouse generally exhibited higher survival rates than passengers travelling alone or in very large family groups.

However, no consistent trend was observed across all SibSp values.

Parch and Survival

Passengers travelling with one to three parents or children generally exhibited higher survival rates than passengers travelling alone.

Passengers travelling in very large family groups experienced relatively poor survival outcomes, although these categories contained very few observations.

Fare and Survival

Passengers paying higher ticket fares generally demonstrated higher survival rates.

This relationship is consistent with the higher survival rates observed among first-class passengers.

Embarked and Survival

Passengers embarking from Cherbourg (C) recorded the highest survival rate, followed by Queenstown (Q) and Southampton (S).

This suggests that embarkation port may contain useful predictive information.

6. Correlation Analysis

Correlation analysis was performed using the numerical variables.

The strongest relationships observed were:

Pclass and Fare (-0.55): Moderate negative correlation indicating that passengers travelling in higher classes generally paid higher fares.
SibSp and Parch (0.41): Moderate positive correlation showing that passengers travelling with siblings or spouses were also likely to travel with parents or children.
Survived and Pclass (-0.34): Moderate negative correlation indicating that higher-class passengers were more likely to survive.
Survived and Fare (0.26): Weak positive correlation suggesting that passengers paying higher fares had better survival outcomes.

Most remaining variable pairs exhibited weak or negligible correlations.

7. Important Features

Based on the exploratory analysis, the following variables were identified as the most informative predictors of passenger survival:

Feature	Importance	Reason
Sex	Very High	Largest difference in survival rates
Pclass	Very High	Strong association with survival
Fare	High	Higher fares associated with higher survival
Embarked	Moderate	Survival varied across embarkation ports
Parch	Moderate	Small family groups showed better survival
SibSp	Moderate	Some relationship with survival
Age	Low	Weak relationship with survival

PassengerId, Name, and Ticket were not considered useful predictive variables in their original form because they primarily serve as identifiers.

8. Conclusion

The exploratory data analysis identified Sex, Passenger Class, and Fare as the most influential variables associated with passenger survival. Female passengers, first-class passengers, and passengers who paid higher fares experienced substantially higher survival rates.

Family-related variables (SibSp and Parch) also influenced survival, with passengers travelling in small family groups generally exhibiting better survival outcomes than those travelling alone or in very large groups. Age showed only a weak relationship with survival, while embarkation port demonstrated moderate predictive value.

Overall, the dataset is well-suited for predictive modeling after preprocessing, with Sex, Pclass, Fare, Embarked, Parch, and SibSp identified as the most important features for predicting passenger survival.