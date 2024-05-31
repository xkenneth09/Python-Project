import streamlit as st
import pandas as pd


##
st.markdown('EDA Assingement Using Streamlit...')

st.title("Final EDA Assingement")

st.header('Netflix Project')

##
netflix = pd.read_csv(r"C:\Users\HWYA\Python Test\Project\Netflix_LY.csv")
st.dataframe(netflix.sample(5))

st.title('Dataset Review')

##
st.write("Description:")
st.write(netflix.describe(include = "all"))
##
st.write("Number of rows: ", netflix.shape[0])
st.write("Number of columns: ", netflix.shape[1])
st.write("Columns and Data Types: ")
st.write(netflix.dtypes)
##
st.write("Missing Values: ")
st.write(netflix.isnull().sum())

# 
st.write("Preview of the Dataset:")
if st.checkbox('Show The Dataset with dataframe'):
    chart_data = pd.DataFrame(netflix)
    chart_data


##
media = st.select_slider(
     'Select the type of the media!',
     options=['Movie', 'TV Show'])
st.write('The count of media according to ', media)    
st.title("The Types of Media On Netflix")
numb = netflix['type'].value_counts()
type = pd.DataFrame(numb)
st.bar_chart(type)
