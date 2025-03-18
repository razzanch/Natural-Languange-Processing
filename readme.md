# Text Representation and Vectorization

## Project Overview
This project explores different text vectorization techniques for Natural Language Processing (NLP), including Bag of Words (BoW), Term Frequency-Inverse Document Frequency (TF-IDF), and Word Embeddings (Word2Vec). The goal is to compare these techniques in terms of semantic representation, efficiency, and suitability for further NLP tasks like sentiment analysis and text classification.

## Author Information
- **Name:** Muhammad Razzan Carveyna Hibrizi  
- **Program:** Informatics Engineering  
- **University:** Universitas Muhammadiyah Malang  
- **Class:** NLP (C)  

## Project Structure
```
├── datasets
│   ├── cleaned_webdev_text_sample.csv   # Preprocessed dataset
│   ├── processed_webdev_text_sample.csv # Vectorized dataset
│
├── preprocessing
│   ├── text_preprocessing.py            # Functions for text cleaning and tokenization
│
├── vectorization
│   ├── text_vectorization.py            # Implements BoW, TF-IDF, and Word2Vec vectorization
│
├── report
│   ├── analysis.md                       # Report and comparison of vectorization techniques
│
├── main.py                              # Main execution file
```

## Installation and Dependencies
To run this project, install the required dependencies using:
```bash
pip install -r requirements.txt
```
Ensure you have the following libraries:
- pandas
- numpy
- scikit-learn
- gensim
- nltk

## How to Run the Project
1. **Data Preprocessing:**
   ```bash
   python preprocessing/text_preprocessing.py
   ```
   This script cleans and tokenizes the dataset, removing stopwords and normalizing text.

2. **Text Vectorization:**
   ```bash
   python vectorization/text_vectorization.py
   ```
   This script applies BoW, TF-IDF, and Word Embeddings (Word2Vec) on the dataset.

3. **Run Main Program:**
   ```bash
   python main.py
   ```
   This will execute the full pipeline and generate vectorized outputs for further analysis.

## Analysis and Interpretation
### Best Representation Technique
From the results, **Word Embeddings (Word2Vec)** provides the best representation compared to BoW and TF-IDF due to:
- **Semantic Representation:** Captures word meaning, unlike BoW and TF-IDF.
- **Fixed-Dimension Output:** More efficient than high-dimensional sparse matrices from BoW and TF-IDF.
- **Context Awareness:** Understands the relationships between words.

### Comparison of Methods
| Technique | Advantages | Disadvantages |
|-----------|------------|----------------|
| **BoW** | Simple, interpretable | Ignores word order, high dimensionality |
| **TF-IDF** | Weighs words based on importance | Still ignores context, sparse representation |
| **Word2Vec** | Captures semantic meaning, efficient | Requires large corpus for training |

## Future Improvements
- Implement **BERT embeddings** for deeper semantic understanding.
- Apply different datasets to test model generalization.
- Perform **text classification** to compare the performance of vectorization techniques.

## Conclusion
Word Embeddings (Word2Vec) is the most effective technique for this dataset, as it captures semantic meaning while keeping dimensionality manageable. However, BoW and TF-IDF still have their use cases in simpler NLP tasks.

---
### Contact & Support
For any questions, feel free to reach out via email or discussion forums related to NLP research.

