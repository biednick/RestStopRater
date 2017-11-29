#Nick Biederman, Rob Boeckermann, Zack Sullivan
#Python FInal Project:
#Rest Stop Rater

#Ratings ADT
class Reviews:
    bathroom_rating = 0
    food_rating = 0
    scenery_rating = 0
    information_rating = 0
    number_of_reviews = 0
    def __init__(self):
        self.bathroom_rating = 0
        self.food_rating = 0
        self.scenery_rating = 0
        self.information_rating = 0
        self.number_of_reviews = 0
    def add(self, b, f, s, i):
        self.bathroom_rating += b
        self.food_rating += f
        self.scenery_rating += s
        self.information_rating += i
        self.number_of_reviews += 1
    def getAverageRating(self):
        return ((bathroom_rating / number_of_reviews) + (food_rating / number_of_reviews) + (scenery_rating / number_of_reviews) + (information_rating / number_of_reviews)) / 4

def readFile():                      #Opens a text file, reads each line, puts any ints in a list and saves a string
                                     #This layout relies heavily on properly sanatizing inputs before writing to the .txt
    inFile = open("ratings.txt", 'r')
    ratings = []
    for line in inFile:
        if (isInt(line)):
            x = int(line)
            ratings.append(x)
        elif len(line) != 0
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
    
