import streamlit as st

# News item data
news_items = [
    {
        "image_url": "https://i1-suckhoe.vnecdn.net/2023/02/12/crop-legs-running-upstairs-1303-1676156457.jpg?w=1020&h=0&q=100&dpr=1&fit=crop&s=RADljfCia0eDPLFBFxlzDw",
        "summary": "This is a summary of the first news item",
        "url": "https://vnexpress.net/tap-luyen-tranh-thu-cho-nguoi-ban-ron-4569578.html"
    },
    {
        "image_url": "https://vnexpress.net/mac-covid-19-khi-lao-dong-duoc-huong-bao-hiem-xa-hoi-4569104.html",
        "summary": "This is a summary of the second news item",
        "url": "https://vnexpress.net/mac-covid-19-khi-lao-dong-duoc-huong-bao-hiem-xa-hoi-4569104.html"
    },
    # {
    #     "image_url": "https://www.example.com/image3.jpg",
    #     "summary": "This is a summary of the third news item",
    #     "url": "https://www.example.com/news3"
    # },
]

# Loop through the news items and display them in a row
st.header("News")
for item in news_items:
    st.image(item["image_url"], width=100)
    st.write(item["summary"])
    st.write("Read more:", item["url"])
    st.write("---")
