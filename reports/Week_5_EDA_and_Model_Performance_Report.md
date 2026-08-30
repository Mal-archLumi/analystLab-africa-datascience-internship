# Week 5: Advanced Machine Learning

## EDA and Model Performance Report

**House Price Prediction and Titanic Survival Prediction**

### 1. Introduction

This report presents the exploratory data analysis (EDA), data preparation, model development, performance comparison, and hyperparameter tuning completed during Week 5 of the Advanced Machine Learning internship. Two datasets were analyzed: the House Price Prediction dataset for regression and the Titanic dataset for classification.

### 2. House Price Prediction Dataset

#### 2.1 EDA and Data Preparation

The House Price Prediction dataset was reviewed to understand its structure, data types, missing values, duplicate records, numerical distributions, categorical variables, and relationships between predictors and house prices.

Data preparation included handling missing values, checking for duplicate records, encoding categorical variables, applying feature scaling where appropriate, and separating the predictors from the target variable. The resulting dataset was then split into training and testing sets for model development and evaluation.

EDA also examined relationships between housing characteristics and price, including the influence of numerical variables and categorical indicators. Distribution plots, boxplots, and relationship plots were used to identify patterns, variation, and potential outliers.

#### 2.2 Regression Models

| Model | MAE | MSE | RMSE | R² |
|---|---:|---:|---:|---:|
| Linear Regression | 970,043.40 | 1,754,318,687,330.66 | 1,324,506.96 | 0.6529 |
| Decision Tree | 1,195,266.06 | 2,642,802,637,614.68 | 1,625,669.90 | 0.4771 |
| Random Forest | 1,021,546.04 | 1,961,585,044,320.34 | 1,400,565.97 | 0.6119 |
| Gradient Boosting | 961,734.63 | 1,693,306,118,911.06 | 1,301,270.96 | 0.6650 |
| Tuned Gradient Boosting | 1,021,988.20 | 1,937,963,730,283.18 | 1,392,107.66 | 0.6166 |

#### 2.3 House Price Findings

Gradient Boosting achieved the strongest test-set performance among the evaluated regression models. It recorded the lowest MAE, MSE, and RMSE, and the highest R² score of 0.6650. Linear Regression ranked second and performed better than both the Decision Tree and Random Forest models.

Hyperparameter tuning was applied to Gradient Boosting using GridSearchCV. The selected parameters were `learning_rate=0.05`, `max_depth=2`, `min_samples_split=2`, and `n_estimators=100`. The tuned model did not outperform the original Gradient Boosting model on the held-out test set.

### 3. Titanic Survival Prediction Dataset

#### 3.1 EDA and Data Preparation

The cleaned Titanic dataset was loaded from `../data/cleaned/titanic_cleaned.csv`. The dataset contains passenger information including `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, and `Embarked`.

For modelling, `Survived` was used as the binary target variable. `PassengerId` was treated as an identifier, while `Name` and `Ticket` were excluded from the Week 5 model features. `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`, `Sex`, and `Embarked` were retained as predictive variables.

Categorical variables were converted into numerical features using one-hot encoding. Missing numerical values were handled where necessary. The data was split into training and testing sets using stratification on the target variable. `StandardScaler` was applied to the training features for Logistic Regression, while the tree-based models were trained using unscaled feature values.

#### 3.2 Classification Models

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8045 | 0.7931 | 0.6667 | 0.7244 | 0.8436 |
| Decision Tree | 0.8045 | 0.7500 | 0.7391 | 0.7445 | 0.7792 |
| Random Forest | 0.8101 | 0.7778 | 0.7101 | 0.7424 | 0.8287 |
| Gradient Boosting | 0.7989 | 0.7895 | 0.6522 | 0.7143 | 0.8165 |
| Tuned Random Forest | 0.8045 | 0.7931 | 0.6667 | 0.7244 | 0.8378 |

#### 3.3 Titanic Confusion Matrix Findings

The Logistic Regression confusion matrix was `[[98, 12], [23, 46]]`. This indicates 98 correct predictions for passengers who did not survive and 46 correct predictions for passengers who survived, with 12 false positives and 23 false negatives.

The Decision Tree confusion matrix was `[[93, 17], [18, 51]]`. The model correctly identified 93 passengers who did not survive and 51 passengers who survived, with 17 false positives and 18 false negatives.

The tuned Random Forest produced the same classification matrix as Logistic Regression: `[[98, 12], [23, 46]]`. Its predicted class labels therefore matched the baseline model on the test set, although its predicted probabilities resulted in a different ROC-AUC score.

#### 3.4 Titanic Findings

Random Forest achieved the highest Accuracy at 0.8101. Decision Tree achieved the highest F1 Score at 0.7445 and the highest Recall at 0.7391. Logistic Regression achieved the highest Precision at 0.7931 and the highest ROC-AUC at 0.8436.

Hyperparameter tuning was applied to Random Forest using GridSearchCV. The tuned model achieved an Accuracy of 0.8045, Precision of 0.7931, Recall of 0.6667, F1 Score of 0.7244, and ROC-AUC of 0.8378. The tuning did not improve overall test-set performance compared with the original Random Forest model.

### 4. Key EDA and Machine Learning Insights

- EDA is essential for understanding data structure, distributions, categorical variables, and data quality, all of which inform preprocessing and modelling decisions.
- Increased model complexity does not necessarily lead to better predictive performance.
- For the House Price task, Gradient Boosting produced the strongest test-set results.
- For the Titanic task, no single model dominated every classification metric; the best model depends on the evaluation objective.
- Hyperparameter tuning should be evaluated on unseen test data after cross-validation rather than assumed to improve performance automatically.
- Using multiple evaluation metrics provides a more complete view of model behaviour than relying on Accuracy or R² alone.

### 5. Conclusion

The Week 5 work demonstrated a complete machine learning workflow across both regression and classification tasks. The datasets were explored and prepared, baseline models were established, tree-based models were trained, performance was compared, and hyperparameter tuning was performed using GridSearchCV.

The results highlight the importance of empirical model evaluation. The best-performing model was not always the most complex or the tuned model. For House Price Prediction, the original Gradient Boosting model achieved the strongest results, while for Titanic Survival Prediction, Random Forest achieved the highest Accuracy and Decision Tree achieved the highest F1 Score. These findings provide a solid foundation for the feature engineering and model optimization work planned for Week 6.

### 6. Week 6 Connection

The Titanic dataset provides a strong basis for Week 6 feature engineering and model optimization. Potential engineered features include extracting titles from passenger names, creating family-size variables from `SibSp` and `Parch`, identifying whether a passenger was travelling alone, and developing additional interaction or categorical features. These engineered features can then be evaluated through feature selection, cross-validation, and further model optimization.