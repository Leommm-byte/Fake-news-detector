from flask import Flask, render_template, request, jsonify
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')


app = Flask(__name__)

model = pickle.load(open('model2.pkl', 'rb'))
tfidfvect = pickle.load(open('tfidfvect2.pkl', 'rb'))

ps = PorterStemmer()


def predict(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    review_vect = tfidfvect.transform([review])
    print(review_vect)
    print(model.predict(review_vect))
    prediction = 'This is Real news' if model.predict(review_vect) == 'REAL' else 'This is Fake news'

    return prediction


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def webapp():
    text = request.form['text']
    prediction = predict(text)
    return jsonify({'prediction': prediction})



if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
