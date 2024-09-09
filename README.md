# FinancialSentimentAnalyzer
Here's a README file for your GitHub repository:

---

# 📰 Financial Sentiment Analyzer

This repository contains a Financial Sentiment Analyzer built using Python. The application leverages the `transformers`, `requests`, and `streamlit` libraries to analyze sentiment in financial news articles fetched from various sources. The sentiment analysis is powered by a model specifically trained on financial data (`ProsusAI/finbert`).

## 🚀 Features

- **News API Integration**: Fetches financial news articles from the News API based on user-defined keywords.
- **Sentiment Analysis**: Uses the `ProsusAI/finbert` model from the `transformers` library to perform sentiment analysis on the news articles.
- **User-Friendly Interface**: Provides a simple and intuitive web-based UI using Streamlit.
- **Real-Time Analysis**: Fetches and analyzes news articles in real-time.

## 📦 Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/financial-sentiment-analyzer.git
cd financial-sentiment-analyzer
pip install -r requirements.txt
```

### Dependencies

- `transformers`: Library for state-of-the-art NLP models.
- `requests`: Simple HTTP library for Python.
- `streamlit`: An open-source app framework for Machine Learning and Data Science.
- `feedparser`: Library for parsing RSS feeds (if using RSS instead of News API).

You can install all dependencies using the following command:

```bash
pip install -r requirements.txt
```

## 🔧 Usage

### 1. News API Configuration

To use the News API, you'll need to sign up for an API key at [NewsAPI.org](https://newsapi.org/).

### 2. Running the Application

Run the Streamlit app using the following command:

```bash
streamlit run financeChat.py
```

### 3. Input Parameters

- **Keyword**: Enter the keyword to search for in financial news (e.g., "Tesla", "stock market").
- **Date**: Specify the start date for fetching articles (default is today’s date).

### 4. Sentiment Analysis Output

The application will display:
- **Article Title**: Title of the news article.
- **Published Date**: Date the article was published.
- **Sentiment**: Sentiment of the article content (Positive, Negative, or Neutral).
- **Score**: Confidence score of the sentiment analysis.

## 📁 Project Structure

```plaintext
financial-sentiment-analyzer/
│
├── financeChat.py          # Main Streamlit application file
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🛠️ Development

To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## 🙏 Acknowledgments

- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [Streamlit](https://github.com/streamlit/streamlit)
- [NewsAPI](https://newsapi.org/)

---
Idea taken from NeuralNine Youtube Channel......
