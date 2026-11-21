import nltk
from nltk import sentiment
nltk.download("vader_lexicon")
sia = sentiment.SentimentIntensityAnalyzer();
import pandas as pd


df = pd.read_csv("feedback.csv");

def analyze_sentiment(feedback):
    score = sia.polarity_scores(feedback)["compound"]
    if score >= 0.05:
        sentiment = "positive";
    elif score <= -0.05:
        sentiment = "negative";
    else:
        sentiment = "neutral";
    return pd.Series([score,sentiment]);
df[["Sentiment_Score","Sentiment"]] = df["feedback"].apply(analyze_sentiment);
df.to_csv("newdata.csv",index=0);
            
            
