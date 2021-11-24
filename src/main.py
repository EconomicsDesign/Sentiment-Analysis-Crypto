from textblob import TextBlob
import tweepy
import sys
import os

# Get API keys from env variables
consumer_key = os.environ.get("T_API_KEY")
consumer_secret = os.environ.get("T_API_SEC")

# Authenticate with API keys
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Function which collects tweets and writes them to tweets.txt
def collect_tweets(search_term, tweet_amount):
    polarity = 0
    tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(tweet_amount)
    tweets_file = open("tweets.txt", "a")
    for tweet in tweets:
        final_text = tweet.text.replace('RT', '')
        if final_text.startswith(' @'):
            position = final_text.index(':')
            final_text = final_text[position+2:]
            tweets_file.write(final_text)
            tweets_file.write("\n")
        if final_text.startswith('@'):
            position = final_text.index(' ')
            final_text = final_text[position+2:]
            tweets_file.write(final_text)
            tweets_file.write("\n")
        analysis = TextBlob(final_text)
        polarity += analysis.polarity
    tweets_file.close
    print(polarity)

def main():
    search_term = "Audius"
    tweet_amount = 30
    collect_tweets(search_term, tweet_amount)



if __name__ == "__main__":
    main()

