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
