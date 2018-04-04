#!/usr/bin/python3.5
from tweet import Tweet
import json

def analyzeTweets(tweetFilename, analysis_strategy):
    examples = Tweet.fromTweetFile(tweetFilename)[:100]

    sentences = []
    for example in examples:
        try:
            sen = example.full_text
        except AttributeError:
            sen = example.text

        sentences.append(sen)

    return analysis_strategy(sentences)

def outputJSON(outfile, data, fileMode='w'):
    print('Writing data to ' + outfile)
    with open(outfile, fileMode) as outfile:
        json.dump(data, outfile, indent=4)

def doNLTK():
    from nltkProof import nltkStrategy
    print('Running NLTK sentiment')
    data = analyzeTweets('trump-tweets.json', nltkStrategy)
    outputJSON('nltk-out.json', data)

def doIndico(method):
    from indicoProof import indicoStrategyFactory
    data = analyzeTweets('trump-tweets.json', indicoStrategyFactory(method))
    outputJSON('indico-{}-out.json'.format(method), data)

if __name__ == "__main__":
    #doNLTK()
    for m in ['political', 'twitter_engagement', 'sentiment_hq', 'organizations', 'personality', 'places']:
        doIndico(m)
