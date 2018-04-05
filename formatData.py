import sys
import csv
import pandas
import json
from tweet import Tweet

def importCSV(csvFilename):
    raw = pandas.read_csv(csvFilename)
    fields = list(raw)
    data = []
    for x in raw.values.tolist():
        data.append({k: v for k, v in zip(fields, x)})
    return data

def loadTweets(filename):
    data = importCSV(filename)
    return [Tweet(d) for d in data]

def loadData(filename):
    with open(filename, 'r') as infile:
        return json.load(infile)

def collectAll(tweetFile, dataFiles):
    ''' Assumes order is preserved between files'''
    tweets = loadTweets(tweetFile)
    for f in dataFiles:
        dat = loadData(f)
        for tweet, elm in zip(tweets, dat):
            if isinstance(elm, dict):
                for key, val in elm.items():
                    tweet.data[key] = val
            else:
                tweet.data[f] = elm
    return tweets

def dumpAll(tweets, filename):
    tweetData = []
    fields = filter(lambda x: x != 'sentence', tweets[0].data.keys())
    fields.extend(['date', 'time'])
    for tweet in tweets:
        tData = tweet.data
        del tData['sentence']
        tData['date'] = tweet.date
        tData['time'] = tweet.time
        tweetData.append(tData)

    with open(filename, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fields)
        writer.writeheader()
        for dat in tweetData:
            try:
                writer.writerow(dat)
            except Exception as e:
                print(dat)
                raise e


def main():
    DATAFILES = sys.argv[1:]
    TWEET_FILE = 'data/tweetsSince2014.csv'
    OUTFILE = 'FormattedData.csv'

    tweets = collectAll(TWEET_FILE, DATAFILES)
    dumpAll(tweets, OUTFILE)

if __name__ == '__main__':
    main()
