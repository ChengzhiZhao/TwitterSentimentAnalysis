import sys
import json
import operator

hashtags = {}
top_ten = {}


def readTwitter(tweet_file):
    result = ""
    global hashtags
    for line in tweet_file:
	response = json.loads(line)
	if(response.has_key("created_at")):
	    if(response["entities"]["hashtags"]!=""):
		for hashtag in response["entities"]["hashtags"]:
		    tag = hashtag["text"]
		    if(hashtags.has_key(tag)):
                         hashtags[tag] += 1.0
		    else:
			 hashtags[tag] = 1.0

def sortTopTen():
    global hashtags, top_ten
    keyContainer = []
    temp = ""
    i = 0
    sorted_X = sorted(hashtags.iteritems(), key = operator.itemgetter(1))
    sorted_X.reverse()
    for i in range(len(sorted_X)):
	if(i<10):
		unicode_string = str(sorted_X[i][0]) + " " + str(sorted_X[i][1])
		enicode_string = unicode_string.encode("utf-8")
		print enicode_string
        	i += 1
        else:
	        break


def main():
    tweet_file = open(sys.argv[1])
    twitter_text = ""
    readTwitter(tweet_file)
    sortTopTen()

    #for tag in hashtags.iterkeys():
	#print tag + ": " + str(hashtags[tag])

if __name__ == '__main__':
    main()
