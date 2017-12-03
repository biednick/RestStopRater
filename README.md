# Reststop Rater

Using a simple Python script, this twitter bot reads ratings from the Twitter page @RestStopRater and sends a tweet of the three highest rated rest stops.

This project was done by Nick Biederman, Rob Boekermann, Pato the Guinea Pig, and Zack Sullivan for CS2021 at the University of Cincinnati. 


## Required Packages

This script uses the python twitter package. Install using `$ pip3 install python-twitter` for Python 3. 

## Known Issues

### Input Sanitation

Currently inputs from Twitter are not sanitized. If a user sends a tweet to @RestStopRater that does not follow the listed format perfectly, the script will fail to properly parse the tweet.

### Minumum number of ratings

Due to the method used to find the three highest rated there must be at least 4 ratings before the script is run the first time. These ratings can be seeded to the Twitter page or into ratings.txt. The ratings.txt file located in this repo contains an adequate number of ratings to run the script.

### Missing API

Since this code is shared publically the API information for @RestStopRater has been removed. Prior to using this script, the API must be populated with keys in this format:

`CONSUMER_KEY = '<KEY>'`

`CONSUMER_SECRET = '<KEY SECRET>'`

`ACCESS_TOKEN = '<TOKEN>'`

`ACCESS_TOKEN_SECRET = '<TOKEN SECRET>'`

This populated code block should then replace `####PASTE API HERE####` on line 13.

## Running the script

Using terminal on Mac or Linux or Bash on Ubuntu on Windows CD into the location you have saved the repo. Run the script using `python3 RestStopRater.py`. This script was written and tested in Python 3.6.2 and has not been tested on any other version.

## Tweet format

The format of the tweet is extremely important. Any variation from this format will cause the script to work improperly.

@RestStopRater

I-xxx MM yy [zB]

a

b

c

d

Note there is only one newline between lines, one space for each whitespace, and no spaces at the end of each line.

The second line, I-xxx MM yy [zB], represents the name of the rest stop. Names in the appropriate format can be found by using [this app](https://play.google.com/store/apps/details?id=com.insofttech.reststops&hl=en) for Android or a similar rest stop finding app for iOS. 

a,b,c, and d represent ratings on a scale of 1-5 for bathrooms, food, scenery, and information respectively.