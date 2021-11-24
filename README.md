# Sentiment-Analysis-Crypto
Here we test and develop sentiment analysis techniques for Twitter relating to various cryptocurrency projects and tokens.

## Objectives
1. Figure out how we can analyse the market sentiments of different protocols (create some sort of framework).
2. Find new, relevant metrics relating to sentiment analysis for crypto projects on Twitter and understand 
their relevance to other metrics like price and value of the token.


## TODO
1. Collect the required data (token data, twitter tweet data relating to the protocol)
2. Organize and clean up the data (tweet data for sentiment analysis as well as crypto price movement) into a singular database (SQL or postgres)
3. Find the right sentiment analysis model (NLP or otherwise) to analyse the tweet data
4. Record the sentiment (and experiment with other metrics as well!) of the tweets in the database
5. Perform regressions and time series analysis on the tweet sentiment in relation to price movements and other metrics to see if there are any correlations

## Some Ideas
If the metrics will be used in the production application in Econteric it might be a good idea to create a 
postgres database in the cloud where all these metrics and data can be stored. We can also have dockerized applications
in the cloud performing sentiment analysis and correlations on the updated data automatically. This will allow the data feed
to be updated easily and in real-time.

For now, since it is just research, we can just understand which metrics are important to look at to streamline that application development.
The most efficent and scaleable solution can be implemented much later after a lot of work.
