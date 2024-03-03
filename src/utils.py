# Get movie poster
import streamlit as st
import requests
def get_poster(id):
    import requests
    try:
        url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYWY0ZWJjNmVjM2EyMzA5NDZkNzNmOGYwMzIzMjhkNSIsInN1YiI6IjY1ZTNiMTUwMjc4ZDhhMDE4NWJmMjUzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JwkQZ10GMBKgtB-G-Dpr7HeyQUTgPojX-KzhCqhyRZ8"
        }

        response = requests.get(url, headers=headers)
        response=response.json()
        
        title=response['title']
        poster='https://image.tmdb.org/t/p/original//'+ response['poster_path']
        
        return [title,poster]
    except:
        return 'Poster Not Found'
    

def display_images(*image):
    num_image=len(image)
    nbr_of_columns=st.columns(num_image)

    for i in range(num_image):
        with nbr_of_columns[i]:
            try:
                st.image(image[i][1],caption=image[i][0],use_column_width='auto',width=150)
            except:
                st.warning(f"{image[i][0]}")

