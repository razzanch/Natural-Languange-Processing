import torch
import os
from transformers import BertTokenizer, BertForSequenceClassification

# Path ke models/
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "bert_model")

# Load tokenizer dan model BERT yang sudah dilatih
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

def predict_sentiment_bert(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()

    if prediction == 2:
        return "😊 Positive"
    elif prediction == 1:
        return "😐 Neutral"
    else:
        return "😠 Negative"

if __name__ == "__main__":
    user_input = input("Enter a review: ")
    sentiment = predict_sentiment_bert(user_input)
    print(f"BERT Sentiment: {sentiment}")
