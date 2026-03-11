import streamlit as st
import pandas as pd
import joblib

# 1. Load the model and encoders
model = joblib.load("extra_trees_credit_model.pkl")

# Load all 4 encoders into a dictionary
encoder_cols = ["Sex", "Housing", "Saving accounts", "Checking account"]
encoders = {col: joblib.load(f"{col}_encoder.pkl") for col in encoder_cols}

st.title("Credit Risk Prediction App")
st.write("Enter applicant information to predict if the credit risk is Good or Bad.")

# 2. Collect User Input
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=80, value=30)
    sex = st.selectbox("Sex", ["male", "female"])
    job = st.number_input("Job (0=unskilled, 1=skilled)", min_value=0, max_value=3, value=1)
    housing = st.selectbox("Housing", ["own", "rent", "free"])

with col2:
    saving_accounts = st.selectbox("Saving Accounts", ["little", "moderate", "rich", "quite rich"])  
    checking_account = st.selectbox("Checking Accounts", ["little", "moderate", "rich"])   
    credit_amount = st.number_input("Credit amount", min_value=0, value=1000)
    duration = st.number_input("Duration (months)", min_value=1, value=12)


input_data = {
    "Age": [age],
    "Sex": [encoders["Sex"].transform([sex])[0]],
    "Job": [job],
    "Housing": [encoders["Housing"].transform([housing])[0]],
    "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],
    "Checking account": [encoders["Checking account"].transform([checking_account])[0]], # Fixed key name
    "Credit amount": [credit_amount],
    "Duration": [duration]
}

input_df = pd.DataFrame(input_data)


# 4. Predict
if st.button("Predict Risk"):
    try:
        # Use .values if the feature names error persists, 
        # but matching column names is better practice.
        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.success("### The predicted credit risk is: ** GOOD ** ✅")
        else:
            st.error("### The predicted credit risk is: ** BAD ** ⚠️")
            
    except Exception as e:
        st.error(f"Prediction Error: {e}")