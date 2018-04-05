## DATA VISUALIZATION PROJECT
currently just campbell's proof of concept script

The tweets can be found in `trump-tweets.json.zip`. Please unzip before
continuing.

## Proof of concept
The proof of concepts are run through the `generic-proof.py` script which expects
`trump-tweets.json` to be in the same directory. If you look in the generic proof
file, you can alter it to run indico by swapping `doNLTK` with `doIndico`. By default,
the output of the proof of concept run is put into an `outfile.json` file.

Run `make` to setup the environment and source env/bin/activate to source the environment.

`python generic-proof.py` to generate the data.


Indico has many more methods for sentiment analysis than the NLTK Vader package.
If you look at how `doIndico` works, there is a strategy factory for getting the
sentiments. Replace `'sentiment_hq'` with the name of any other `indicoio` sentiment
method and the factory _should_ generate a strategy that pulls down and formats that type
of sentiment.
