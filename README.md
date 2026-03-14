# Credit Risk Modeling

## Project Overview

This project focuses on building a machine learning model to predict the credit risk of loan applicants. The objective is to classify whether a customer is likely to be a **good credit risk or bad credit risk** based on financial and demographic attributes.



---

## Dataset

The project uses the **German Credit Dataset**, which contains information about loan applicants including:

* Age
* Job type
* Credit amount
* Duration
* Housing status
* Saving accounts
* Checking account status
* Purpose of loan
* Risk label (Good / Bad)

---

## Project Workflow

### 1. Data Loading

The dataset is loaded using **Pandas** for analysis and preprocessing.

### 2. Data Preprocessing

* Handling categorical variables
* Label Encoding for categorical features
* Feature selection for modeling

### 3. Exploratory Data Analysis (EDA)

Visualization techniques were used to understand data patterns:

* Distribution plots
* Correlation analysis
* Risk distribution

Libraries used:

* Matplotlib
* Seaborn

### 4. Model Building

Multiple machine learning algorithms were implemented to compare performance:

* Decision Tree Classifier
* Random Forest Classifier
* Extra Trees Classifier
* XGBoost Classifier

### 5. Hyperparameter Tuning

GridSearchCV was used to optimize model parameters for better performance.

### 6. Model Evaluation

Models were evaluated using:

* Accuracy Score
* Performance comparison across algorithms

### 7. Model Saving

The final trained model is saved using **Joblib** for future predictions.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Joblib
* Jupyter Notebook

---



