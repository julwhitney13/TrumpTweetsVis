import indicoio

def configure():
    with open('./indico-key.txt') as keyFile:
        indicoio.config.api_key = keyFile.read().strip()

def get_examples(filename):
    with open(filename) as inputText:
        return inputText.readlines()


def main():
    configure()
    examples = filter(lambda sen: sen != '', get_examples('input.txt'))
    # single examples
    sentiments = indicoio.sentiment_hq(examples)
    poli = indicoio.political(examples)
    for i in range(len(examples)):
        print('============')
        print('{}\n\n{}\n\n{}\n'.format(examples[i], sentiments[i], poli[i]))
        print('============')

if __name__ == "__main__":
    main()
