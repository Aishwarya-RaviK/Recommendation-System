import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
movies_list= pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_list)

similarity= pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
from PIL import Image
image = Image.open('popcorn.jpg')
st.image(image, caption='Grab you popcorn')

selected_movie_name = st.selectbox(
'What movie would you like to see?',movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
