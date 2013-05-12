# Which state is the happiest

import sys
import json

states = {}

def setState():
	states['AL'] = 0
	states['AK'] = 0
	states['AZ'] = 0
	states['CA'] = 0
	states['CO'] = 0
	states['CT'] = 0
	states['DE'] = 0
	states['FL'] = 0
	states['GA'] = 0
	states['HI'] = 0
	states['ID'] = 0
	states['IL'] = 0
	states['IN'] = 0
	states['IA'] = 0
	states['KS'] = 0
	states['KY'] = 0
	states['LA'] = 0
	states['ME'] = 0
	states['MD'] = 0
	states['MA'] = 0
	states['MI'] = 0
	states['MN'] = 0
	states['MS'] = 0
	states['MO'] = 0
	states['MT'] = 0
	states['NE'] = 0
	states['NV'] = 0
	states['NH'] = 0
	states['NJ'] = 0
	states['NM'] = 0
	states['NY'] = 0
	states['NC'] = 0
	states['ND'] = 0
	states['OH'] = 0
	states['OK'] = 0
	states['OR'] = 0
	states['PA'] = 0
	states['RI'] = 0
	states['SC'] = 0
	states['SD'] = 0
	states['TN'] = 0
	states['TX'] = 0
	states['UY'] = 0
	states['VT'] = 0
	states['VA'] = 0
	states['WA'] = 0
	states['WV'] = 0
	states['WI'] = 0
	states['WY'] = 0



def getSentimentOfEach(scores,twitter_text):
    sentiment = ""
    totalScore = 0
    for word in twitter_text.split(" "):
	if(scores.has_key(word)):
	     totalScore = totalScore + scores.get(word)
    return totalScore

def getTheHappiest():
    global states
    happiestState = "AL"
    for state in states.iterkeys():
	if(states[state]>states[happiestState]):
		happiestState = state
    print happiestState

def readTwitter(scores,tweet_file):
    global states
    result = ""
    for line in tweet_file:
      response = json.loads(line)
      if(response.has_key("created_at")):
	if(response["user"]["location"]!=""):
	   for state in states.iterkeys():
		if(state in response["user"]["location"]):
			score = getSentimentOfEach(scores,line)
			states[state] += score

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
    	term, score = line.split("\t")
    	scores[term] =int(score)

    setState()
    tweet_file = open(sys.argv[2])
    twitter_text = ""
    twitter_text = readTwitter(scores,tweet_file)
    getTheHappiest()
    

if __name__ == '__main__':
    main()

