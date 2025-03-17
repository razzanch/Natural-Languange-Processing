import csv
import re
import nltk
from nltk.corpus import stopwords
import string

# Download stopwords jika belum ada
nltk.download('stopwords')
nltk.download('punkt')

def clean_csv_and_preprocess(input_file, output_file):
    # Load stopwords
    stop_words = set(stopwords.words('english'))
    
    def preprocess_text(text):
        # Lowercase the text
        text = text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenize the text
        tokens = nltk.word_tokenize(text)
        
        # Remove stopwords and non-alphabetic tokens
        tokens = [word for word in tokens if word not in stop_words and word.isalpha()]
        
        # Join tokens back into a string
        return " ".join(tokens)
    
    fixed_rows = []
    
    # Increase the field size limit
    csv.field_size_limit(1000000)  # Naikkan batas maksimum field
    
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header
        
        current_url = None
        current_text = ""
        
        for row in reader:
            if len(row) >= 2:  # Ensure row has at least two columns
                url, text = row[0], row[1]
                
                # Check if the first column is a valid URL
                if re.match(r'^https?://', url):
                    # If we already have a valid URL and text, save it
                    if current_url and current_text.strip():
                        fixed_rows.append([current_url, current_text.strip()])
                    
                    # Start a new entry
                    current_url = url
                    current_text = text
                else:
                    # Append to the current text if the URL is invalid
                    current_text += " " + url + " " + text
        
        # Add the last entry
        if current_url and current_text.strip():
            fixed_rows.append([current_url, current_text.strip()])
    
    # Preprocess the text samples
    preprocessed_rows = []
    for url, text in fixed_rows:
        cleaned_text = preprocess_text(text)
        preprocessed_rows.append([url, cleaned_text])
    
    # Save the cleaned and preprocessed data to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Cleaned Text"])
        writer.writerows(preprocessed_rows)
    
    print(f"Data cleaned and preprocessed. Saved to {output_file}")

# Run the function
input_csv = "merged_TextSample.csv"
output_csv = "datasets/cleaned_webdev_text_samples.csv"
clean_csv_and_preprocess(input_csv, output_csv)