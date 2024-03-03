import streamlit as st
import pandas as pd
from utils import get_poster,display_images

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
        # st.text(recomendation.index)
        x=recomendation.index
        poster=[get_poster(i) for i in x ]
        display_images(*poster)

def main():
    st.title('Movie Recomendor System')
    with st.container(border=True):
        title=st.selectbox('Please Select Movie',movie['title'].to_list())
    if st.button('Recomend'):
        show_recomendation(title)
        # l=['https://image.tmdb.org/t/p/original//sJpl1EfHGZhbKtZ3fWTlwrpM1tH.jpg',
        #     'https://image.tmdb.org/t/p/original//sJpl1EfHGZhbKtZ3fWTlwrpM1tH.jpg',
        #     'https://image.tmdb.org/t/p/original//sJpl1EfHGZhbKtZ3fWTlwrpM1tH.jpg',
        #     'https://image.tmdb.org/t/p/original//sJpl1EfHGZhbKtZ3fWTlwrpM1tH.jpg',
        #     'https://image.tmdb.org/t/p/original//sJpl1EfHGZhbKtZ3fWTlwrpM1tH.jpg',
        #     'https://image.tmdb.org/t/p/original//sJpl1EfHGZhbKtZ3fWTlwrpM1tH.jpg']
        # display_images(*l)
           
                
               

if __name__== "__main__":
    main()


