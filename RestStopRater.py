#Nick Biederman, Rob Boeckermann, Zack Sullivan, Pato the Guinea Pig
#Python Final Project:
#Rest Stop Rater

#sga8WQ;L5XXXccccccccccccccccccccccccccccccccccc"h"gGGG]H     <--- code from the guinea pig


import twitter
import datetime

now = datetime.datetime.now()  #This variable is used when building the tweet to send. The date is included to prevent duplicating tweets.

CONSUMER_KEY = 'kD1k9NfDeNsaIzXr0EIUldahk'          #API keys for Twitter account @RestStopRater
CONSUMER_SECRET = 'wSdRUZD9XEB5CxOEhciFK812QNQDonApxiM0z3sFTWXZbiGHkp'
ACCESS_TOKEN = '935197823255109634-5AXvEZLKBrBU2iIqF74JQKeqDcY4f5g'
ACCESS_TOKEN_SECRET = 'E6R8dHRAE5r4245LDAkpT894R8z0GluSucRFFyNs7CHVY'

api = twitter.Api(consumer_key=CONSUMER_KEY,        #Makes Api from keys
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)



######################################################################################################################################
###########################ADTs: 'Reviews' NODE, LINKED LIST##########################################################################
######################################################################################################################################
class Reviews:  #class to hold the ratings information for each rest stop location
    #"""
    #    >>> test = Reviews("RS1")
    #    >>> test.add(5,5,5,5)
    #    >>> test.add(3,3,3,3)
    #    >>> test.getBathroomRating()
    #    4.0
    #    >>> test.add(5,5,5,5)
    #    >>> test.getAverageRating()
    #    4.33
    #    """
    name = ""
    bathroomRating = 0 #rating variables will hold the summation of all ratings given for a rest stop
    foodRating = 0
    sceneryRating = 0
    informationRating = 0
    numberOfReviews = 0 #rating summations will be divided by this variable to determine the average rating for that catagory
    nextPointer = None #variables that hold the "Reviews" class for the next and previous location in the list
    previousPointer = None 
    def __init__(self, nameIn, b=0, f=0, s=0, i=0, r=0):  #new locations have ratings set to 0 by default unless the values are passed in
        self.name = nameIn
        self.bathroomRating = int(b)
        self.foodRating = int(f)
        self.sceneryRating = int(s)
        self.informationRating = int(i)
        self.numberOfReviews = int(r)
        self.nextPointer = None
        self.previousPointer = None
    def add(self, b, f, s, i):  #new ratings for a location are added to the summation of all ratings so far for that location
        self.bathroomRating = self.bathroomRating + int(b)
        self.foodRating = self.foodRating + int(f)
        self.sceneryRating = self.sceneryRating + int(s)
        self.informationRating = self.informationRating + int(i)
        self.numberOfReviews = self.numberOfReviews + 1 #number of reviews +1
    def getBathroomRating(self):
        return round(self.bathroomRating / self.numberOfReviews, 2)  #ratings are rounded to two decimal places
    def getFoodRating(self):
        return round(self.foodRating / self.numberOfReviews, 2)
    def getSceneryRating(self):
        return round(self.sceneryRating / self.numberOfReviews, 2)
    def getInformationRating(self):
        return round(self.informationRating / self.numberOfReviews, 2)
    def getAverageRating(self):
        return round((self.getBathroomRating() + self.getFoodRating() + self.getSceneryRating() + self.getInformationRating()) / 4, 2)

