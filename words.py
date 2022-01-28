import time
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

print('''Hello, this program will calculate the most used word in a web page,
all you need to do is copy and paste the link you want the program to examine,
then you choose if you want the most, or the least common word.''')
url = input('Enter URL: ')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    fhandle = urllib.request.urlopen(url, context=ctx).read()
except:
    print(url)
    quit()

words = dict()
soup = BeautifulSoup(fhandle, 'html.parser')
text = soup.find_all("p")

def sort(file,info):
    for line in file:
        line = line.text
        ln = line.split()
        for word in ln:
            words[word] = words.get(word,0) + 1
    sender = None
    count = None
    if info =='most':
        userInput = 0
        for key,value in words.items():
            if count is None or value > count:
                sender = key
                count = value
    elif info == 'least':
        userInput = 1
        for key,value in words.items():
            if count is None or value < count:
                sender = key
                count = value
    return sender, count, userInput

while True:
    result = sort(text,input('''Enter what information you want(most, or least)
     Be sure to use the words "most" or "least": '''))

    print('processing...')
    time.sleep(1)

    if result[2] == 0:
        print(f"The most common word used is '{result[0]}' with it appearing in the text '{result[1]}' times.")
    if result[2] == 1:
        print(f"The least common word used is '{result[0]}' with it appearing in the text '{result[1]}' times.")

    keepGoing = input('do you want to try again? ')
    if keepGoing == 'yes':
        url = input('Enter URL: ')
        try:
            handle = urllib.request.urlopen(url).read()
        except:
            quit()
        soup = BeautifulSoup(fhandle, 'html.parser')
        tags = soup("p")
    elif keepGoing == 'no':
        print('Bye bye')
        quit()
