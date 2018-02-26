#!/usr/bin/python3.5
from nltk.sentiment.vader import SentimentIntensityAnalyzer
print('\n\n=======')

sid = SentimentIntensityAnalyzer()

with open('input.txt') as infile:
    examples = infile.readlines()

for example in examples:
    s = sid.polarity_scores(example)
    print('\nSentence: ' + example)
    out = []
    for k in sorted(s):
        out.append("{}: {}".format(k, s[k]))

    print(', '.join(out))


