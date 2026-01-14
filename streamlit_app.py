import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

model_data = load('artifacts/loan_default_model_logistic.joblib')
model = model_data['model']
scaler = model_data['scaler']
cols_to_scale = list(model_data['cols_to_scale'])
features = model_data['features']


def prepocess_input(input_df):
    if input_df['loan_purpose'].iloc[0] == 'Education':
        input_df['loan_purpose_Education'] = 1
        input_df['loan_purpose_Home'] = 0
        input_df['loan_purpose_Personal'] = 0
    elif input_df['loan_purpose'].iloc[0] == 'Home':
        input_df['loan_purpose_Education'] = 0
        input_df['loan_purpose_Home'] = 1
        input_df['loan_purpose_Personal'] = 0
    elif input_df['loan_purpose'].iloc[0] == 'Personal':
        input_df['loan_purpose_Education'] = 0
        input_df['loan_purpose_Home'] = 0
        input_df['loan_purpose_Personal'] = 1
    else:
        input_df['loan_purpose_Education'] = 0
        input_df['loan_purpose_Home'] = 0
        input_df['loan_purpose_Personal'] = 0
        
    if input_df['loan_type'].iloc[0] == 'Unsecured':
        input_df['loan_type_Unsecured'] = 1
    else:
        input_df['loan_type_Unsecured'] = 0
        
    if input_df['residence_type'].iloc[0] == 'Owned':
        input_df['residence_type_Owned'] = 1
        input_df['residence_type_Rented'] = 0
    elif input_df['residence_type'].iloc[0] == 'Rented':
        input_df['residence_type_Owned'] = 0
        input_df['residence_type_Rented'] = 1
    
    input_df = input_df.drop(columns=['loan_purpose', 'loan_type', 'residence_type'])
    
    return input_df

def predict(processed_df, base_score = 300, base_length = 600):
    # Make a copy to avoid modifying original
    df = processed_df.copy()

    # Only scale columns that are present in both cols_to_scale and features
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    prediction_default = model.predict(df[features])
    pred_proba_nondefault = model.predict_proba(df[features])[0][0]
    pred_proba_default = 1 - pred_proba_nondefault
    
    credit_score = base_score + (base_length * (pred_proba_nondefault))
    return prediction_default, pred_proba_default, credit_score