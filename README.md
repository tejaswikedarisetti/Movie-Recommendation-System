# 🎬 Movie Recommendation System

This project is a **Python Streamlit web application** that recommends movies based on user preferences using **Collaborative Filtering**. It utilizes the **MovieLens dataset** and integrates the **TMDb API** to display movie posters, providing users with an interactive and personalized movie recommendation experience.

---

## 🚀 Project Features

- 🎥 Recommend similar movies using Collaborative Filtering
- 📊 Personalized movie recommendations
- 🖼️ Display movie posters using TMDb API
- 🔍 Search and select movies from an interactive interface
- ⚡ Fast and responsive Streamlit web application
- 📂 Uses the MovieLens dataset for recommendations
- 💻 Clean and user-friendly interface

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Framework | Streamlit |
| Libraries | Pandas, NumPy, Scikit-learn, Requests |
| Dataset | MovieLens Small Dataset |
| API | TMDb (The Movie Database) API |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── recommendation.py
├── movies.csv
├── ratings.csv
├── links.csv
├── tags.csv
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── images/
    ├── home.png
    ├── recommendations.png
    └── posters.png
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/tejaswikedarisetti/Movie-Recommendation-System.git

cd Movie-Recommendation-System
```

---

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 3. Configure TMDb API

Create a file named **.env**

Add your API Key

```text
TMDB_API_KEY=YOUR_TMDB_API_KEY
```

---

### 4. Run the Application

```bash
streamlit run app.py
```

Open your browser

```text
http://localhost:8501
```

---

## 📊 How It Works

The application performs the following steps:

- Loads the MovieLens dataset
- Processes movie ratings using Pandas
- Builds a movie similarity model using Collaborative Filtering
- Calculates similar movies using Scikit-learn
- Fetches movie posters from the TMDb API
- Displays recommended movies in a Streamlit interface

---

## 🎯 Key Features

- Movie Recommendation Engine
- Collaborative Filtering
- Movie Poster Integration
- Interactive User Interface
- Fast Recommendation Generation
- Personalized Suggestions

---

## 📂 Dataset

The project uses the **MovieLens Small Dataset**.

Dataset Files

- movies.csv
- ratings.csv
- links.csv
- tags.csv

Dataset contains

- Movie IDs
- Movie Titles
- Genres
- User Ratings
- Movie Tags

---

## 📸 Application Screens

- 🏠 Home Page
- 🎬 Movie Selection
- ⭐ Recommended Movies
- 🖼️ Movie Posters

(Add screenshots inside the **images** folder.)

---


## 📦 Requirements

```text
streamlit
pandas
numpy
scikit-learn
requests
python-dotenv
```

Or install using

```bash
pip install -r requirements.txt
```

---

## 🚀 Future Enhancements

- User Login & Authentication
- Content-Based Recommendation
- Hybrid Recommendation System
- Genre-Based Filtering
- Watchlist Feature
- Favorite Movies
- Movie Reviews
- IMDb Ratings Integration
- Deployment on Streamlit Cloud

---

## 📚 Learning Outcomes

- Python Programming
- Data Preprocessing
- Collaborative Filtering
- Recommendation Systems
- API Integration
- Streamlit Web Development
- Pandas & NumPy
- Scikit-learn
- Git & GitHub

---

## 👨‍💻 Author

**Sai Tejaswi**

GitHub: https://github.com/tejaswikedarisetti

