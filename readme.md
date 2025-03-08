# PDF Text Summarization using TF-IDF

## 📌 Overview
This project extracts text from a PDF file, cleans unnecessary metadata, and summarizes the content using **TF-IDF (Term Frequency-Inverse Document Frequency)**. The goal is to generate concise summaries while preserving key information.

## 🚀 Features
- Extracts text from PDF using **PyMuPDF (fitz)**.
- Cleans text by removing **DOI, URLs, emails, citations, and metadata**.
- Uses **TF-IDF Vectorizer** to identify and rank the most informative sentences.
- Generates a summary based on **sentence scoring and thresholding**.
- Adjustable summary length to fit user needs.

## 🛠 Requirements
Make sure you have the following dependencies installed before running the script:

```bash
pip install pymupdf scikit-learn nltk
```

Additionally, download the necessary NLTK resources (only needed once):

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## 📂 File Structure
```
project-folder/
│── summarize.py         # Main script
│── README.md       # Project documentation
│── sample.pdf      # Example PDF file for testing
```

## 🔧 Usage
### 1️⃣ Run the script with a PDF file
Replace `sample.pdf` with your actual PDF file path:
```python
pdf_path = 'sample.pdf'  # Change this to your file path
summary = main(pdf_path, summary_length=10)  # Adjust summary length as needed
print("Summary:")
print(summary)
```

### 2️⃣ Modify summary length
Adjust `summary_length` parameter to change the number of sentences in the output summary.

## 📑 How It Works
1. **Extract Text**: Reads the PDF content and extracts raw text.
2. **Clean Text**: Removes unnecessary information such as DOI, URLs, citations, and references.
3. **Tokenization & TF-IDF Processing**:
   - Splits text into sentences.
   - Computes **TF-IDF scores** for each sentence.
   - Selects sentences with the highest relevance.
4. **Summarization**:
   - Sentences with scores above a calculated **threshold** are selected.
   - The summary length is controlled by `summary_length`.

## 📌 Example Output
**Input PDF Content (simplified):**
```
Abstract: This paper discusses sentiment analysis... (Full text extracted from PDF)
...
Conclusion: The model achieved 89% accuracy...
```

**Generated Summary:**
```
The paper discusses sentiment analysis and compares various NLP models.
The best model achieved an accuracy of 89% using Bi-LSTM and BERT embeddings.
...
```

## 📌 Future Improvements
- Implement **BERT-based summarization** for better contextual understanding.
- Add **Graph-based ranking algorithms** like TextRank for better sentence selection.
- Support **multiple PDF processing** in batch mode.

## 💡 Credits
Developed by **Muhammad Razzan Carveyna Hibrizi** | Inspired by NLP techniques in text summarization.

---
**Happy Coding! 🚀**

