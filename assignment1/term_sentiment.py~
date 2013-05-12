import sys
import json

nonSentiment = {}
count = {}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def readTwitter(tweet_file):
    result = ""
    for line in tweet_file:
	response = json.loads(line)
	if(response.has_key("created_at")):
		result += response["text"] + "\n"
    return result

def getNonSentiment(scores,twitter_string):
    nonSentiment = {}
    for text in twitter_string.split("\n"):
	nonSentiment = assignNonSentiment(scores, text)
	if(nonSentiment.keys() != None):
	   getNoneSentimentValue(nonSentiment)

def assignNonSentiment(scores,twitter_text):
    sentiment = ""
    totalScore = 0
    result = {}
    for word in twitter_text.split(" "):
	if(scores.has_key(word)):
 	     totalScore = totalScore + scores[word]
    for word in twitter_text.split(" "):
	if(scores.has_key(word)):
	     continue
	else:
	     result[word.replace(',','').replace('.','').replace('\'','')] = totalScore
    return result

def getNoneSentimentValue(nonS_dict):
    global nonSentiment, count
    for word in nonS_dict.iterkeys():
    	if(nonSentiment.has_key(word)):
		nonSentiment[word] = nonSentiment[word] + nonS_dict[word]
		count[word] = count[word] + 1.0
	else:
		nonSentiment[word] = nonS_dict[word]
		count[word] = 1.0
    for word in nonSentiment.keys():
	if (count.has_key(word)):
		nonSentiment[word] = nonSentiment[word]/count[word]
		
    

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
    	term, score = line.split("\t")
    	scores[term] =int(score)


    tweet_file = open(sys.argv[2])
    twitter_text = ""
    twitter_text = readTwitter(tweet_file)

    getNonSentiment(scores, twitter_text)
    
    for i in nonSentiment.keys():
	if(i != ""):
           unicode_string = i + " " + str(nonSentiment[i])
	   enicode_string = unicode_string.encode("utf-8")
	   print enicode_string

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
