import sys
import json
from pprint import pprint
from collections import  defaultdict

from states import states

"""
For this part, you will compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.
"""
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
    stateScore = defaultdict(list)

    with open(sys.argv[2]) as f:
        for line in f:
            tweet = json.loads(line,"utf-8");
            #pprint(tweet)
            #print(sentiment_tweet(scores,tweet))
            s = sentiment_tweet(scores,tweet)
            if "place" in tweet.keys():
                if not tweet['place'] is None:
                    if tweet['place']['country_code'] == "US":
                        fullname = tweet['place']['full_name']
                        city,state = fullname.split(",")
                        #state=str(state)
                        state = state.strip()
                        if not state in states.keys():
                            continue
                        if state in stateScore.keys():
                            stateScore[state]=[s]
                        else:
                            stateScore[state].append(s)
    ## output
    for st,lst in stateScore.items():
        t=0
        for v in lst:
            t=t+v
        avgs=t/len(lst)

        print(st+" "+str(avgs))



if __name__ == '__main__':
    main()
