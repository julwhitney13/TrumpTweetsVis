#!/usr/bin/python3.5
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweet import Tweet
print('\n\n=======')

sid = SentimentIntensityAnalyzer()

examples = Tweet.fromTweetFile('trump-tweets.json')

for example in examples:
    try:
        sen = example.full_text
    except AttributeError:
        print("No full_text, trying text")
        sen = example.text

    s = sid.polarity_scores(sen)

    print('\nSentence: ' + sen)
    out = []
    for k in sorted(s):
        out.append("{}: {}".format(k, s[k]))

    print(', '.join(out))


