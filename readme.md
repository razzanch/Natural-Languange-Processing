# Sentiment Analysis on Product Reviews

## 📌 Project Overview
This project analyzes sentiments in product reviews using various Natural Language Processing (NLP) techniques. I apply different text representations and train two models:
1. **Naïve Bayes (NB)** using TF-IDF
2. **BERT (Bidirectional Encoder Representations from Transformers)**

I compare their performance based on accuracy, precision, recall, and F1-score, and provide easy-to-use prediction scripts.

---

## 📂 Dataset
I use a dataset of product reviews obtained from Kaggle (**Threads_review.csv**). The dataset consists of:
- `review_description`: The textual review.
- `rating`: Numeric ratings (1-5).
- `sentiment`: Converted from rating:
  - **Positive**: Rating ≥ 4
  - **Neutral**: Rating = 3
  - **Negative**: Rating ≤ 2

---

## 📁 Project Structure
```
Sentiment-Analysis-Threads-Review/
│── data/
│   ├── Threads_review.csv           # Dataset from Kaggle
│── outputs/
│   ├── Output_Scenario_1.txt        # Experiment outputs
│   ├── Output_Scenario_2.txt
│── src/
│   ├── explore_data_threads_review.py  # Main exploration and testing
│   ├── libraryPUNKT.py               # PUNKT dependency file
│   ├── main.py                       # CLI interface for predictions
│   ├── predict_nb.py                 # Naïve Bayes prediction module
│   ├── predict_bert.py               # BERT prediction module
│── results/
│   ├── laporan_analisis.pdf          # Optional: Analysis report
│── models/                           # Trained models
│   ├── naive_bayes_model.pkl         # Saved Naïve Bayes model
│   ├── tfidf_vectorizer.pkl          # TF-IDF vectorizer
│   ├── bert_model/                   # Directory with trained BERT model
│── README.md                         # Project documentation
```

---

## 🔧 Setup Environment
To run this project, install the required dependencies:
```bash
pip install numpy pandas scikit-learn tensorflow torch transformers datasets nltk seaborn matplotlib
```

---

## 🏗 Data Preprocessing
1. **Handle Missing Values**: Remove rows with empty reviews or ratings.
2. **Text Cleaning**:
   - Convert text to lowercase.
   - Remove special characters and numbers.
3. **Tokenization**: Convert sentences into words.
4. **Stopwords Removal**: Remove common words like "the", "is", "and".
5. **Lemmatization**: Convert words to their base form (e.g., "running" → "run").

---

## 📊 Feature Representation
We convert text into numerical format using three methods:
1. **Bag of Words (BoW)** - (Optional)
2. **TF-IDF (Term Frequency - Inverse Document Frequency)** - Used for Naïve Bayes.
3. **Word Embeddings (Word2Vec)** - (Optional, as BERT already has transformer-based embeddings).

---

## 🏋️ Model Training

### 1️⃣ Naïve Bayes Classifier
- Uses **TF-IDF** as feature representation.
- Model: **MultinomialNB** from `sklearn.naive_bayes`.
- Split dataset (80% training, 20% testing).
- Evaluation Metrics: **Accuracy, Precision, Recall, F1-score**.

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
y_pred = nb_model.predict(X_test_tfidf)
print(classification_report(y_test, y_pred))
```

✅ **Model Saving**
```python
import pickle
pickle.dump(nb_model, open("models/naive_bayes_model.pkl", "wb"))
pickle.dump(vectorizer_tfidf, open("models/tfidf_vectorizer.pkl", "wb"))
```

---

### 2️⃣ BERT Transformer Model
- Uses **BERT-base-uncased** from `transformers`.
- Tokenizes input text.
- Fine-tunes BERT on sentiment classification task.
- Uses PyTorch for training.

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch.optim as optim

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
optimizer = optim.AdamW(model.parameters(), lr=5e-5)
```

✅ **Training Loop**
```python
for epoch in range(1):
    model.train()
    for batch in train_loader:
        optimizer.zero_grad()
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
```

✅ **Model Saving**
```python
model.save_pretrained("models/bert_model")
tokenizer.save_pretrained("models/bert_model")
```

---

## 📈 Model Evaluation
I compare **Naïve Bayes** and **BERT** using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**

| Model                 | Accuracy | Precision | Recall | F1-score |
|-----------------------|----------|-----------|--------|----------|
| Naïve Bayes           | 80.19%   | 0.74      | 0.80   | 0.77     |
| BERT (Early Stopping) | 67.02%   | 0.62      | 0.67   | 0.64     |
| BERT (NO Stopping)    | 81.69%   | 0.78      | 0.82   | 0.79     |

*Note: BERT trained with 1 epoch*

---

## 🚀 Using the Models

### Command Line Interface
Run the main program to analyze sentiments:
```bash
python src/main.py
```

This will prompt you to:
1. Choose a model (Naïve Bayes or BERT)
2. Enter a review text
3. View the sentiment prediction (Positive, Neutral, or Negative)

### Using Individual Prediction Modules

#### Naïve Bayes Prediction
```python
from predict_nb import predict_sentiment_nb

review = "I really love this product! It works exactly as described."
sentiment = predict_sentiment_nb(review)
print(sentiment)  # Output: 😊 Positive
```

#### BERT Prediction
```python
from predict_bert import predict_sentiment_bert

review = "The quality is okay but not worth the price."
sentiment = predict_sentiment_bert(review)
print(sentiment)  # Output: 😐 Neutral
```

---

## 📌 Conclusion
- **Naïve Bayes** performs well with TF-IDF but lacks deep semantic understanding.
- **BERT** achieves higher accuracy due to contextual embeddings but requires more computation.
- Use **Naïve Bayes** for lightweight tasks, and **BERT** for high-accuracy sentiment analysis.
- The project now includes ready-to-use prediction scripts and pre-trained models for immediate sentiment analysis.

---

## 🚀 Future Work
- Test with larger datasets.
- Experiment with LSTMs or Transformer variants (e.g., RoBERTa, DistilBERT).
- Optimize BERT training using techniques like learning rate scheduling.
- Create a web API for sentiment analysis.
- Add support for multi-language sentiment analysis.

---

## 👨‍💻 Author
- **Muhammad Razzan Carveyna Hibrizi** - Universitas Muhammadiyah Malang, Informatics Engineering

📌 *Feel free to contribute or reach out for collaboration!* 🚀
