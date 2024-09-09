from transformers import pipeline
import requests
import streamlit as st
from datetime import date

apiKey = "f1528ef99a144085abe5d1960473cbb3"


def fetch_sentiments(apiKey, keyword, date):
    url = f'https://newsapi.org/v2/everything?q={keyword}&from={date}&sortBy=popularity&apiKey={apiKey}'

    response = requests.get(url)
    if response.status_code != 200:
        st.error(f"Error fetching data : {response.status_code}")
        return None, None, None
    articles = response.json().get("articles", [])

    articles = [article for article in articles if
                keyword.lower() in str(article['title']).lower() or keyword.lower() in str(
                    article['description']).lower()]

    if not articles:
        st.warning('No articles matching the criteria were found.')
        return None, None, None
    pipe = pipeline("text-classification", model="ProsusAI/finbert")

    total_score = 0
    num_articles = 0
    sentiments = []
    for article in articles:
        title = article.get("title", "No title")
        description = article.get("description", "No description")
        content = article.get("content", "No content")

        sentiment = pipe(article["content"])[0]
        label = sentiment['label']
        score = sentiment['score']

        if sentiment['label'] == 'positive':
            total_score += sentiment['score']
            num_articles += 1

        elif sentiment['label'] == 'negative':
            total_score -= sentiment['score']
            num_articles += 1

        sentiments.append(
            {
                'title': title,
                'description': description,
                'content': content,
                'sentiment': label,
                'score': score
            }
        )

    final_score = total_score / num_articles if num_articles > 0 else 0
    overall_sentiment = "Positive" if final_score >= 0.15 else "Negative" if final_score <= -0.15 else "Neutral"

    return sentiments, final_score, overall_sentiment


st.title("Financial News Sentiment Portal")

keyword = st.text_input("Enter any company name or commodity")
date = st.date_input("Enter the date to start from ", date.today())

if st.button('Analyze the news'):
    with st.spinner("Fetching and analyzing news articles ....."):
        sentiments, final_score, overall_sentiment = fetch_sentiments(apiKey, keyword, date)

        if sentiments is not None and overall_sentiment is not None and final_score is not None:
            st.subheader("Sentiment Analysis results")
            st.write(f"Overall Sentiment : **{overall_sentiment}** with a score of **{final_score:.2f}**")

            st.subheader("Article Sentiments")

            for sentiment in sentiments:
                st.write(f"**Title**: {sentiment['title']}")
                st.write(f"**Description**: {sentiment['description']}")
                st.write(f"**Content**: {sentiment['content']}")
                st.write(f"**Sentiment**: {sentiment['sentiment']} with a score of {sentiment['score']:.2f}")
                st.write("---")

        else:
            st.warning("No valid articles found or an error occurred during the sentiment analysis.")
