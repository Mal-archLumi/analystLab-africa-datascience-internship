
---

# `week6_titanic_survival_prediction_report.md`

```markdown
# Week 6: Feature Engineering & Model Optimization — Titanic Survival Prediction

## 1. Project Overview

Week 6 of the AnalystLab Africa Data Science Internship focused on improving machine learning performance through feature engineering, feature transformation, feature selection, cross-validation, and hyperparameter tuning.

The Titanic Survival Prediction dataset was selected as the classification problem.

The objective was to transform raw passenger information into meaningful predictive features, identify the most important variables, optimize a Gradient Boosting classifier, and evaluate the resulting model using multiple classification metrics.

---

## 2. Dataset Overview

The cleaned Titanic dataset contained **891 observations and 11 columns**.

The target variable was:

- `Survived`

where:

- `0` = Did not survive
- `1` = Survived

The dataset included:

- `PassengerId`
- `Pclass`
- `Name`
- `Sex`
- `Age`
- `SibSp`
- `Parch`
- `Ticket`
- `Fare`
- `Embarked`

The data had previously been cleaned during Week 1, including removal of duplicate records and handling missing values.

---

## 3. Feature Engineering

Several new features were created to capture relationships that were not directly represented by the original variables.

### `FamilySize`

Calculated as:

```text
FamilySize = SibSp + Parch + 1