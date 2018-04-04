#!/usr/bin/python3.5
from tweet import Tweet

def analyzeTweets(tweetFilename, analysis_strategy):
    examples = Tweet.fromTweetFile(tweetFilename)

    sentences = []
    for example in examples:
        try:
            sen = example.full_text
        except AttributeError:
            sen = example.text

        sentences.append(sen)

    return analysis_strategy(sentences)


if __name__ == "__main__":
    from nltkProof import nltkStrategy
    import json
    data = analyzeTweets('trump-tweets.json', nltkStrategy)
    with open('outfile.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
