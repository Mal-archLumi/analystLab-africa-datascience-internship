# AnalystLab Africa Data Science Internship --- Week 4 Report

## Supervised Learning: Housing Price Prediction and Titanic Survival Classification

**Intern:** Alvine Lumiti Makutu\
**Program:** AnalystLab Africa Data Science Internship\
**Week:** 4 --- Supervised Learning

------------------------------------------------------------------------

## 1. Introduction

Week 4 focused on supervised machine learning and the process of
building predictive models from labeled datasets.

Two different supervised learning problems were addressed:

1.  **Housing Prices Dataset** --- a regression problem where the
    objective was to predict house prices.
2.  **Titanic Dataset** --- a binary classification problem where the
    objective was to predict whether a passenger survived.

The work covered data preprocessing, categorical encoding, feature and
target selection, train/test splitting, model training, prediction, and
model evaluation.

------------------------------------------------------------------------

## 2. Objectives

The main objectives of the week were to:

-   Prepare datasets for machine learning.
-   Separate features from target variables.
-   Split data into training and testing sets.
-   Build a Linear Regression model for house price prediction.
-   Build a Logistic Regression model for Titanic survival prediction.
-   Make predictions using unseen test data.
-   Evaluate model performance using appropriate metrics.
-   Understand the difference between regression and classification.

------------------------------------------------------------------------

# 3. Housing Price Prediction --- Linear Regression

## 3.1 Dataset

The Housing dataset contains information about residential properties
and their prices.

The target variable was:

-   `price`

The available predictor variables included:

-   `area`
-   `bedrooms`
-   `bathrooms`
-   `stories`
-   `mainroad`
-   `guestroom`
-   `basement`
-   `hotwaterheating`
-   `airconditioning`
-   `parking`
-   `prefarea`
-   `furnishingstatus`

## 3.2 Data Preprocessing

The dataset was inspected for missing values and duplicate records. No
missing values or duplicate records requiring removal were identified.

The categorical variables could not be passed directly to the Linear
Regression model because machine learning algorithms require numerical
input. One-Hot Encoding was therefore used with `drop_first=True`.

This converted categorical variables such as `yes/no` and the
furnishing-status categories into numerical indicator variables.

The `drop_first=True` option was used to remove one category from each
categorical variable and avoid redundant dummy variables.

## 3.3 Feature and Target Selection

The target variable was:

``` text
price
```

The features were all remaining encoded variables.

``` python
X = housing.drop("price", axis=1)
y = housing["price"]
```

Therefore:

-   `X` represents the information used to predict house prices.
-   `y` represents the actual house prices.

## 3.4 Train/Test Split

The dataset was divided into training and testing data using an 80/20
split.

``` python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The training set was used to learn the relationship between the features
and house prices, while the test set was kept unseen during training and
used to evaluate how well the model generalizes to new observations.

`random_state=42` was used to make the split reproducible.

## 3.5 Linear Regression Model

A Linear Regression model was trained using the training data.

Linear Regression attempts to learn a mathematical relationship between
the input features and the continuous target variable, house price.

The trained model was then used to predict prices for the test dataset.

## 3.6 Model Evaluation

The Linear Regression model produced the following results:

  Metric                                       Result
  -------------------------------- ------------------
  Mean Absolute Error (MAE)            KSh 970,043.40
  Root Mean Squared Error (RMSE)     KSh 1,324,506.96
  R² Score                                       0.65

### Interpretation

The **MAE of KSh 970,043.40** means that, on average, the model's
predictions differed from the actual house prices by approximately KSh
970,043.

The **RMSE of KSh 1,324,506.96** indicates the typical magnitude of
prediction error while giving greater weight to larger errors.

The **R² score of 0.65** indicates that the model explains approximately
65% of the variation in house prices in the test data.

The results provide a useful baseline for comparing more advanced
regression algorithms.

## 3.7 Feature Coefficients

The Linear Regression coefficients provided insight into how the model
associated each feature with house price, while holding the other
features constant.

The strongest positive coefficients included:

  Feature                   Coefficient
  ----------------------- -------------
  `bathrooms`                 1,094,445
  `airconditioning_yes`         791,427
  `hotwaterheating_yes`         684,650
  `prefarea_yes`                629,891
  `stories`                     407,477
  `basement_yes`                390,251
  `mainroad_yes`                367,920

The largest negative coefficients were:

  Feature                               Coefficient
  ----------------------------------- -------------
  `furnishingstatus_unfurnished`           -413,645
  `furnishingstatus_semi-furnished`        -126,882

The coefficients should be interpreted as model-estimated associations
rather than proof that an individual feature directly causes a change in
house price.

------------------------------------------------------------------------

# 4. Titanic Survival Prediction --- Logistic Regression

## 4.1 Dataset

The Titanic dataset contains passenger information and whether each
passenger survived.

The target variable was:

-   `Survived`

where:

-   `0` = did not survive
-   `1` = survived

The dataset contained 891 passenger records.

## 4.2 Data Preprocessing

The dataset was inspected for missing values and duplicate records.

The features selected for modelling were:

-   `Pclass`
-   `Age`
-   `SibSp`
-   `Parch`
-   `Fare`
-   `Sex_male`
-   `Embarked_Q`
-   `Embarked_S`

The following columns were removed because they were identifiers or
text-based fields that were not directly used as predictive features:

-   `PassengerId`
-   `Name`
-   `Ticket`

Categorical variables were converted into numerical variables using
One-Hot Encoding with `drop_first=True`.

This resulted in features such as:

``` text
Sex_male
Embarked_Q
Embarked_S
```

## 4.3 Feature and Target Selection

The target variable was:

``` text
Survived
```

The remaining selected passenger characteristics were used as input
features.

``` python
X = titanic.drop("Survived", axis=1)
y = titanic["Survived"]
```

## 4.4 Train/Test Split

An 80/20 train/test split was used with `random_state=42`.

``` python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

