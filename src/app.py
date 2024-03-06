import streamlit as st
import pandas as pd
from utils import get_poster,display_images,fetch_trailer

# Read The Data
movie=pd.read_csv('src/Dataset/tmdb_5000_credits.csv')

def pagination():
    st.set_page_config(
    page_title="Movies Recomendor System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="auto"
    )
def show_recomendation(title):
    with st.spinner('Recomendation is processing...'):
        from recomendor import get_recomend
        recomendation=get_recomend(title)
        # st.text(recomendation)
        x=recomendation['id'].to_list()
        poster=[get_poster(i) for i in x ]
        display_images(*poster)

def main():
    st.title('Movie Recomendor System')
    with st.container(border=True):
        title=st.selectbox('Please Select Movie',movie['title'].to_list())
    if st.button('Recommend'):
        show_recomendation(title)
      
                    

if __name__== "__main__":
    main()

