# Imports libraries used in the code.
import time
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Introduction to the program, tells user the purpose of the code and how to use it
print('''Hello, this program will calculate the most used word in a web page,
all you need to do is copy and paste the link you want the program to examine,
then you choose if you want the most, or the least common word.''')

url = input('Enter URL: ') #Asks the user for the URL used to find the word

# Ignores SSL certificate. taken from:
# https://stackoverflow.com/questions/19268548/python-ignore-certificate-validation-urllib2
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# try & except in order to avoid error if the user inputs an ivalid URL
try:
    fhandle = urllib.request.urlopen(url, context=ctx).read() #sends a request, gets the HTML, and opens the file
except:
    print('Invalid URL, please try again')
    quit() #closes the program if the URL is invalid

words = dict() #creates a dictionary, will be used in the function later on the program
soup = BeautifulSoup(fhandle, 'html.parser') #uses the BeautifulSoup library to parse the HTML
text = soup.find_all("p") #gets all the 'p' tags in the HTML

def sort(file,info): #function that goes throughout the HTML and return the most/least used word
    print('generating lists...')
    time.sleep(1) #waits one second
    for line in file: #goes throughout each line in the HTML
        line = line.text #ignores the 'p' elements and only gets the text inside it
        ln = line.split() #splits the text by spaces and generates a list
        time.sleep(0.4) #waits 0.4 seconds
        print(ln) #prints the list
        for word in ln: #goes throughout each item in the list
            words[word] = words.get(word,0) + 1 #adds to the 'words' dictionary and generates tuple with a key(word) and value(count)
    word = None
    count = None
    if info =='most': #checks if the users choose the most common word, or the least common word
        userInput = 0 #this variable is used in the while loop to check the user's input
        for key,value in words.items(): #goes throughout each key/value pair in the 'words' dictionary
            if count is None or value > count: #checks the amount of times a word is used,
                word = key                     #and if it's greater than the one already in the variable
                count = value                  #it updates the variables
    elif info == 'least': #checks if the users choose the most common word, or the least common word
        userInput = 1 #this variable is used in the while loop to check the user's input
        for key,value in words.items(): #goes throughout each key/value pair in the 'words' dictionary
            if count is None or value < count: #checks the amount of times a word is used,
                word = key                     #and if it's less than the one already in the variable
                count = value                  #it updates the variables
    return word, count, userInput #returns the word, the count, and the userInput.

while True:
    result = sort(text,input('''Enter what information you want(most, or least)
     Be sure to use the words "most" or "least": ''')) #asks the user if they want the most or the least used word
                                                       #then it puts it as the second parameter of the function
    print('processing...')
    time.sleep(1) #waits one second

    if result[2] == 0: #checks if the user choose the most/least word via the userInput, which can be found in result[2].
        print(f"The most common word used is '{result[0]}' with it appearing in the text '{result[1]}' times.")
    if result[2] == 1: #checks if the user choose the most/least word via the userInput, which can be found in result[2].
        print(f"The least common word used is '{result[0]}' with it appearing in the text '{result[1]}' times.")

    keepGoing = input('do you want to try again? ') #asks the user if they want to try again, stores it in the variable 'keepGoing'
    if keepGoing == 'yes': #checks if the user's input is 'yes'
        url = input('Enter URL: ') #Asks the user for the URL used to find the word
        # try & except in order to avoid error if the user inputs an ivalid URL
        try:
            fhandle = urllib.request.urlopen(url, context=ctx).read() #sends a request, gets the HTML, and opens the file
        except:
            print('Invalid URL, please try again')
            quit() #closes the program if the URL is invalid

        words = dict() #creates a dictionary, will be used in the function later on the program
        soup = BeautifulSoup(fhandle, 'html.parser') #uses the BeautifulSoup library to parse the HTML
        text = soup.find_all("p") #gets all the 'p' tags in the HTML

    elif keepGoing == 'no': #checks if the user's input is 'no'
        print('Bye bye')
        quit() #ends the program
