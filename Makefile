tweets:
	./scripts/download-tweets.sh

nltk:
	tweets
	./scripts/nltk-setup.sh

indico:
	tweets
	./scripts/indico-setup.sh

