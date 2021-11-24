from textblob import TextBlob
import tweepy
import sys
import os

T_API_KEY = os.environ.get("T_API_KEY")
T_API_SEC = os.environ.get("T_API_SEC")
BEARER = os.environ.get("BEARER")





def main():
    print("Hello World! \n")
    print("T_API_KEY = " + T_API_KEY)
    print("T_API_SEC = " + T_API_SEC)
    print("BEARER = " + BEARER)

if __name__ == "__main__":
    main()

