from flask import Flask, render_template, request
import pickle
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

# load pickle files
final_ratings_50 = pickle.load(open('final_df.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def recommend_book(book_name):
    book_name = book_name.strip()

    if book_name not in pt.index:
        return []

    book_index = np.where(pt.index == book_name)[0][0]

    distances, suggestions = model.kneighbors(
        pt.iloc[book_index, :].values.reshape(1, -1),
        n_neighbors=6
    )

    data = []

    for i in suggestions[0][1:]:
        temp_df = books[books['title'] == pt.index[i]].drop_duplicates('title')

        item = {
            'title': temp_df['title'].values[0],
            'author': temp_df['author'].values[0],
            'image': temp_df['image_url'].values[0]
        }

        data.append(item)

    return data


@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(final_ratings_50['title'].values),
        author=list(final_ratings_50['author'].values),
        image=list(final_ratings_50['image_url'].values),
        votes=list(final_ratings_50['number_of_ratings'].values),
        ratings=list(final_ratings_50['rating'].values),
        data=None
    )


@app.route('/recommend', methods=['POST'])
def recommend():
    user_book = request.form.get('user_book')
    data = recommend_book(user_book)

    return render_template(
        'index.html',
        book_name=list(final_ratings_50['title'].values),
        author=list(final_ratings_50['author'].values),
        image=list(final_ratings_50['image_url'].values),
        votes=list(final_ratings_50['number_of_ratings'].values),
        ratings=list(final_ratings_50['rating'].values),
        data=data,
        searched_book=user_book
    )

if __name__ == '__main__':
    app.run(debug=True)