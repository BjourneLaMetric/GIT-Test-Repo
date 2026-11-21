import nltk 
from nltk import sentiment
import pandas as pd

df = pd.read_csv("data.csv")
print(df)

def sentiet_analyzer (feedback):
    scores = sentiment.SentimentIntensityAnalyzer.polarity_scores(feedback)["compound"]
    for score in scores:
        if score >= 0.05:
            sentiment = "positive"
        elif score <= -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"
    return pd.Series([score,sentiment])              
df[["Sentiment_Scores","Sentiment"]] = df["CanteenFeedback"].apply(sentiet_analyzer) 
df.to_csv("newdata.csv",index = 0)
