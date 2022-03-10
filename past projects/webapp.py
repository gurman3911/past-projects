import streamlit as st
from mainModel import gpt3

st.title("Text Generation using GPT3")

st.header("Paragraph completion")

st.warning('this is made for assignment provided by the IConsultify for the intership only')

st.write('This program is made to complete or generate paragraph for the user as per the input given to the open ai model')
st.caption('The Davinci-001 api is used to complete or generate the set of text as per input')

content = st.text_input("enter the heading for the paragraph")
result = gpt3(content)

if st.button('show results'):

    st.write(result)
    
    st.success("The model program wroked sucessfully")
