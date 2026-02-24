import requests
import streamlit as st


url=" https://api.nasa.gov/planetary/apod?api_key=WSsdHYPPhpratZkc1DuH38LTYWqQEgbBDNH1YxDT"
request=requests.get(url)
content=request.json()
print(content)

img=requests.get(content["hdurl"])
img2=requests.get(content["url"])

st.title(content["title"])
st.subheader(content["date"])
st.image(img.content)
st.write(content["explanation"])
st.subheader("The Seen Planets Are")
st.image(img2.content)