import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def readTwitter(tweet_file):
    result = ""
    for line in tweet_file:
	response = json.loads(line)
	if(response.has_key("created_at")):
		result += response["text"] + "\n\n"
    return result

def printSentimentOfEach(scores,twitter_text):
    sentiment = ""
    totalScore = 0
    for word in twitter_text.split(" "):
	if(scores.has_key(word)):
	     sentiment += word + ':' +str(scores.get(word)) + "\n"
	     totalScore = totalScore + scores.get(word)
    #sentiment + "The tweet total sentiment is: " + 
    return totalScore

def getSentiment(scores,twitter_string):
    for text in twitter_string.split("\n\n"):
        if(text != ""):
	   sentiment = printSentimentOfEach(scores, text)
           print sentiment

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
    	term, score = line.split("\t")
    	scores[term] =int(score)
    #print scores.items()

    tweet_file = open(sys.argv[2])
    twitter_text = ""
    twitter_text = readTwitter(tweet_file)
    #print twitter_text

    getSentiment(scores, twitter_text)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
