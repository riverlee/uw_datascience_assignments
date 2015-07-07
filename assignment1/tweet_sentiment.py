import sys
import json
from pprint import pprint

"""
For this part, you will compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.
"""

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def sentiment_tweet(score,tweet):
    ## Only check the text in a tweet
    if "text" in tweet.keys():
        #print(tweet['text'])    
        words = tweet['text'].split()
        s = 0
        for w in words:
            w = unicode(w.lower()).encode("utf-8")
            #print(w)
            if w in score.keys():
                s=s+score[w]
        return s
    else:
        return 0
    

def main():
    ### build a dictionary to store the term score
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

#   print scores.items()
    
##  Load the tweet json data
    tweet_file = open(sys.argv[2])
    i = 1
    with open(sys.argv[2]) as f:
        for line in f:
            tweet = json.loads(line,"utf-8");
            #pprint(tweet)
            print(sentiment_tweet(scores,tweet))
            
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