class reviewsList:                    #Creates a doubly linked list with node type Reviews
    def __init__ (self, head = None): #Initializes the list with head = None
        self.head = head
    
    def insert(self, nameIn, b = 0, f = 0, s = 0, i = 0, r = 0):  #Adds a new node with a name and defaults of 0 for every rating
        newNode = Reviews(nameIn, b, f, s, i, r)                  #Creates an instance of Reviews
        newNode.nextPointer = self.head                           #Points the new node to head
        self.head = newNode                                       #Makes the new node head
        if self.head.nextPointer is not None:                     #If there is a next node, the next node's previous pointer is pointed to the new node
            self.head.nextPointer.previousPointer = self.head

    def display(self):              #Simple display function
        currentNode = self.head     #Start at head
        while(currentNode):         #Loop ends when final node is reached
            print(currentNode.name) #Prints the name of each node
            currentNode = currentNode.nextPointer
                
    def findHighest(self):          #Finds the highest node, removes it from the list, and returns it
        currentNode = self.head
        previousNode = None
        topVal = 0                  #Variable used for checking for the highest average
        topNode = currentNode
        while (currentNode):        #Loops to end of list
            if (currentNode.getAverageRating() > topVal):   #True if rating of the current node is higher than any previous node
                topVal = currentNode.getAverageRating()     #New top rating
                topNode = currentNode                       #New top node to remove and return
            currentNode = currentNode.nextPointer
        if topNode.previousPointer is None:                 #Removes top node from list. This case is for a top node at the begining of the list
            topNode.nextPointer.previousPointer = None
            self.head = topNode.nextPointer
        elif topNode.nextPointer is None:                   #This case is for a top node at the end of the list
            topNode.previousPointer.nextPointer = None
        else:                                               #This is for a top node anywhere else in the list
            topNode.previousPointer.nextPointer = topNode.nextPointer
            topNode.nextPointer.previousPointer = topNode.previousPointer
        return topNode              #Returns the top node

#########################################################################################################################################
##########################DATA PARSING- READS AND WRITES .txt, CALCULATES BEST REST STOP#################################################
#########################################################################################################################################
def readFile(_reviewsList):                      #Opens a text file, reads each line, puts any ints in a list and saves a string
                                     #This layout relies heavily on properly sanatizing inputs before writing to the .txt
    #"""
    #>>> test = readFile()
    #>>> test.head.getBathroomRating()
    #5.0
    #>>> test.head.getAverageRating()
    #4.25
    #>>> test.head.nextPointer.getBathroomRating()
    #4.0
    #>>> test.head.nextPointer.name
    #I-75 MM 27 [NB]\n
    #"""
    #_reviewsList = reviewsList()
    inFile = open("ratings.txt", 'r')
    ratings = []
    name = "" 
    for line in inFile:
        if (isInt(line)): #add rating to array
            if (int(line) > 1000000000000000):
                _reviewsList.insert(name, ratings[0], ratings[1], ratings[2], ratings[3], ratings[4])
                name = line.strip("\n")
            else:
                x = int(line)
                ratings.append(x)
        else: #If there are no ratings in the array, record the name of the location. Else add the previous location and ratings to the list and record the name of the new node. Clear array.
            if(ratings != []):
                _reviewsList.insert(name, ratings[0], ratings[1], ratings[2], ratings[3], ratings[4])
            name = line.strip("\n")
            ratings = []
    return _reviewsList, name

def isInt(x):       #file.read() returns a string. This checks to see if a string from the file represents an int
    try:
        int(x)
        return True
    except ValueError:
        return False

def writeFile(llist, ID):
    #"""
    #>>> test = readFile()
    #>>> test.insert("I-75 MM 95 [NB]", 0, 0, 0, 0, 1)
    #>>> test.insert("hi nicky", 1, 2, 3, 4, 1)
    #>>> writeFile(test)
    #"""
    #open ("ratings.txt", 'w').close()  #Clears all information in text file
    outFile = open ("ratings.txt", 'w')#Opens .txt for writing
    outFile.close()
    outFile = open ("ratings.txt", 'w')
    temp = llist.head
    while (temp != None):
        outFile.write(str(temp.name) + "\r\n")
        outFile.write(str(temp.bathroomRating) + "\r\n")
        outFile.write(str(temp.foodRating) + "\r\n")
        outFile.write(str(temp.sceneryRating) + "\r\n")
        outFile.write(str(temp.informationRating) + "\r\n")
        outFile.write(str(temp.numberOfReviews) + "\r\n")
        temp = temp.nextPointer
    outFile.write(ID)

#############################################################################################################################################
#############################GET TWEETS: READS FROM TWITTER, WRITES TO ADT###################################################################
#############################################################################################################################################

def getTweets(lastID):
    tlist = api.GetMentions(200, lastID, None, False, False, True) #deleted last parameter: False
    revList = [i.text for i in tlist]
    ids = [j.id_str for j in tlist]
    return revList, ids[len(ids) - 1]


