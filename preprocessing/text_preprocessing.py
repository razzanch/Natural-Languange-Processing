import csv
import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary resources if not already downloaded
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Clean and preprocess text: remove URLs, special characters, numbers, stopwords, and perform lemmatization."""
    if not isinstance(text, str):  # Ensure input is a string
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # Remove non-alphabetic characters and extra whitespace
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords and lemmatize words
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    return " ".join(tokens)

def clean_and_preprocess_csv(input_csv, output_csv):
    """Read CSV, preprocess text, and save cleaned data to a new CSV file."""
    print("[STEP 2] Preprocessing Text...")

    processed_rows = []
    csv.field_size_limit(1000000)  # Increase field size limit for large text fields

    with open(input_csv, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header
        
        for row in reader:
            if len(row) >= 2:
                url, text = row[0], row[1]
                processed_text = preprocess_text(text)
                processed_rows.append([url, processed_text])
    
    # Save preprocessed data
    with open(output_csv, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Processed Text"])  # Write header
        writer.writerows(processed_rows)

    print(f"Preprocessing complete! Data saved to '{output_csv}'.")

if __name__ == "__main__":
    input_csv = "datasets/cleaned_webdev_text_samples.csv"
    output_csv = "datasets/processed_webdev_text.csv"
    clean_and_preprocess_csv(input_csv, output_csv)
