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
        
        return [title,poster,id]
    except:
        return 'Poster Not Found'
    

def display_images(*image):
    num_image = len(image)
    nbr_of_columns = st.columns(num_image)

    # if 'show_trailer' not in st.session_state:
    st.session_state['show_trailer'] = False
    # st.write(st.session_state['show_trailer'])
    for i in range(num_image):
        with nbr_of_columns[i]:
            try:
                st.image(image[i][1], caption=image[i][0], use_column_width='auto', width=150)

                trailer_key = fetch_trailer(image[i][2])
                if(trailer_key):
                    youtube_url = f"https://www.youtube.com/watch?v={trailer_key}"
                    st.video(youtube_url)
                    # with st.contaier():
                    #     youtube_url = f"https://www.youtube.com/watch?v={trailer_key}"
                    #     st.video(youtube_url)
                else:
                    st.write('trailer not found')
            except:
                st.warning(f"{image[i][0]}")



def fetch_trailer(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYWY0ZWJjNmVjM2EyMzA5NDZkNzNmOGYwMzIzMjhkNSIsInN1YiI6IjY1ZTNiMTUwMjc4ZDhhMDE4NWJmMjUzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JwkQZ10GMBKgtB-G-Dpr7HeyQUTgPojX-KzhCqhyRZ8"
    }

    response = requests.get(url, headers=headers)
    trailer_data = response.json()
    if trailer_data.get('results'):
        return trailer_data['results'][0]['key']
    else:
        return None
