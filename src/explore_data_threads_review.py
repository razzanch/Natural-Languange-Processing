#=================================
#=================================
#STEP 1 : SETUP LINGKUNGAN KERJA
#=================================
#=================================
    #pip install numpy pandas scikit-learn tensorflow torch transformers datasets nltk seaborn matplotlib


#=================================
#=================================
#STEP 2 : Dataset dari Kaggle
#=================================
#=================================
    #kata kunci seperti "sentiment analysis reviews"
    #wajib mencari dataset yang:
        #1. Punya kolom teks (misalnya: review_text, text, comment).
        #2. Punya kolom label sentimen (misalnya: sentiment, label, rating).


#==============================================
#==============================================
# STEP 3: EXPLORATING AND PRE-PROCESSING DATA
#==============================================
#==============================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk

# 1. Load dataset
df = pd.read_csv("data/threads_reviews.csv")

# 2. Cek missing values
print("Jumlah data kosong per kolom:")
print(df.isnull().sum())

# Hapus data yang kosong di kolom review atau rating
df = df.dropna(subset=["review_description", "rating"])

# 3. Tampilkan beberapa sampel data
print(df.head())

# 4. Cek jumlah data dan tipe data
print(df.info())

# 5. Cek distribusi rating
plt.figure(figsize=(8,5))
sns.countplot(x=df["rating"], palette="coolwarm")
plt.xlabel("Rating")
plt.ylabel("Jumlah Review")
plt.title("Distribusi Rating")
plt.show()

# 6. Konversi rating ke sentimen
def convert_rating_to_sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"

df["sentiment"] = df["rating"].apply(convert_rating_to_sentiment)

# Cek hasil konversi
print(df[["review_description", "rating", "sentiment"]].head())

# 7. Cek distribusi sentimen
plt.figure(figsize=(8,5))
sns.countplot(x=df["sentiment"], palette="coolwarm", order=["Negative", "Neutral", "Positive"])
plt.xlabel("Sentimen")
plt.ylabel("Jumlah Review")
plt.title("Distribusi Sentimen")
plt.show()

# 8. Membersihkan teks (hapus karakter khusus, angka, ubah ke lowercase)
def clean_text(text):
    text = text.lower()  # Ubah ke huruf kecil
    text = re.sub(r"[^a-z\s]", "", text)  # Hanya menyisakan huruf dan spasi
    return text

df["cleaned_review"] = df["review_description"].apply(clean_text)

# Cek hasil pembersihan teks
print(df[["review_description", "cleaned_review"]].head())

# 9. Tokenisasi (ubah teks menjadi daftar kata)
nltk.download('punkt')
from nltk.tokenize import word_tokenize

df["tokens"] = df["cleaned_review"].apply(word_tokenize)

# Cek hasil tokenisasi
print(df[["cleaned_review", "tokens"]].head())

# 10. Menghapus Stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

df["filtered_tokens"] = df["tokens"].apply(remove_stopwords)

# Cek hasil penghapusan stopwords
print(df[["tokens", "filtered_tokens"]].head())

# 11. Lemmatization (mengubah kata menjadi bentuk dasar)
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def lemmatize_words(tokens):
    return [lemmatizer.lemmatize(word) for word in tokens]

df["lemmatized_tokens"] = df["filtered_tokens"].apply(lemmatize_words)

# Cek hasil lemmatization
print(df[["filtered_tokens", "lemmatized_tokens"]].head())




#=======================================================================================
#=======================================================================================
#STEP 4 REPRESENTASI TEKS (BoW, TF-IDF, Word Embeddings) CONVERTING STRING TO NUMBER
#=======================================================================================
#=======================================================================================

#1. BAG OF WORD (OPSIONAL)

from sklearn.feature_extraction.text import CountVectorizer

# Inisialisasi CountVectorizer
vectorizer_bow = CountVectorizer()

# Transformasi teks menjadi vektor BoW
X_bow = vectorizer_bow.fit_transform(df["cleaned_review"])

# Lihat ukuran matriks BoW
print("Shape dari BoW:", X_bow.shape)

# Contoh beberapa fitur (kata) yang dipakai
print("Fitur BoW:", vectorizer_bow.get_feature_names_out()[:20])


#2. TF-IDF (Term Frequency - Inverse Document Frequency) (PILIH YANG INI UNTUK NANTI TRAINING NAIVE BAYES)

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TF-IDF Vectorizer
vectorizer_tfidf = TfidfVectorizer()

# Transformasi teks menjadi vektor TF-IDF
X_tfidf = vectorizer_tfidf.fit_transform(df["cleaned_review"])

# Lihat ukuran matriks TF-IDF
print("Shape dari TF-IDF:", X_tfidf.shape)

# Contoh beberapa fitur (kata) yang dipakai
print("Fitur TF-IDF:", vectorizer_tfidf.get_feature_names_out()[:20])


#3. Word Embeddings (Word2Vec) (OPSIONAL KARENA UNTUK TRAINING BERT SUDAH ADA TRANFORMER-BASED EMBEDDINGS)

