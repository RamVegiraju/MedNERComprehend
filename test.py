import requests
import json
import streamlit as st

#Headings for Application
st.title("Medical NER with AWS Comprehend Medical Example")
st.subheader("Enter the text you would like to analyze below")
inputText = st.text_input('Enter text') #text is stored in this variable

#Function to hit API GW and Lambda function for Entity Detection
def detectEntities(inputText):
    inputObj = {"Input": inputText}
    url = "https://80g6psdc39.execute-api.us-east-1.amazonaws.com/prod/medner"
    x = requests.post(url, data = json.dumps(inputObj))
    resDict = x.text
    res = json.loads(resDict)
    resEntities = res["body"]["Entities"]
    resText = [i['Text'] for i in resEntities]
    resCategories = [i['Category'] for i in resEntities]
    entDict = dict(zip(resText, resCategories))
    return entDict
 
st.subheader("Entities Detected")
st.write(detectEntities(inputText))
