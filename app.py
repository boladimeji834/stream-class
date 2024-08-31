import joblib, numpy as np, pandas as pd, streamlit as st

# import the model.pkl file as my model 
model = joblib.load('model.pkl')

st.title("Laptop Price Prediction")

# feature1 = st.number_input("Enter The Value of RAM space: ")
# feature2 = st.number_input("Enter The Value of Battery Capacity: ")
# feature3 = st.number_input("Enter The Value of Screen Resolution: ")


st.header("Form Header")
form = st.form(key="Input Form")
feature1 = float(form.number_input("Enter The Value of RAM space: "))
feature2 = float(form.number_input("Enter The Value of Battery Capacity: "))
feature3 = float(form.number_input("Enter The Value of Screen Resolution: "))
submit_btn = form.form_submit_button("Submit")

input_array = np.array([[feature1, feature2, feature3]])

if submit_btn: 
    if not input_array is None: 
        prediction = model.predict(input_array)

        st.write(f'The Price of the laptop for the required specs is: ${int(prediction[0])}')
    else: 
        st.write("Please fill all the required fields.")

