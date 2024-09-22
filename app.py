import streamlit as st
import pickle
import pandas as pd

import requests




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  
    distances = similarity[movie_index]
    
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    
    # Print the recommended movie titles
    recommended_movies=[]

    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title) 
    return recommended_movies       
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similrity.pkl','rb'))
st.title('Movie Recommender System')

option = st.selectbox(
    'Which movie suggestion would you like',
    movies['title'].values

)

if st.button('recommend'):
    recommendtions = recommend(option)

    for i in recommendtions:
        st.write(i)

