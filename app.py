import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown

# TMDB API Key
API_KEY = "e04a738a5eb0b0798172f57508b48498"

# -------------------------------
# Download similarity.pkl from Google Drive
# -------------------------------
FILE_ID = "165Zb42pyu0jLwdBnjSHZb8r90HofgjcG"
OUTPUT = "similarity.pkl"

if not os.path.exists(OUTPUT):
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gdown.download(url, OUTPUT, quiet=False)

# -------------------------------
# Fetch movie poster
# -------------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("poster_path"):
        return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

# -------------------------------
# Recommend movies
# -------------------------------
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# -------------------------------
# Load Data
# -------------------------------
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open(OUTPUT, "rb"))

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button("Recommend Movies"):

    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
