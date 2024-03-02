import streamlit as st
import pandas as pd


movie=pd.read_csv('src/Dataset/tmdb_5000_credits.csv')

# Add the title
# st.title(f'Movie Recomendor System')

# # Add a Select box
# title=st.selectbox('Please Select Movie',movie['title'].to_list())
# from recomendor import get_recomend
# st.text(get_recomend(title))
def main():
    with st.container(border=True):
        st.title('Movie Recomendor System')
        title=st.selectbox('Please Select Movie',movie['title'].to_list())

if __name__== "__main__":
    main()


