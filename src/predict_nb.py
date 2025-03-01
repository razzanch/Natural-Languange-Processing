import pickle
import os

# Path ke models/
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models")

# Load model dan vectorizer
nb_model = pickle.load(open(os.path.join(MODEL_PATH, "naive_bayes_model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(MODEL_PATH, "tfidf_vectorizer.pkl"), "rb"))

def predict_sentiment_nb(text):
    text_tfidf = vectorizer.transform([text])  # Transformasi teks ke TF-IDF
    prediction = nb_model.predict(text_tfidf)[0]  # Prediksi sentimen
    
    if prediction == 1:
        return "😊 Positive"
    elif prediction == 0:
        return "😐 Neutral"
    else:
        return "😠 Negative"

if __name__ == "__main__":
    user_input = input("Enter a review: ")
    sentiment = predict_sentiment_nb(user_input)
    print(f"Naïve Bayes Sentiment: {sentiment}")
