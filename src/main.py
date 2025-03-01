import sys
import os

# Tambahkan path src ke sys.path agar bisa mengimpor modul predict_nb dan predict_bert
sys.path.append(os.path.dirname(__file__))

from predict_nb import predict_sentiment_nb
from predict_bert import predict_sentiment_bert

def main():
    print("\n=== Sentiment Analysis ===")
    print("1. Naïve Bayes (TF-IDF)")
    print("2. BERT Transformer")
    choice = input("Choose a model (1/2): ")

    review = input("\nEnter a review: ")

    if choice == "1":
        sentiment = predict_sentiment_nb(review)
        print(f"\n✅ Naïve Bayes Prediction: {sentiment}")
    elif choice == "2":
        sentiment = predict_sentiment_bert(review)
        print(f"\n✅ BERT Prediction: {sentiment}")
    else:
        print("\n❌ Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
