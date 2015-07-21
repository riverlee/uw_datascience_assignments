#!/usr/bin/python
from __future__ import  division
import sys
import json
import re
from collections import Counter
from pprint import pprint

def main():
    terms=[]
    exp = re.compile('^\w+$')
    with open (sys.argv[1]) as f:
        for line in f:
           tweet = json.loads(line,"utf-8")
           if "text" in tweet.keys():
               words = tweet['text'].split()
               for w in words:
                   w = unicode(w.lower()).encode("utf-8")
                   if not re.search(exp,w):
                       continue
                   terms.append(w)

    ## End fill terms
    #pprint(terms)
    n = len(terms)
    #print(n)
    terms_count = Counter(terms)
    for term,count in terms_count.most_common():
        f = count/n
        print(term+" " +str(f))






if __name__ =="__main__":
    main()


