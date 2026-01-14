# ML_Classification_Credit_Scoring_Project
# Credit Scoring Classification Project

## Overview
This project is a complete machine learning pipeline for credit scoring, including data preprocessing, feature engineering, model training, evaluation, and deployment via a Streamlit web app. The goal is to predict the likelihood of loan default using customer, loan, and bureau data.

## Features
- Data cleaning and merging from multiple sources
- Exploratory Data Analysis (EDA) and visualization
- Feature engineering and selection (IV, WOE, VIF)
- Handling class imbalance (SMOTETomek, RandomUnderSampler)
- Model training: Logistic Regression, Random Forest, XGBoost
- Hyperparameter tuning (Optuna, RandomizedSearchCV)
- Model evaluation: Accuracy, F1, ROC-AUC, KS statistic
- Model export and deployment with Streamlit

## Project Structure
```
ML_Classification_Credit_Scoring_Project/
├── data/
│   ├── customers.csv
│   ├── loans.csv
│   └── bureau_data.csv
├── artifacts/
│   └── loan_default_model_logistic.joblib
├── credit_score_model.ipynb   # Jupyter notebook for EDA, feature engineering, modeling
├── streamlit_app.py           # Streamlit web app for predictions
├── main.py                    # (Optional) Script entry point
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## How to Run
1. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```
2. **Run the Streamlit app**
	```bash
	streamlit run streamlit_app.py
	```
3. **Use the App**
	- Enter customer and loan details in the web form.
	- Get instant predictions and probability of default.

## Notebooks
- All data exploration, feature engineering, and model training steps are documented in `credit_score_model.ipynb`.

## Model Deployment
- The trained model and scaler are exported as a joblib file in the `artifacts/` directory.
- The Streamlit app loads this file for real-time predictions.

## Requirements
See `requirements.txt` for all dependencies.
