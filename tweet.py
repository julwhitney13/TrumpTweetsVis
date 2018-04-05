import json
import re

class Tweet():
    TEMPLATE = """
    Source: {source}
    Text: {text}
    Retweets: {retweet_count}
    Favorites: {favorite_count}
    Created At: {created_at}
    Date: {date}
    Time: {time}
    Sentiment: {sentiment}
    """

    TIME_REGEX = r'(\d\d:\d\d:\d\d)'
    DATE_REGEX = r'(\d\d-\d\d-\d\d\d\d)'

    @staticmethod
    def fromTweetFile(filename):
        with open(filename, 'r') as jsonIn:
            tweets = json.load(jsonIn)

        tweetObjs = []
        for tweet in tweets:
            tweetObjs.append(Tweet(tweet))
        return tweetObjs

    def __init__(self, src_dict):
        src_dict["sentiment"] = None
        self.date = self.parseDateFromCreatedAt(src_dict["created_at"])
        self.time = self.parseTimeFromCreatedAt(src_dict["created_at"])
        self.data = {}

        self.__dict__.update(src_dict)

    def __str__(self):
        return Tweet.TEMPLATE.format(source=self.source,
                                     text=self.full_text,
                                     retweet_count=self.retweet_count,
                                     favorite_count=self.favorite_count,
                                     created_at=self.created_at,
                                     date=self.date,
                                     time=self.time,
                                     sentiment=self.sentiment)

    def parseDateFromCreatedAt(self, created_at):
        date = re.search(Tweet.DATE_REGEX, created_at)
        return date.group(1)

    def parseTimeFromCreatedAt(self, created_at):
        time = re.search(Tweet.TIME_REGEX, created_at)
        return time.group(1)


def main():
    TWEET_FILE = './trump-tweets.json'
    tweets = Tweet.fromTweetFile(TWEET_FILE)

    for tweet in tweets[0:100]:
        print(str(tweet))

if __name__ == "__main__":
    main()

