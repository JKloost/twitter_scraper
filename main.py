import sys, re
import output_functionality as of
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got


#  gathers an amount of tweets (max_tweets) on the query
def gatherTweets(max_tweets, query):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setMaxTweets(max_tweets)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    
    return tweets


#  gathers the accident tweets, makes the outputfile
#  then filters the tweets and writes the tweets to the output file
def gatherAccidentTweets(max_tweets, query):
    tweets = gatherTweets(max_tweets, query)
    outputFile = of.readyOutputCsv()
    filtered_tweets = filter_unwanted_words(tweets)
    of.writeToOutput(filtered_tweets, outputFile)

   
#  goes through the output_got.csv file, searches the last 10 tweets for every user
#  then adds those tweets to the Tweets.txt file using writeToText()
def gatherLastTweets(amount):
    with open("output.csv", "r", encoding="utf-8") as myfile:
        number = 0
        for line in myfile:
            line = line.strip('\n').split(" :: ")
            if 'username'==line[0]:
                pass
            else:
                number+=1
                print('Now working on %s, tweet number %d' % (line[0], number))
                tweetCriteria = got.manager.TweetCriteria().setUsername(str(line[0])).setUntil(str(line[1][0:10])).setMaxTweets(amount)
                tweets = got.manager.TweetManager.getTweets(tweetCriteria)
                of.writeToText(tweets, line[0])
                

#filters certain words out of all the tweets we find   
def filter_unwanted_words(tweets):
    unwanted_words = {'not', '(NOT', '(Not', 'wasn’t', 'wasnt', "wasn't", '(not', 'none', 'neither', 'Not', 'Neither',
                      'NOT', "Wasn't", "Wasnt", ',not', '.not', 'Almost', 'almost', 'RT', '"RT', 'Baja', '#LegalTips',
                      "WASN'T", "WASNT", "NEITHER"}
    size = 0
    for t in tweets:
        text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', t.text, flags=re.MULTILINE)
        line = '\n%s :: %s :: "%s"' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), text)
        if set(line.split()).isdisjoint(unwanted_words):
            size += 1
            yield line
    print('From %d filtered %d out, and added to file \n' % (len(tweets), len(tweets)-size))
    


if __name__ == '__main__':
    #  Amount of tweets that are gather containing the query
    max_tweets = 20
    #  The query which will be searched
    query = 'I got car accident my fault'
    #  Amount of tweets gathered from people having mentioned a car accident
    previous_tweets_amount = 10
    #  Gathers max_tweets tweets of people having mentioned query
    gatherAccidentTweets(max_tweets, query)
    #  Gathers the previous previous_tweets_amount for people having mentioned query
    #  These tweets will (most likely) not contain the query
    gatherLastTweets(previous_tweets_amount)

