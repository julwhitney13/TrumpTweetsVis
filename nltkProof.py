#!/usr/bin/python3.5
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def nltkStrategy(sentences):

    sid = SentimentIntensityAnalyzer()
    out = []
    for sen in sentences:
        s = sid.polarity_scores(sen)
        out.append({
            'tweet': sen,
            'sentiment': s
        })
    return out
