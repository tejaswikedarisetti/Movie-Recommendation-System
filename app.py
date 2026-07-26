import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

movie_data = pd.merge(ratings, movies, on="movieId")

movie_matrix = movie_data.pivot_table(
    index="userId",
    columns="title",
    values="rating"
).fillna(0)

# Calculate similarity between movies
similarity = cosine_similarity(movie_matrix.T)

similarity_df = pd.DataFrame(
    similarity,
    index=movie_matrix.columns,
    columns=movie_matrix.columns
)

print(similarity_df.head())

def recommend(movie_name):
    similar_scores = similarity_df[movie_name]
    similar_movies = similar_scores.sort_values(ascending=False)
    return similar_movies.iloc[1:11]

print(recommend("Toy Story (1995)"))