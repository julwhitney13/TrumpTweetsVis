import json
class Tweet():
    TEMPLATE = """
    Source: {source}
    Text: {text}
    Retweets: {retweet_count}
    Favorites: {favorite_count}
    Date: {date}
    """

    @staticmethod
    def fromTweetFile(filename):
        with open(filename, 'r') as jsonIn:
            tweets = json.load(jsonIn)

        tweetObjs = []
        for tweet in tweets:
            tweetObjs.append(Tweet(tweet))
        return tweetObjs

    def __init__(self, src_dict):
        for key in src_dict.keys():
            try:
                src_dict[key] = src_dict[key].encode('utf8')
            except AttributeError:
                continue
        self.__dict__.update(src_dict)

    def __str__(self):
        return Tweet.TEMPLATE.format(source=self.source,
                                     text=self.full_text,
                                     retweet_count=self.retweet_count,
                                     favorite_count=self.favorite_count,
                                     date=self.created_at)


def main():
    TWEET_FILE = './trump-tweets.json'
    tweets = Tweet.fromTweetFile(TWEET_FILE)

    for tweet in tweets[0:100]:
        print(str(tweet))

if __name__ == "__main__":
    main()

