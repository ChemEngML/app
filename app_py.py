

# Import necessary libraries
import pycaret
from pycaret.regression import predict_model, load_model
import pandas as pd
import streamlit as st
import numpy as np

# Set page configuration
st.set_page_config(page_title="FO Performance Predictor", page_icon="3105807.png")
st.image("Desalination_hero.width-2000.jpg", width = 1000)

# Import machine learning model
model = load_model('GradientBoostingRegressor')

# Import dataset & choosing desired parameters to analyze
df = pd.read_csv("Database.csv")

# Defining app's characteristics
def app(): 
    st.title('💦 Water Flux (LMH) Predictor 💦')
    st.header('Welcome to my web app!')
    st.subheader('Please input your values for the following features:')

    MP_Type = df["Micro Pollutant"].unique()
    MB_Type = df["Type of MB"].unique()
    DS_Type = df["Draw Solution"].unique()

    MP = st.selectbox("Micropollutant:", MP_Type)
    MB = st.selectbox("Membrane Type:", MB_Type)
    MP_Conc = st.number_input("MP Concentration (mg/L):", 0.0, 100.0, format="%.7f")
    MP_MW = st.number_input("MP Molecular Weigth (g/mol):", 0.0, 1000.0, format="%.2f")
    Charge = st.slider("MP Charge:", -1, 1)
    FS_pH = st.slider("FS pH:", 0.0, 14.0, step=0.05)
    Contact_angle = st.number_input("MB Contact Angle (°):", 0.0, 110.0, format="%.2f")
    DS = st.selectbox("Draw Solute:", DS_Type)
    DS_MW = st.number_input("DS Molecular Weigth (g/mol):", 0, 999)
    DS_Conc = st.number_input("DS Concentration (M):", 0, 99)
    Op_Time = st.number_input("Operation Time (h):", 0, 72)
    Velocity = st.number_input("Cross-Flow Velocity (cm/s):", 0.0, 50.0, format="%.2f")
    Temp = st.slider("Temperature (⁰C)", 0.0, 40.0, step=0.5)
    Rejection = st.slider("Rejection Rate (%)", 0, 100)

# Perform the prediction based on the user input
    def predict():      
        input_data = {
            'Micro Pollutant': MP,
            'Type of MB': MB,
            'Initial Concentration of MP (mg/L)': MP_Conc,
            'Compound MW (g/mol)': MP_MW,
            'Compound Charge': Charge,
            'Initial FS pH': FS_pH,
            'MB Contact Angle (°)': Contact_angle,
            'Draw Solution': DS,
            'DS MW (g mol-1)': DS_MW,
            'DS Concentration (M)': DS_Conc,
            'Operating Time (h)': Op_Time,
            'Cross Flow Velocity (cm/s)': Velocity,
            'Temperature (⁰C)': Temp,
            'Removal Rate (%)': Rejection
        }

        input_df = pd.DataFrame([input_data])
#if st.button("Predict"):
        prediction = predict_model(model, input_df)
        st.write('The predicted water flux is:', prediction)

    trigger = st.button('Predict', on_click=predict)

# Remove made by streamlit footer
hide_menu_style="""
	<style>
	footer{visibility:hidden;}
	</style>
	"""
st.markdown(hide_menu_style, unsafe_allow_html=True)
# Run Streamlit app
if __name__ == '__main__':
    app()

