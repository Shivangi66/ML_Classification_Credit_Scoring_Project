import pandas as pd
from streamlit_app import prepocess_input, predict
import streamlit as st

if __name__ == "__main__":
    st.title('Credit Scoring Prediction')
    
    
    # Arrange input widgets in 3 columns per row
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=18, max_value=100, value=30)
        loan_purpose = st.selectbox('Loan Purpose', ['Personal', 'Home', 'Education', 'Auto'])
        number_of_open_accounts = st.number_input('Number of Open Accounts', min_value=0, value=1)
        income = st.number_input('Income', min_value=0.0, value=50000.0)
        loan_amount = st.number_input('Loan Amount', min_value=0.0, value=100000.0)


    with col2:
        avg_dpd = st.number_input('Average DPD', min_value=0.0, value=0.0)
        residence_type = st.selectbox('Residence Type', ['Owned', 'Mortgage', 'Rented'])
        loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])
        net_disbursement = st.number_input('Net Disbursement', min_value=0.0, value=100000.0)


    with col3:
        credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0.0, value=0.5)
        del_months_loan_ratio = st.number_input('Delinquent Months Loan Ratio', min_value=0.0, value=0.0)
        loan_tenure_months = st.number_input('Loan Tenure (Months)', min_value=1, value=12)

    # Collect all input values into a DataFrame
    input_dict = {
        'age': age,
        'number_of_dependants': 0,
        'years_at_current_address': 0,
        'sanction_amount': 0,
        'processing_fee': 0,
        'gst': 0,
        'net_disbursement': net_disbursement,
        'loan_tenure_months': loan_tenure_months,
        'principal_outstanding': 0,
        'bank_balance_at_application': 0,
        'number_of_open_accounts': number_of_open_accounts,
        'number_of_closed_accounts': 0,
        'enquiry_count': 0,
        'credit_utilization_ratio': credit_utilization_ratio,
        'loan_to_income_ratio': loan_amount/income,
        'del_months_loan_ratio': del_months_loan_ratio,
        'avg_dpd': avg_dpd,
        'loan_purpose': loan_purpose,
        'residence_type': residence_type,
        'loan_type': loan_type
    }
    user_input_df = pd.DataFrame([input_dict])
    processed_df = prepocess_input(user_input_df)
    st.markdown(f"**Computed Loan to Income Ratio:** {user_input_df['loan_to_income_ratio'].iloc[0]:.2f}")

    if st.button('Predict Credit Default'):  
        prediction, probability_default, credit_score = predict(processed_df)
        if credit_score <= 300:
            st.markdown(f"**Estimated Credit Score is Poor:** {credit_score:.2f}")
        elif 300 < credit_score <= 600:
            st.markdown(f"**Estimated Credit Score is Fair:** {credit_score:.2f}")
        elif 600 < credit_score <= 750:
            st.markdown(f"**Estimated Credit Score is Good:** {credit_score:.2f}")
        else:
            st.markdown(f"**Estimated Credit Score is Excellent:** {credit_score:.2f}")
        
        
        if prediction[0] == 1:
            st.error(f'The applicant is likely to default on the loan with a probability of {probability_default}.')
        else:
            st.success(f'The applicant is likely to not default on the loan with a probability of {1 - probability_default}.')