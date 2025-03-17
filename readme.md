# Data Scraping and Preprocessing Project

## Author
**Muhammad Razzan Carveyna Hibrizi**  
**NIM: 202210370311445**  
**Class: NLP(A)**  

## Objective
This project is aimed at scraping real-world text data, preprocessing it, and preparing it for further NLP model evaluation. The focus is on web development topics, as the data will be used in future model training to predict which programming languages or frameworks will be dominant in the long run.

## Task Breakdown
1. **Data Source Selection**  
   - The data is scraped from various web development blogs and websites.
   
2. **Data Scraping**  
   - The script scrapes web development articles from over 200 sources.
   - Two Python scripts (`web_dev_scrap.py` and `web_dev_scrap2.py`) run concurrently to speed up the scraping process.
   - The data is saved in a CSV file (`datasets/webdev_text_samples.csv`).

3. **Preprocessing the Data**  
   - A script (`web_dev_clean.py`) is used to clean the scraped data by:
     - Converting text to lowercase.
     - Removing punctuation.
     - Tokenizing text.
     - Removing stopwords.
     - Performing lemmatization.
   - The cleaned text is stored in a new CSV file (`datasets/webdev_cleaned_text.csv`).

## Folder Structure
```
├── scraping
│   ├── web_dev_scrap.py
│   ├── web_dev_scrap2.py
│
├── preprocessing
│   ├── web_dev_clean.py
│
├── datasets
│   ├── webdev_text_samples.csv
│   ├── webdev_cleaned_text.csv
```

## Dependencies
Make sure to install the required Python packages before running the scripts.
```bash
pip install requests beautifulsoup4 nltk pandas
```

## How to Run
1. **Scrape Data**
   ```bash
   python scraping/web_dev_scrap.py & python scraping/web_dev_scrap2.py
   ```
2. **Preprocess Data**
   ```bash
   python preprocessing/web_dev_clean.py
   ```

## Output
- The raw scraped text is stored in `datasets/webdev_text_samples.csv`.
- The cleaned text is stored in `datasets/webdev_cleaned_text.csv`.

## Notes
- Random delays are introduced to prevent request blocking.
- Data is collected from multiple sources for diversity and completeness.
- Preprocessing includes lemmatization to enhance text normalization.

## Future Enhancements
- Implement multi-threading for faster data collection.
- Expand the data sources to include more diverse topics.
- Enhance text preprocessing with additional NLP techniques like named entity recognition (NER).