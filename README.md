# 📚 Book Recommender System

A machine learning-powered book recommendation engine built with Python and scikit-learn, using **K-Nearest Neighbors with cosine similarity** to suggest books based on real user rating patterns.

🚀 **Live Demo:** (https://book-recommender-system-project-oo5p.onrender.com)

---

## ✅ Project Status: Completed & Deployed

---

## 🚀 Features

- **Collaborative Filtering via KNN** — Recommends books by finding the most similar ones based on shared user rating behavior
- **Sparse Matrix Optimization** — Converts the user-item matrix to a CSR sparse matrix for memory efficiency
- **Smart Data Filtering** — Retains only users with 200+ ratings and books with 50+ ratings to reduce sparsity and improve recommendation quality
- **`recommend_books()` Function** — Clean, reusable function to get top-5 similar books for any given title
- **Deployed Web App** — Served via Flask on Render with a templated UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.10+ |
| Data Processing | pandas, NumPy |
| ML Model | scikit-learn (`NearestNeighbors`) |
| Sparse Matrix | scipy (`csr_matrix`) |
| Visualization | matplotlib, seaborn |
| Web Framework | Flask |
| WSGI Server | Gunicorn |
| Deployment | Render |
| Data Versioning | DVC |

---

## 📁 Project Structure

```
book-recommender-system/
│
├── notebook/
│   └── EDA___Feature_Engineering.ipynb   # Full EDA, preprocessing & model
│
├── templates/              # HTML templates for Flask UI
│
├── app.py                  # Flask app — main entry point
├── books.pkl               # Serialized books dataframe
├── model.pkl               # Trained KNN model
├── final_df.pkl            # Processed final ratings dataframe
├── pt.pkl                  # Pivot table (book-user matrix)
│
├── Procfile
├── requirements.txt
├── .dvcignore
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Local Setup

1. **Clone the repository**
   ```bash
   git clone (https://github.com/fureza-muqaddas/Book-Recommender-System-Project.git)
   cd book-recommender-system-project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```
   Visit `http://localhost:5000`

---

## 🧠 How It Works

### Step 1 — Load & Inspect the Data
Three datasets are loaded: `Books.csv`, `Users.csv`, and `Ratings.csv` from the Book-Crossing dataset.

```python
books = pd.read_csv("Books.csv", encoding="latin-1")
users = pd.read_csv("Users.csv", encoding="latin-1")
ratings = pd.read_csv("Ratings.csv", encoding="latin-1")
```

---

### Step 2 — Filter for Quality Signal

**Active users only** — Users with fewer than 200 ratings are dropped:
```python
active_users = ratings['user_id'].value_counts()
active_users = active_users[active_users > 200].index
ratings = ratings[ratings['user_id'].isin(active_users)]
```

**Popular books only** — Books with fewer than 50 ratings are dropped:
```python
final_ratings_50 = final_ratings[final_ratings['number_of_ratings'] >= 50]
```

> This step significantly reduces sparsity and noise in the model.

---

### Step 3 — Build the Pivot Table

A book-user matrix is created: rows = book titles, columns = user IDs, values = ratings. Missing values are filled with 0.

```python
pt = final_ratings_50.pivot_table(
    index='title',
    columns='user_id',
    values='rating'
).fillna(0)
```

---

### Step 4 — Convert to Sparse Matrix

To handle the large number of zeros efficiently:

```python
from scipy.sparse import csr_matrix
pt_sparse = csr_matrix(pt.values)
```

---

### Step 5 — Train the KNN Model

A K-Nearest Neighbors model using **cosine distance** is fitted on the sparse matrix:

```python
from sklearn.neighbors import NearestNeighbors

model = NearestNeighbors(metric='cosine')
model.fit(pt_sparse)
```

---

### Step 6 — Generate Recommendations

```python
def recommend_books(book_title):
    book_index = np.where(pt.index == book_title)[0][0]
    distances, suggestions = model.kneighbors(
        pt.iloc[book_index, :].values.reshape(1, -1),
        n_neighbors=6
    )
    recommended_books = []
    for i in suggestions[0][1:]:
        recommended_books.append(pt.index[i])
    return recommended_books
```

**Example:**
```python
recommend_books("The Secret Garden")
```

---

## 🔬 Model Observations

- When tested on **Harry Potter and the Chamber of Secrets**, the model returned other Harry Potter titles — confirming it accurately captures series-level similarity from user rating behavior.
- Some recommendations overlapped across different input books, likely due to **dataset sparsity** or highly popular books acting as common nearest neighbors.
- Recommendations are stronger for books with a richer rating history.

---

## 📊 Dataset

(https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data?select=Books.csv) — real-world book ratings collected from the Book-Crossing community.

| File | Description |
|------|-------------|
| `Books.csv` | ISBN, title, author, year, publisher, cover image URL |
| `Users.csv` | User ID, location, age |
| `Ratings.csv` | User ID, ISBN, rating (0–10) |

**After filtering:**

| Metric | Value |
|--------|-------|
| Min ratings per user | 200+ |
| Min ratings per book | 50+ |
| Rating scale | 0 – 10 |
| Skew | Heavily skewed toward 0 (implicit) and 7–10 (explicit) |

---

## 🌐 Deployment on Render

Deployed as a web service on [Render](https://render.com), served with **Gunicorn** as the production WSGI server.

**Procfile:**
```
web: gunicorn app:app
```

To deploy your own:
1. Fork this repo
2. Create a new **Web Service** on Render
3. Connect your GitHub repo and set the start command to `gunicorn app:app`

---

## Screenshots

### Recommendation Results

![Recommendation Results](<img src="images_recommendation.png" alt="Recommendation Results" width="800">)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Your Name**  
GitHub: [@fureza-muqaddas](https://github.com/fureza-muqaddas)  
LinkedIn: [fureza-muqaddas](https://www.linkedin.com/in/fureza-muqaddas/)

---

> ⭐ If you found this useful, give it a star — it helps others discover the project!