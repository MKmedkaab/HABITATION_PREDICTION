import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open('BEST_model.pkl', 'rb')
predictor = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(a, b, c, d, e, f, g):
    
    names=['Date', 'Property Type', 'Old/New','Duration', 'PAON', 'County', 'PPD Category Type']
    df=pd.DataFrame(columns=names)
    #print(df)    
    df_new_row = pd.DataFrame(data=np.array([[a, b, c, d, e, f, g]]),columns=names)
    df=pd.concat([df,df_new_row], ignore_index=True)
    #print(df)
    #print(df['Date'])
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype('category')
            df[col] = df[col].cat.codes
    #print(df.info())
    
    prediction = predictor.predict(df)
    #print(prediction)
    return prediction
      

# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("HABITATION PRICE PREDICTION")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Habitation price predictor ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    Date = st.text_input("Date (2021)", "Type Here")
    Property_Type = st.text_input("Property type: D = Detached, S = Semi-Detached, T = Terraced, F = Flats/Maisonettes, O = Other", "Type Here")
    Old_New = st.text_input("Old/New: Y = a newly built property, N = an established residential building", "Type Here")
    Duration = st.text_input("Duration: F = Freehold, L= Leasehold", "Type Here")
    PAON=st.text_input("Primary Addressable Object Name", "Type Here")
    County= st.text_input("County", "Type Here")
    PPD_Category_Type=st.text_input("PPD Category Type: A = Standard Price Paid entry, B = Additional Price Paid entry", "Type Here")
    
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(Date, Property_Type, Old_New, Duration, PAON, County, PPD_Category_Type)
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()