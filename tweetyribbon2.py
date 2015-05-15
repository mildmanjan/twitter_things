#######################################################################################
# simpleTweet_01_python.py
# visit my instructables for more information
# http://www.instructables.com/member/pdxnat/
# SPEN CODE MADE FROM tweepy_hello.py AUGUST 2014
print 'running... simpleTweet_01_python'

# import libraries
import twitter
import serial
import time

# connect to arduino via serial port **CHECK HERE**
arduino = serial.Serial('/dev/tty.usbmodem471fp', 9600, timeout=1)

# establish OAuth id with twitter
# this is the oauth for machine_o_grace
#api = twitter.Api(consumer_key='x',
#                  consumer_secret='x',
#                   access_token_key='xxx-xxx',
#                  access_token_secret='xx')


# listen to arduino
def listenToArduino():
    msg=arduino.readline()
    if msg > '':
        print 'arduino msg: '+msg.strip()
        compareMsg(msg.strip())

# avoid duplicate posts
def compareMsg(newMsg):
    # compare the first word from new and old
    status = api.GetUserTimeline('tweetyribbon')
    prevMsg = [s.text for s in status]
    pM = ""+prevMsg[0]+""
    pM = pM.split()
    nM = newMsg.split()
    print "prevMsg: "+pM[0]
    print "newMsg: "+nM[0]
    if pM[0] != nM[0]:
        print "positive feedback"
        postMsg(newMsg)

# post new message to twitter
def postMsg(newMsg):
    localtime = time.asctime(time.localtime(time.time()))
    tweet = api.PostUpdate(newMsg+", "+localtime)
    print "tweeted: "+tweet.text

while 1:
    listenToArduino()

#######################################################################################
