#Nick Biederman, Rob Boeckermann, Zack Sullivan
#Python Final Project:
#Rest Stop Rater


import twitter

api = twitter.Api(consumer_key=['kD1k9NfDeNsaIzXr0EIUldahk'],
                  consumer_secret=['wSdRUZD9XEB5CxOEhciFK812QNQDonApxiM0z3sFTWXZbiGHkp'],
                  access_token_key=['35197823255109634-5AXvEZLKBrBU2iIqF74JQKeqDcY4f5g'],
                  access_token_secret=['E6R8dHRAE5r4245LDAkpT894R8z0GluSucRFFyNs7CHVY'])

######################################################################################################################################
###########################ADTs: 'Reviews' NODE, LINKED LIST##########################################################################
######################################################################################################################################
class Reviews:
    """
    >>> test = Reviews("RS1")
    >>> test.add(5,5,5,5)
    >>> test.add(3,3,3,3)
    >>> test.getBathroomRating()
    4.0
    >>> test.add(5,5,5,5)
    >>> test.getAverageRating()
    4.33
    """
    name = ""
    bathroomRating = 0
    foodRating = 0
    sceneryRating = 0
    informationRating = 0
    numberOfReviews = 0
    nextPointer = None
    def __init__(self, nameIn, b=0, f=0, s=0, i=0, r=0):
        self.name = nameIn
        self.bathroomRating = b
        self.foodRating = f
        self.sceneryRating = s
        self.informationRating = i
        self.numberOfReviews = r
        self.nextPointer = None
    def add(self, b, f, s, i):
        self.bathroomRating += b
        self.foodRating += f
        self.sceneryRating += s
        self.informationRating += i
        self.numberOfReviews += 1
    def getBathroomRating(self):
        return round(self.bathroomRating / self.numberOfReviews, 2)
    def getFoodRating(self):
        return round(self.foodRating / self.numberOfReviews, 2)
    def getSceneryRating(self):
        return round(self.sceneryRating / self.numberOfReviews, 2)
    def getInformationRating(self):
        return round(self.informationRating / self.numberOfReviews, 2)
    def getAverageRating(self):
        return round((self.getBathroomRating() + self.getFoodRating() + self.getSceneryRating() + self.getInformationRating()) / 4, 2)
    def setNext(self, newNext):
        self.nextPointer = newNext
        
class reviewsList:
    def __init__ (self, head = None):
        self.head = head

    def insert(self, nameIn, b = 0, f = 0, s = 0, i = 0, r = 0):
        newNode = Reviews(nameIn, b, f, s, i, r)
        newNode.setNext(self.head)
        self.head = newNode

    def display(self):
        currentNode = self.head
        while(currentNode):
            print(currentNode.name)
            currentNode = currentNode.nextPointer
            
    def findHighest(self):
        currentNode = self.head
        previousNode = None
        topVal = 0
        topNode = currentNode
        while (currentNode):
            if (currentNode.getAverageRating() > topVal):
                print(currentNode.getAverageRating())
                topVal = currentNode.getAverageRating()
                topNode = currentNode
        return topNode
    
#########################################################################################################################################
##########################DATA PARSING- READS AND WRITES .txt, CALCULATES BEST REST STOP#################################################
#########################################################################################################################################
def readFile():                      #Opens a text file, reads each line, puts any ints in a list and saves a string
                                     #This layout relies heavily on properly sanatizing inputs before writing to the .txt
    """
    >>> test = readFile()
    >>> test.head.getBathroomRating()
    5
    >>> test.head.getAverageRating()
    4.25
    >>> test.head.nextPointer.getBathroomRating()
    4
    >>> 
    """
    _reviewsList = reviewsList()
    inFile = open("ratings.txt", 'r')
    ratings = []
    for line in inFile:
        if (isInt(line)): #rating
            x = int(line)
            ratings.append(x)
        elif (line == "_"): #end of current location rating
            _reviewsList.insert(name, ratings[0], ratings[1], ratings[2], ratings[3], ratings[4])
            ratings = []
        else: #location name
            name = line
    return _reviewsList

def isInt(x):       #file.read() returns a string. This checks to see if a string from the file represents an int
    try: 
        int(x)
        return True
    except ValueError:
        return False

def writeFile(name, ratings):
    open ("ratings.txt", 'w').close()  #Clears all information in text file
    outFile = open ("ratings.txt", 'w') #Opens .txt for writing
    outFile.write("This file has been overwritten \r\n")
    print (name)
    outFile.write(name + "\n\r")
    for i in ratings:
        outFile.write(str(ratings[i-1]) + "\r\n")


#############################################################################################################################################
#############################GET TWEETS: READS FROM TWITTER, WRITES TO ADT###################################################################
#############################################################################################################################################
LID = 0 #import last id

def getTweets():
    twitter.GetMentions(count=200, since_id=LID, max_id=None, trim_user=True, contributor_details=False, include_entities=False, return_json=False)
    print (twitter.Status)
    LID = id;
#export LID

#############################################################################################################################################
#############################SEND TWEET: TWEETS TOP RATED REST STOPS#########################################################################
#############################################################################################################################################

def sendTweet():
    postUpdates(makeStatus())

def getHighest():
    return _reviewsList.findHighest()
def makeStatus():
    status = "#1: "
    top = getHighest()
    status += makeLine(top)
    status += "#2: "
    status += makeLine(top)
    status += "#3: "
    status += makeLine(top)
    print(status)
def makeLine(top):
    line = ""
    line += top.name
    line += ": B:"
    line += str(top.bathroomRating)
    line += ", F:"
    line += str(top.foodRating)
    line += ", S:"
    line += str(top.sceneryRating)
    line += ", I:"
    line += str(top.informationRating)
    line += "\r\n"
    return line