def parseTweet(twt):
    tempstr = ""
    #twt = str(twt)
    check = 1
    for i in range(0,len(twt)-2):
        if twt[i] == '\n' and check == 1:
            check = 0
        elif not(twt[i] == '\n') and check == 0:
            tempstr = tempstr + twt[i]
        elif twt[i] == '\n' and check == 0:
            return tempstr,twt[i+1],twt[i+3],twt[i+5],twt[i+7]

#def searchList(aTweet,linList):
#    #search linked list linlist for tweet
#    i = linList.head
#    while i != None:
#        if aTweet == i.name:
#            return i
#        i = i.nextPointer
#    return None

def updateReviews(revList, linList):
    for i in range(0,len(revList)-1):
        a,b,c,d,e = parseTweet(revList[i])
        #temp = searchList(a,linList)

        j = linList.head
        check = 1
        while j != None:
            if a == j.name:
                j.add(b,c,d,e)
                check = 0
            j = j.nextPointer
        if check == 1:
            linList.insert(a,b,c,d,e,1)#create new node
    return linList

#############################################################################################################################################
#############################SEND TWEET: TWEETS TOP RATED REST STOPS#########################################################################
#############################################################################################################################################

def sendTweet(_reviewsList):  #This function calls the other functions needed to post the tweets. Due to some modifications made to the operation of our code,
    makeStatus(_reviewsList)  #This function could be removed and makeStatus(_reviewsList) could be called directly from main. However, we wanted to alter our code
                              #as little as possible once we reached the final troubleshooting stage

def getHighest(_reviewsList): #This helper function returns the node with the highest average rating.
    return _reviewsList.findHighest()

def makeStatus(_reviewsList): #This funtion generates and posts the three tweets that are sent any time the script is run
    status = getDate()        #First a string is created and initialized with the current date
    status += "1: "           #A rating number is then added
    top = getHighest(_reviewsList) #The node for the highest rated stop is found and removed from the list
    status += makeLine(top)   #This node is then passed to makeLine() to generate the remainder of the status
    api.PostUpdate(status)    #The status is then posted to twitter
    status = getDate()        #This process is repeated 2 more times.
    status += "2: "
    top = getHighest(_reviewsList)
    status += makeLine(top)
    api.PostUpdate(status)
    status = getDate()
    status += "3: "
    top = getHighest(_reviewsList)
    status += makeLine(top)
    api.PostUpdate(status)
    print(status)
    return str(status)

def makeLine(top):          #The node of the top rated stop is passed in
    line = ""               #An empty string is created
    line += top.name        #The name is taken from the passed in node
    line += ": B:"          #Constant identifiers for the rating type are added to the string
    line += str(top.getBathroomRating()) #The rating is taken from the passed in node. Since these are stored as an int, str(rating) is used to convert it to a string
    line += ", F:"          #This process is repeated until all 4 rating are added to the string.
    line += str(top.getFoodRating())
    line += ", S:"
    line += str(top.getSceneryRating())
    line += ", I:"
    line += str(top.getInformationRating())
    line += "   "
    return str(line)        #The final string is returned to the calling function

def getDate():              #Returns the current date as a string
    date = ""               #Creates an empty string
    date += str(now.day)    #Adds the current day. now is a constant generated at the beginning of the code.
    date += "/"             #a / is added to seperate day from month
    date += str(now.month)  #This is repeated for month and year
    date += "/"
    date += str(now.year)
    date += "   "
    return date             #The date is returned as a string.


#############################################################################################################################################
#####################################PATO'S CODE#############################################################################################
#############################################################################################################################################
#---j99999999999999o-o[ooooooooooooooooooooooooooooooooooooooooooooooooo[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[9[9999999999999999999999999999999999
#555555555555555/*3
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#/+33333333333333333333333333333333333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777'bttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt79
#,\\\\\\\\\\8888888888888883+.1222222222222211111111111111111111111111111111111111-+++++
#klp


def main():
    llist = reviewsList()
    tweetID = ""
    llist, tweetID = readFile(llist)
    newTweets = []
    newTweets, tweetID = getTweets(tweetID)
    llist = updateReviews(newTweets, llist)
    writeFile(llist, tweetID)
    sendTweet(llist)

if __name__ == '__main__':
    main()
