import sys
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec

sys.stdout.reconfigure(encoding="utf-8")  # Force stdout to use UTF-8 encoding

def vectorize_text(input_csv):
    # Load the CSV file
    df = pd.read_csv(input_csv)

    # Ensure the "Processed Text" column is treated as a string and tokenized properly
    df["Processed Text"] = df["Processed Text"].astype(str)  # Ensure it's a string
    tokenized_texts = [text.split() for text in df["Processed Text"]]  # Tokenize by splitting on spaces

    # **A. Bag of Words (BoW) with filtering**
    vectorizer_bow = CountVectorizer(max_features=2000, min_df=2, max_df=0.8, binary=False)
    bow_matrix = vectorizer_bow.fit_transform(df["Processed Text"])
    bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer_bow.get_feature_names_out())

    # **B. TF-IDF (Term Frequency-Inverse Document Frequency) with filtering**
    vectorizer_tfidf = TfidfVectorizer(max_features=2000, min_df=2, max_df=0.8)
    tfidf_matrix = vectorizer_tfidf.fit_transform(df["Processed Text"])
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer_tfidf.get_feature_names_out())

    # **C. Word Embeddings (Word2Vec)**
    word2vec_model = Word2Vec(sentences=tokenized_texts, vector_size=100, window=5, min_count=2, workers=4)
    word_embeddings = {word: word2vec_model.wv[word] for word in word2vec_model.wv.index_to_key}

    # **Print Sample Output**
    print("Bag of Words (BoW) Sample:\n", bow_df.head(10))  # Print more rows
    print("\nTF-IDF Sample:\n", tfidf_df.head(10))  # Print more rows
    print("\nWord2Vec Embedding Example:\n", list(word_embeddings.items())[:3])  # Print multiple words

if __name__ == "__main__":
    vectorize_text("datasets/processed_webdev_text.csv")
