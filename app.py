import streamlit as st
from pathlib import Path

from utils import get_tweet, display_page

path = Path("urls")

st.set_page_config(
        page_title='MLBookmark',
        page_icon='🔖',
        layout='wide',
        initial_sidebar_state='collapsed'
        )

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
option = st.radio(
    label="",
    options=["Learning resources", "Threads", "Quick tips", "Tools", "Updates"]
)

if option.lower()=="learning resources":
    display_page(path/"learning_resources")

elif option.lower()=="threads":
    display_page(path/"threads")

elif option.lower()=="quick tips":
    display_page(path/"quick_tips")

elif option.lower()=="tools":
    display_page(path/"tools")

elif option.lower()=="updates":
    display_page(path/"updates")
