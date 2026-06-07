import streamlit as st
import pickle
import os
import gdown

# Download similarity.pkl if not present
if not os.path.exists("artifacts/similarity.pkl"):
    url = "https://drive.google.com/uc?export=download&id=1FK_CwMhrOuuv041M8GZicPFypQnoMgwV"
    gdown.download(url, "artifacts/similarity.pkl", quiet=False)

# Load data
movies = pickle.load(open("artifacts/movies.pkl", "rb"))
similarity = pickle.load(open("artifacts/similarity.pkl", "rb"))


# Recommendation function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


# Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(movie)