This produced 712 training observations and 179 test observations.

## 4.5 Logistic Regression Model

Logistic Regression was selected because the target variable is binary.

Unlike Linear Regression, which predicts a continuous numerical value,
Logistic Regression estimates the probability of an observation
belonging to a class.

For this project, the classes were:

``` text
0 = Did not survive
1 = Survived
```

The model was initially trained using the default iteration limit, which
produced a convergence warning. The `max_iter` parameter was increased
to 1000:

``` python
model = LogisticRegression(max_iter=1000)
```

The model then trained successfully without the convergence warning.

## 4.6 Predictions

Predictions were generated using:

``` python
y_pred = model.predict(X_test)
```

The model was also examined using:

``` python
model.predict_proba(X_test)
```

`predict()` returns the predicted class, while `predict_proba()`
provides the estimated probability for each class.

## 4.7 Model Evaluation

The Logistic Regression model achieved:

  Metric                  Result
  --------------------- --------
  Accuracy Score          0.8101
  Accuracy Percentage     81.01%

The model therefore correctly classified approximately 81% of the
passengers in the unseen test set.

## 4.8 Confusion Matrix

The confusion matrix was:

``` text
[[90 15]
 [19 55]]
```

Interpreted as:

                                  Predicted: Did Not Survive   Predicted: Survived
  ----------------------------- ---------------------------- ---------------------
  **Actual: Did Not Survive**                             90                    15
  **Actual: Survived**                                    19                    55

Therefore:

-   **90** were correctly predicted as non-survivors.
-   **55** were correctly predicted as survivors.
-   **15** were predicted as survivors but actually did not survive.
-   **19** were predicted as non-survivors but actually survived.

The model correctly classified:

``` text
90 + 55 = 145
```

out of:

``` text
179
```

test observations, resulting in the reported 81.01% accuracy.

------------------------------------------------------------------------

# 5. Regression vs Classification

Week 4 demonstrated two fundamental types of supervised learning.

  Aspect                   Housing                      Titanic
  ------------------------ ---------------------------- -----------------------
  Problem Type             Regression                   Binary Classification
  Model                    Linear Regression            Logistic Regression
  Target                   House price                  Survival status
  Target Type              Continuous numerical value   Binary category
  Main Evaluation Metric   RMSE                         Accuracy

The Housing model predicts **how much** a house is expected to cost,
while the Titanic model predicts **which class** a passenger belongs to.

This distinction determines the type of machine learning algorithm and
evaluation metrics that should be used.

------------------------------------------------------------------------

# 6. Challenges Encountered

Several practical machine learning challenges were encountered during
the week.

### Categorical Data

Machine learning models require numerical inputs, so categorical
variables had to be converted using One-Hot Encoding.

### Model Convergence

The initial Logistic Regression model produced a convergence warning
because the optimizer reached its default iteration limit. Increasing
`max_iter` to 1000 allowed the model to converge successfully.

### Understanding Model Evaluation

Different types of machine learning problems require different
evaluation metrics. Regression and classification metrics cannot simply
be interchanged.

### Train/Test Splitting

The data had to be divided into training and testing sets to evaluate
the models on observations that were not used during training.

------------------------------------------------------------------------

# 7. Key Learnings

The major lessons from Week 4 were:

1.  Supervised learning uses labeled data to learn a relationship
    between input features and a target variable.
2.  `X` contains the input features, while `y` contains the target
    variable.
3.  Training and testing data serve different purposes.
4.  Categorical variables must be appropriately encoded before being
    passed to most machine learning models.
5.  Linear Regression is appropriate for predicting continuous numerical
    outcomes.
6.  Logistic Regression is appropriate for binary classification.
7.  Model evaluation metrics must match the type of machine learning
    problem.
8.  A convergence warning does not necessarily mean a model failed, but
    it indicates that the optimization process may require additional
    iterations or preprocessing.
9.  A confusion matrix provides more detail about classification errors
    than accuracy alone.
10. Model coefficients can provide insight into the relationships
    learned by a Linear Regression model.

------------------------------------------------------------------------

# 8. Overall Results

  Dataset   Model                 Evaluation               Result
  --------- --------------------- ------------ ------------------
  Housing   Linear Regression     MAE              KSh 970,043.40
  Housing   Linear Regression     RMSE           KSh 1,324,506.96
  Housing   Linear Regression     R²                         0.65
  Titanic   Logistic Regression   Accuracy                 81.01%

These models establish baseline supervised learning performance that can
be improved and compared with more advanced machine learning algorithms
in subsequent work.

------------------------------------------------------------------------

# 9. Conclusion

Week 4 provided practical experience with the complete supervised
learning workflow, from data preparation to model evaluation.

The Housing dataset was used to develop a Linear Regression model for
continuous price prediction, achieving an RMSE of KSh 1,324,506.96 and
an R² score of 0.65.

The Titanic dataset was used to develop a Logistic Regression
classification model, which achieved 81.01% accuracy on the test
dataset. The confusion matrix provided additional insight into the
model's correct and incorrect classifications.

The most important outcome of the week was not only obtaining model
scores, but understanding the process behind them: preparing data
correctly, selecting appropriate algorithms, separating training and
testing data, making predictions, and interpreting model performance.

These models provide a foundation for the next stage of the internship,
where more advanced machine learning algorithms, model comparison, and
hyperparameter tuning will be explored.
