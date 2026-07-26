import streamlit as st
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity
API_KEY = "871a151abc836deb7a62d60b1c203292"

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
links = pd.read_csv("data/links.csv")

# ---------------------------------------------------
# Merge Data
# ---------------------------------------------------
movie_data = pd.merge(ratings, movies, on="movieId")

# ---------------------------------------------------
# Top 10 Popular Movies
# ---------------------------------------------------
popular_movies = (
    movie_data.groupby("title")["rating"]
    .count()
    .sort_values(ascending=False)
    .head(10)
)

# ---------------------------------------------------
# Create User-Movie Matrix
# ---------------------------------------------------
movie_matrix = movie_data.pivot_table(
    index="userId",
    columns="title",
    values="rating"
).fillna(0)

# ---------------------------------------------------
# Calculate Cosine Similarity
# ---------------------------------------------------
similarity = cosine_similarity(movie_matrix.T)

similarity_df = pd.DataFrame(
    similarity,
    index=movie_matrix.columns,
    columns=movie_matrix.columns
)

# ---------------------------------------------------
# Recommendation Function
# ---------------------------------------------------
def recommend(movie_name):
    similar_movies = similarity_df[movie_name].sort_values(ascending=False)
    return similar_movies.iloc[1:11]


# ---------------------------------------------------
# Fetch Poster Function
# ---------------------------------------------------
def fetch_poster(movie_title):

    try:
        # Get movieId
        movie = movies[movies["title"] == movie_title]

        if movie.empty:
            return None

        movie_id = movie.iloc[0]["movieId"]

        # Get tmdbId
        link = links[links["movieId"] == movie_id]

        if link.empty:
            return None

        tmdb_id = link.iloc[0]["tmdbId"]

        if pd.isna(tmdb_id):
            return None

        tmdb_id = int(tmdb_id)

        # API URL
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        if "poster_path" not in data or data["poster_path"] is None:
            return None

        poster_url = (
            "https://image.tmdb.org/t/p/w500"
            + data["poster_path"]
        )

        return poster_url

    except:
        return None


# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("🔥 Top 10 Popular Movies")

for movie in popular_movies.index:
    st.sidebar.write(movie)

# ---------------------------------------------------
# Main Title
# ---------------------------------------------------
st.markdown(
    "<h1 style='text-align:center;'>🎬 Movie Recommendation System</h1>",
    unsafe_allow_html=True
)

st.markdown("""
Welcome to the Movie Recommendation System.

Select a movie and get 10 similar movie recommendations.
""")
# ---------------------------------------------------
# Movie Selection
# ---------------------------------------------------
movie_list = sorted(movie_matrix.columns)

selected_movie = st.selectbox(
    "🔍 Search or Select a Movie",
    movie_list
)

# ---------------------------------------------------
# Recommendation Button
# ---------------------------------------------------
if st.button("Recommend"):

    avg_rating = movie_data[
        movie_data["title"] == selected_movie
    ]["rating"].mean()

    total_ratings = movie_data[
        movie_data["title"] == selected_movie
    ]["rating"].count()

    st.subheader("📽 Selected Movie")

    st.write("⭐ Average Rating:", round(avg_rating, 2))
    st.write("👥 Total Ratings:", total_ratings)

    poster = fetch_poster(selected_movie)

    if poster:
        st.image(poster, width=250)

    st.markdown("---")

    st.subheader("🎥 Recommended Movies")

    recommendations = recommend(selected_movie)

    col1, col2 = st.columns(2)

    for i, movie in enumerate(recommendations.index):

        genre = movies[movies["title"] == movie]["genres"].values

        poster = fetch_poster(movie)

        if i % 2 == 0:

            with col1:

                st.markdown(f"### 🎬 {movie}")

                if len(genre) > 0:
                    st.write("🎭 Genre:", genre[0])

                if poster:
                    st.image(poster, width=200)
                else:
                    st.write("Poster not available")

                st.divider()

        else:

            with col2:

                st.markdown(f"### 🎬 {movie}")

                if len(genre) > 0:
                    st.write("🎭 Genre:", genre[0])

                if poster:
                    st.image(poster, width=200)
                else:
                    st.write("Poster not available")

                st.divider()

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
