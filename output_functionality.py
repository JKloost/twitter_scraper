#  This contains all code on writing to a file and printing on console:
import codecs, re

#  simple print function, used for checking
#  prints username, retrweets, and the tweet text
def printTweet(t):
    print("Username: %s" % t.username)
    print("Retweets: %d" % t.retweets)
    print("Text: %s \n" % t.text)


#  makes the output csv clean and in correct format
def readyOutputCsv():
    outputFileName = "output.csv"
    outputFile = codecs.open(outputFileName, "w+", "utf-8")
    outputFile.write('username :: date :: text')
    
    return outputFile


#  writes the gathered tweets to the output file
def writeToOutput(lines, outputFile):
    outputFile.writelines((line for line in lines))
    outputFile.flush()
    
    
#  writes the last n tweets of a person to the Tweets.txt file
def writeToText(tweets, username):
    with open("Tweets.txt", "a", encoding="utf-8") as myfile:
        myfile.write(username + '\n')
        for t in tweets:
            if t.username=='username':
                pass
            else:
                text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', t.text, flags=re.MULTILINE)
                myfile.write(text + '\n')
        myfile.write('\n')