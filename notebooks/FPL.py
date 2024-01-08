### CODING AN APP IN STREAMLIT

### import libraries
import pandas as pd
import numpy as np
import streamlit as st
import joblib

#####################################################################################################################################
### Create a title
st.title("Fantasy Premier League Point Predictor")

st.write('Welcome to the FPL Point Prediction App! Use this interactive tool to predict total number of points a player would get in a specific game. Simply adjust the sliders on the sidebar to input your values and see how the changes input affect the predicted score based on the model. The model used for this prediction is the Gradient Boost model')


#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file


######################################################################################################################################
# Press R in the app to refresh after changing the code and saving here

### You can try each method by uncommenting each of the lines of code in this section in turn and rerunning the app

### You can also use markdown syntax.
#st.write('# Our last morning kick off :sob:')

### To position text and color, you can use html syntax
#st.markdown("<h1 style='text-align: center; color: blue;'>Our last morning kick off</h1>", unsafe_allow_html=True)


#######################################################################################################################################
# Create a header
st.subheader("Data")

# DATA LOADING
df = pd.read_csv('/Users/mu-izzgbadamosi/Downloads/Capstone Project/data/cleaned.csv',index_col=0)


### C. Display the dataframe in the app
st.dataframe(df.head(6))

#######################################################################################################################################


#######################################################################################################################################
### MODEL INFERENCE: we use Gradient Boosting model for prediction

# Create a header
st.subheader("Users Input")

# Load the model using joblib
model = joblib.load('/Users/mu-izzgbadamosi/Downloads/Capstone Project/notebooks/gb_model.pkl')

# Create a header
st.sidebar.header("User Input")

### create sliders for the features


goals_scored = st.sidebar.slider("Goals Scored", min_value=0, max_value=6, step=1)


minutes = st.sidebar.slider("Minutes played", min_value=0, max_value=90, step=1)


clean_sheets = st.sidebar.checkbox("Did this player have a clean sheet?")
# Convert 'holiday' to 0 or 1
clean_sheets_encoded = 1 if clean_sheets else 0


position_DEF = st.sidebar.checkbox("Is this player a Defender?")
# Convert 'holiday' to 0 or 1
position_DEF_encoded = 1 if position_DEF else 0

bps = st.sidebar.slider("Bonus points", min_value=0, max_value=6, step=1)

assists = st.sidebar.slider("Assists", min_value=0, max_value=6, step=1)


goals_conceded = st.sidebar.slider("Goals Conceded", min_value=0, max_value=10, step=1)

position_MID = st.sidebar.checkbox("Is this player a Midfielder?")

position_MID_encoded = 1 if position_DEF else 0

saves = st.sidebar.slider("Saves", min_value=0, max_value=6, step=1)

red_cards = st.sidebar.slider("Red cards", min_value=0, max_value=1, step=1)

value = st.sidebar.slider("Player Value", min_value=40, max_value=150, step=5)


##########################################################################################################################
# Make a prediction based on user input
input_data = pd.DataFrame({'goals_scored':[goals_scored],
                           'minutes':[minutes],
                           'position_DEF':[position_DEF_encoded],
                           'clean_sheets':[clean_sheets],
                           'bps':[bps],
                           'assists':[assists],
                           'goals_conceded':[goals_conceded],
                           'position_MID': [position_MID_encoded],
                           'saves': [saves], 
                           'red_cards': [red_cards],
                           'value':[value]})

# display user input
st.dataframe(input_data)

# create a subheader
st.subheader("Predict Total Points using Gradient Boosting")



pro_input_data = pd.DataFrame({
                           'const':[1],
                           'xP': [1],
                           'assists':[assists],
                           'bps':[bps],
                           'clean_sheets':[clean_sheets],
                           'expected_assists':[1],
                           'expected_goals':[1],
                           'goals_conceded':[goals_conceded],
                           'goals_scored':[goals_scored],
                           'minutes':[minutes],
                           'own_goals':[0],
                           'penalties_missed':[0],
                           'penalties_saved':[0],
                           'red_cards': [red_cards],
                           'saves': [saves], 
                           'team_a_score':[0],
                           'team_h_score':[0],
                           'transfers_in':[0],
                           'value':[value],
                           'yellow_cards':[0],
                           'position_DEF':[position_DEF_encoded],
                           'position_MID': [position_MID_encoded],
                           'form':[0],
                           'minutes_lag1':[0],
                           'bps_lag1':[0],
                           'value_lag1':[0],
                           'transfers_in_lag1':[0],
                           'transfers_out_lag1':[0]})

# predict the pro_input_data
prediction = model.predict(pro_input_data)

# round the prediction value
rounded_prediction= int(np.round(prediction))

# create a box and display the rounded prediction value inside that
st.markdown(
    f'<div style="display: flex; justify-content: center; align-items: center; width: 60px; height: 30px; border: 2px solid blue; border-radius: 5px;">'
    f'<span style="color: #04F5FF; font-weight: bold; font-size: 28px ;">{rounded_prediction}</span>'
    f'</div>',
    unsafe_allow_html=True
)



