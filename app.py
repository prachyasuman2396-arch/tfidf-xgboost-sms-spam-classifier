from flask import Flask, render_template, request
import pickle
import numpy as np
import re
from scipy.sparse import hstack

app = Flask(__name__)

# Load saved model artifacts
with open("xgboost_spam_model.pkl", "rb") as f:
    artifacts = pickle.load(f)

word_tfidf = artifacts["word_tfidf"]
char_tfidf = artifacts["char_tfidf"]
model = artifacts["model"]
threshold = artifacts.get("threshold", 0.5)

# Text cleaning (MUST match training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    message = ""

    if request.method == "POST":
        message = request.form["sms"]

        clean_msg = clean_text(message)

        # TF-IDF features
        X_word = word_tfidf.transform([clean_msg])
        X_char = char_tfidf.transform([clean_msg])

        # Engineered features (same order as training)
        msg_len = len(clean_msg)
        has_numbers = int(any(c.isdigit() for c in clean_msg))
        has_free = int("free" in clean_msg)

        X_extra = np.array([[msg_len, has_numbers, has_free]])

        # Combine all features
        X_final = hstack([X_word, X_char, X_extra]).toarray()

        # Prediction
        prob = model.predict_proba(X_final)[0][1]
        prediction = "SPAM " if prob > threshold else "HAM "
        confidence = round(prob * 100, 2)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