import gensim
from gensim.models import Word2Vec

# Latih model Word2Vec dari data token yang telah diproses
model_w2v = Word2Vec(sentences=df["lemmatized_tokens"], vector_size=100, window=5, min_count=2, workers=4)

# Cek representasi vektor dari kata tertentu
print("Vektor kata 'app':", model_w2v.wv["app"])

# Lihat ukuran vektor per kata
print("Dimensi vektor Word2Vec:", model_w2v.wv.vector_size)



#======================================
#======================================
#STEP 5 : MODEL TRAINING (NAÏVE BAYES)
#======================================
#======================================

#1. Bagi Data Menjadi Training & Testing Set
from sklearn.model_selection import train_test_split

# Pisahkan fitur (X) dan label (y)
X = df["cleaned_review"]  # Teks review yang sudah dibersihkan
y = df["sentiment"]  # Label sentimen (Positive, Neutral, Negative)

# Bagi data 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Jumlah data latih:", len(X_train))
print("Jumlah data uji:", len(X_test))


#2. Konversi Teks ke Vektor (TF-IDF & BoW)
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# BoW (Bag of Words)
vectorizer_bow = CountVectorizer()
X_train_bow = vectorizer_bow.fit_transform(X_train)
X_test_bow = vectorizer_bow.transform(X_test)

# TF-IDF (Term Frequency - Inverse Document Frequency)
vectorizer_tfidf = TfidfVectorizer()
X_train_tfidf = vectorizer_tfidf.fit_transform(X_train)
X_test_tfidf = vectorizer_tfidf.transform(X_test)

print("BoW shape:", X_train_bow.shape)
print("TF-IDF shape:", X_train_tfidf.shape)



#3. Train Model Naïve Bayes dengan TF-IDF

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Buat model Naïve Bayes
nb_model = MultinomialNB()

# Latih model dengan TF-IDF
nb_model.fit(X_train_tfidf, y_train)

# Prediksi
y_pred = nb_model.predict(X_test_tfidf)

print("Training Model Naïve Bayes Selesai!")

# Evaluasi
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 4. Simpan Model Naïve Bayes dan TF-IDF Vectorizer
import pickle
import os

# Buat folder models/ jika belum ada
os.makedirs("models", exist_ok=True)

# Simpan Model Naïve Bayes
with open("models/naive_bayes_model.pkl", "wb") as f:
    pickle.dump(nb_model, f)

# Simpan TF-IDF Vectorizer
with open("models/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer_tfidf, f)



#=================================
#=================================
#STEP 6: MODEL TRAINING (BERT)
#=================================
#=================================

import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, Dataset, random_split
import torch.optim as optim
from tqdm import tqdm
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Tokenizer dan Model BERT
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)

# 2. Konversi Label Sentimen ke Angka
label_mapping = {"Negative": 0, "Neutral": 1, "Positive": 2}
df["sentiment_label"] = df["sentiment"].map(label_mapping)

# 3. Tokenisasi Semua Teks
def encode_texts(texts, max_length=128):
    return tokenizer(texts.tolist(), padding=True, truncation=True, max_length=max_length, return_tensors="pt")

X_encoded = encode_texts(df["cleaned_review"])
y_encoded = torch.tensor(df["sentiment_label"].values)

# 4. Buat Dataset PyTorch
class SentimentDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item["labels"] = self.labels[idx]
        return item

dataset = SentimentDataset(X_encoded, y_encoded)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

# 5. Dataloader untuk Training
train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=8, shuffle=False)

# 6. Training Model BERT
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

optimizer = optim.AdamW(model.parameters(), lr=5e-5)

epochs = 1  # Target 1 epoch

for epoch in range(epochs):
    model.train()
    loop = tqdm(train_loader, leave=True)
    
    for batch in loop:
        batch = {key: val.to(device) for key, val in batch.items()}  
        optimizer.zero_grad()
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        loop.set_description(f"Epoch {epoch+1}")
        loop.set_postfix(loss=loss.item())

print("Training Model Bert Selesai!")

# 7. Evaluasi Model BERT
model.eval()
y_true, y_pred = [], []

with torch.no_grad():
    for batch in test_loader:
        batch = {key: val.to(device) for key, val in batch.items()}
        outputs = model(**batch)
        predictions = torch.argmax(outputs.logits, dim=-1)
        
        y_true.extend(batch["labels"].cpu().numpy())
        y_pred.extend(predictions.cpu().numpy())

# Evaluasi dengan Sklearn
print("Hasil Evaluasi Model BERT:")
print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}")
print(classification_report(y_true, y_pred, target_names=["Negative", "Neutral", "Positive"]))


# 8. Simpan Model BERT
# Buat folder models/ jika belum ada
os.makedirs("models/bert_model", exist_ok=True)

# Simpan model BERT
model.save_pretrained("models/bert_model")
tokenizer.save_pretrained("models/bert_model")

print("Model BERT telah disimpan di folder models/bert_model/")





