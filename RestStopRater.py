#Nick Biederman, Rob Boeckermann, Zack Sullivan
#Python Final Project:
#Rest Stop Rater

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
    def __init__(self, nameIn):
        self.name = nameIn
        self.bathroomRating = 0
        self.foodRating = 0
        self.sceneryRating = 0
        self.informationRating = 0
        self.numberOfReviews = 0
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

    def insert(self, nameIn):
        newNode = Reviews(nameIn)
        newNode.setNext(self.head)
        self.head = newNode

    def display(self):
        head = self.head
        while(head):
            print(head.name)
    
#########################################################################################################################################
##########################DATA PARSING- READS AND WRITES .txt, CALCULATES BEST REST STOP#################################################
#########################################################################################################################################
def readFile():                      #Opens a text file, reads each line, puts any ints in a list and saves a string
                                     #This layout relies heavily on properly sanatizing inputs before writing to the .txt
    inFile = open("ratings.txt", 'r')
    ratings = []
    for line in inFile:
        if (isInt(line)):
            x = int(line)
            ratings.append(x)
        elif len(line) == 0:
            print(line)
            name = line
    print(name)
    for i in ratings:
        print(ratings[i - 1])
        
   # writeFile(name, ratings)

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
    return Reviews("I-75 MM 27 [NB]")
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
    
