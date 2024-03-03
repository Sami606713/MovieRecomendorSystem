import pandas as pd
import numpy as np
import ast
import requests



credit=pd.read_csv('src/Dataset/tmdb_5000_credits.csv')
movie=pd.read_csv('src/Dataset/tmdb_5000_movies.csv')

 
movies=credit.merge(movie)

movies=movies[['id','title','cast','crew','genres','keywords','tagline','overview']]

def preprocess(text):
    text=ast.literal_eval(text)
    
    new_list=[]
    for i in text:
        new_list.append(i['name'])
    return new_list

movies['genres']=movies['genres'].apply(preprocess)

movies['keywords']=movies['keywords'].apply(preprocess)

def preprocess2(text):
    text=ast.literal_eval(text)
    
    new_list=[]
    flag=0
    for i in text:
        if(flag<=5):
            new_list.append(i['name'])
            flag+=1
        else:
            break
    return new_list

movies['cast']=movies['cast'].apply(preprocess2)

movies['crew']=movies['crew'].apply(preprocess2)

def list_to_string(list_):
    return ','.join(list_)

# Convert list to string so that i cancombine it
movies['cast']=movies['cast'].apply(list_to_string)
movies['crew']=movies['crew'].apply(list_to_string)
movies['genres']=movies['genres'].apply(list_to_string)
movies['keywords']=movies['keywords'].apply(list_to_string)

# Replace Space with empty string
movies['cast']=movies['cast'].str.replace(" ","")
movies['crew']=movies['crew'].str.replace(" ","")
movies['genres']=movies['genres'].str.replace(" ","")
movies['keywords']=movies['keywords'].str.replace(" ","")
movies['tagline']=movies['tagline'].str.replace(" ","")
movies['overview']=movies['overview'].str.replace(" ","")

# Make a tag col
movies['tags']=movies['overview']+' '+movies['tagline']+' '+movies['keywords']+' '+movies['crew']+' '+movies['cast']+' '+movies['genres']

# it a good practice to copy the dataframe
movies_df=movies.copy()

# get the title and tag columns only and replce null value with empty space
movies_df=movies_df[['id','title','tags']]
movies_df.fillna('',inplace=True)

# now convert text int vector
from sklearn.feature_extraction.text import TfidfVectorizer
vector=TfidfVectorizer(stop_words='english',max_features=1000)
metrix=vector.fit_transform(movies_df['tags'])

# Calculate the simularity score of each movie
from sklearn.metrics.pairwise import linear_kernel
cosign_simularity=linear_kernel(metrix,metrix)

# now make a recomendation function
def get_recomend(title,cosign_simularity=cosign_simularity,nbr_of_recomendation=5):
    """
    1-Find the movies that are give by user and get the index of the movies.
    2-calculate the simularity score of the movies by using movie index with each other movies.
    3-After finding the score use enumunrate function to get the index and score and store in a variable.
    4-Now them sort using value not index into decending order.
    5-After 4 step we have simiar movie and their index.
    6-Find the index form the dataframe that we can get after 4 step and retur the title.
    """
    movie_idx=movies_df[movies_df['title']==title].index[0]
    
    sim_score=cosign_simularity[movie_idx]
    
    index_value=list(enumerate(sim_score))
    
    recomend=sorted(index_value,key=lambda x:x[1],reverse=True)
    
    recomend=recomend[0:nbr_of_recomendation]
    
    list_index=[i[0] for i in recomend]
    
    return movies_df[['id','title']].iloc[list_index]

# print(get_recomend('Superman Returns'))

