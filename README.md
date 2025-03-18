# Restaurant Rating Prediction App

The **Restaurant Rating Prediction App** is a **Streamlit-based web application** designed to predict restaurant ratings based on user inputs. Using a **machine learning model**, the app analyzes factors such as **estimated cost, table booking availability, online delivery, and price range** to estimate a restaurant’s rating.  

The model is trained on a dataset containing restaurant features and their corresponding ratings. By leveraging **pre-trained machine learning algorithms**, the app provides instant predictions, helping users assess restaurant quality interactively.


## Overview
This project is a **Streamlit-based web application** that predicts restaurant ratings based on user inputs. The model leverages machine learning to estimate ratings based on factors like **cost, table booking availability, online delivery, and price range**.

## Technologies Used
- **Python**
- **Streamlit** (for the web app)
- **NumPy** (for numerical computations)
- **Joblib** (for model and scaler loading)
- **Scikit-learn** (for training the model)

## Dataset
The dataset used for training includes:
- **Estimated Cost for Two**
- **Table Booking Availability** (Yes/No)
- **Online Delivery Availability** (Yes/No)
- **Price Range** (1 to 4)
- **Ratings** (target variable)

## Steps Involved
1. **Data Preprocessing**: Handled missing values and scaled numerical features.
2. **Feature Engineering**: Converted categorical features into numerical form.
3. **Model Training**: Trained a machine learning model to predict ratings.
4. **Deployment**: Built a Streamlit web app to take user inputs and predict ratings.

## Results
- The model classifies restaurant ratings into **Bad, Average, Good, and Excellent**.
- Users receive instant predictions along with color-coded feedback.
- The system provides an interactive way to evaluate restaurant performance.

