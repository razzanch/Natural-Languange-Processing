import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import nltk
import re

# Download NLTK data (hanya perlu dilakukan sekali)
nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    """
    Mengekstrak teks dari file PDF menggunakan PyMuPDF.
    """
    text = ''
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def clean_text(text):
    """
    Membersihkan teks dari informasi yang tidak relevan.
    """
    # Hapus DOI, URL, dan informasi metadata
    text = re.sub(r'DOI:\s*\S+', '', text)
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'ISSN\s*\d+-\d+', '', text)
    text = re.sub(r'\(Received:.*?\)', '', text)
    text = re.sub(r'\b\w+@\w+\.\w+\b', '', text)  # Hapus email
    text = re.sub(r'\s+', ' ', text)  # Hapus spasi berlebihan
    
    # Hapus judul, abstrak, dan bagian yang tidak relevan
    text = re.sub(r'BAREKENG:.*?ABSTRACT', '', text, flags=re.DOTALL)
    text = re.sub(r'ABSTRACT.*?Introduction', '', text, flags=re.DOTALL)
    text = re.sub(r'Article History:.*?\n', '', text, flags=re.DOTALL)
    text = re.sub(r'REFERENCES.*', '', text, flags=re.DOTALL)  # Hapus referensi
    text = re.sub(r'\[\d+\].*?\n', '', text)  # Hapus kutipan seperti [12]
    
    return text.strip()

def summarize_text(text, summary_length=5):
    """
    Melakukan summarization menggunakan TF-IDF dengan logika yang diberikan.
    """
    # Tokenize teks menjadi kalimat
    sentences = sent_tokenize(text)
    
    # Training TF-IDF Vectorizer pada kalimat
    vectorizer = TfidfVectorizer(stop_words='english')
    features = vectorizer.fit_transform(sentences)
    
    # Inisialisasi variabel
    sent_scores = []
    
    # Hitung skor TF-IDF untuk setiap kalimat
    for i in features:
        sent_score = i.sum()
        sent_length = len(i.data)
        avg_score = sent_score / sent_length if sent_length > 0 else 0
        sent_scores.append(avg_score)
    
    # Hitung threshold (rata-rata skor kalimat)
    threshold = sum(sent_scores) / len(sent_scores) * 0.8  # Kurangi threshold
    
    # Inisialisasi summary akhir
    final_summ = ""
    
    # Ambil kalimat yang memiliki skor di atas threshold
    for index, data in enumerate(sent_scores):
        if data >= threshold:
            final_summ = final_summ + " " + sentences[index]
    
    # Batasi jumlah kalimat dalam summary
    final_sentences = sent_tokenize(final_summ)
    final_summ = ' '.join(final_sentences[:summary_length])
    
    return final_summ

def main(pdf_path, summary_length=5):
    """
    Fungsi utama untuk menjalankan summarization.
    """
    # Ekstrak teks dari PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Bersihkan teks
    text = clean_text(text)
    
    # Lakukan summarization
    summary = summarize_text(text, summary_length)
    
    return summary

# Contoh penggunaan
pdf_path = '#10 23775-50667-2-PB.pdf'  # Ganti dengan path file PDF Anda
summary = main(pdf_path, summary_length=10)  # Sesuaikan jumlah kalimat yang diinginkan
print("Summary:")
print(summary)

