import sys
import json
from pprint import pprint
import re

"""
In this part you will be creating a script that computes the sentiment for the terms that do not appear in the file AFINN-111.txt.
"""

globdict = {}

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
 
def sentiment_term(score,tweet):
    ## Only check the text in a tweet
    if "text" in tweet.keys():
        s = sentiment_tweet(score,tweet)
        words = tweet['text'].split()
        for w in words:
            w = unicode(w.lower()).encode("utf-8")
            #print(w)
            if w not in score.keys():
                ## A filter on w (word)
                exp = re.compile('^\w+$')
                if not re.search(exp,w):
                    continue
                if w in globdict.keys():
                    globdict[w].append(s)
                else:
                    globdict[w]=[]
                    globdict[w].append(s)
def average(item):
    s=0
    for i in item:
        s=s+int(i)
    return s/len(item)

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
            sentiment_term(scores,tweet)
    #        break
            #pprint(globdict)
     
    ## print term score
    for key, item in globdict.items():
        print(str(key)+" "+str(average(item)))


    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
