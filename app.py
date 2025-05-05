import streamlit as st
import numpy as np
import joblib

st.set_page_config(layout="wide")

scaler = joblib.load("scaler.pkl")

st.title("Restaurant Rating Prediction App")

st.caption("This app helps you to predict a restaurant review class")

st.divider()

averagecost = st.number_input("Please enter the cost for estimated two", min_value=50, max_value=99999, value=1000, step=200)

tablebooking = st.selectbox("Restaurant has table booking?", ["YES", "NO"])

onlinedelivery = st.selectbox("Restaurant has online delivery?", ["YES", "NO"])

pricerange = st.selectbox("What is the price range (1 Cheapest, 4 Most expensive)", [1, 2, 3, 4])

predictbutton = st.button("Predict the review")

st.divider()

model = joblib.load("model.pkl")

bookingstatus = 1 if tablebooking == "YES" else 0

deliverystatus = 1 if onlinedelivery == "YES" else 0

values = [[averagecost, bookingstatus, deliverystatus, pricerange]]
my_x_values = np.array(values)

x = scaler.transform(my_x_values)

if predictbutton:

    prediction = model.predict(x)
    st.write(prediction)
    
    if prediction < 2.5:
        st.error("The restaurant review is bad")
    elif prediction < 3.5:
        st.warning("The restaurant review is average")
    elif prediction < 4.5:
        st.info("The restaurant review is good")
    else:
        st.success("The restaurant review is excellent")
   
