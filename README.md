# 🎬 Movie Recommendation System

## 📌 Overview

This project is a **Content-Based Movie Recommendation System** developed using **Python**, **Machine Learning**, and **Streamlit**. The application recommends movies similar to the user's selected movie based on content similarity.

The recommendation model uses **CountVectorizer** and **Cosine Similarity** to identify movies with similar features such as genres, keywords, cast, crew, and overview.

---

## 🚀 Features

* 🎥 Recommend similar movies
* 🖼️ Display movie posters using TMDB API
* 🎯 Interactive Streamlit web interface
* ⚡ Fast content-based recommendations
* 📱 Simple and user-friendly interface

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Requests
* Pickle

---

## 📂 Dataset

The project uses the **TMDB 5000 Movie Dataset**.

Files:

* tmdb_5000_movies.csv
* tmdb_5000_credits.csv

---

## 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── model.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── models/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── assets/
│   └── screenshots/
│
└── notebooks/
    └── movie_recommendation.ipynb
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Movie-Recommendation-System.git
```

Move into the project folder:

```bash
cd Movie-Recommendation-System
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

##  Screenshots

Add screenshots of your Streamlit application inside the **assets/screenshots** folder.
![Home Page](assets/screenshots/home_page.png)

## 🔮 Future Improvements

* Search autocomplete
* Genre-based filtering
* Movie ratings
* Movie trailers
* Top-rated and trending movies
* Responsive UI
* User authentication

---

## 👩‍💻 Author

**Summaiya Bibi**

Machine Learning & Data Science Enthusiast

GitHub: https://github.com/summaiyazafar

LinkedIn: https://linkedin.com/in/summaiya-bibi/
