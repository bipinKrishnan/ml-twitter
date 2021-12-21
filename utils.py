import requests
import streamlit as st
import streamlit.components.v1 as components


@st.cache
def get_tweet(url):
    api = f"https://publish.twitter.com/oembed?url={url}&maxwidth=400&theme=dark"
    content = requests.get(api).json()
    return content

def display_page(urls_path):
    columns = st.columns([1, 1, 1])

    with open(urls_path, "r") as f:
        urls = f.readlines()
        
        for i in range(0, len(urls)-3, 3):
            with columns[0]:
                st.write("-"*10)
                components.html(get_tweet(urls[i])['html'], height=283, scrolling=True)

            with columns[1]:
                st.write("-"*10)
                components.html(get_tweet(urls[i+1])['html'], height=283, scrolling=True)

            with columns[2]:
                st.write("-"*10)
                components.html(get_tweet(urls[i+2])['html'], height=283, scrolling=True) 