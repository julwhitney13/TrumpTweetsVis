import indicoio

def configure():
    with open('./indico-key.txt') as keyFile:
        indicoio.config.api_key = keyFile.read().strip()

def main():
    configure()
    # single example
    print(indicoio.sentiment_hq("I love writing code!"))
    print(indicoio.political("I have a constitutional right to own land!"))


if __name__ == "__main__":
    main()
