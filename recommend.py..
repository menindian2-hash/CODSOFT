# recommend.py
# Simple Recommendation System without pandas

# Our movie "database"
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6},
    {"title": "Avengers: Endgame", "genre": "Action", "rating": 8.4},
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
    {"title": "The Lion King", "genre": "Animation", "rating": 8.5}
]

def recommend_movies(genre, min_rating=0):
    results = []
    for movie in movies:
        if movie["genre"].lower() == genre.lower() and movie["rating"] >= min_rating:
            results.append(movie)
    return results

# Main program
print("===== Movie Recommendation System =====")
print("Available genres: Sci-Fi, Action, Drama, Animation")

genre = input("👉 Enter a genre: ")
min_rating = float(input("👉 Minimum rating (0-10): "))

recommended = recommend_movies(genre, min_rating)

if recommended:
    print(f"\n🎬 Recommended {genre} movies (rating ≥ {min_rating}):\n")
    for movie in recommended:
        print(f"- {movie['title']} (⭐ {movie['rating']})")
else:
    print("\n❌ No movies found with your criteria.")