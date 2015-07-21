import sys
import json
from pprint import pprint
from collections import Counter
"""
For this part, you will compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.
"""

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tags=[]
    with open(sys.argv[1]) as f:
        for line in f:
            tweet = json.loads(line,"utf-8");
            if "entities" in tweet.keys():
                if 'hashtags' in tweet["entities"].keys():
                    for tmpdict in  tweet['entities']['hashtags']:
                        if "text" in tmpdict.keys():
                            tags.append(tmpdict['text'])
            
    ## end reading
    tagcounter = Counter(tags)
    for tag,count in tagcounter.most_common(10):
        print(tag+" "+str(count))

if __name__ == '__main__':
    main()
