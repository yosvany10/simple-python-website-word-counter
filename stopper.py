# Yosvany Blanco

# must install the "requests" module
# must also install "BeautifulSoup4" Module
# both can be found on Pip

# developed and tested on Python 3.5.2
import sys
import requests
from bs4 import BeautifulSoup
from collections import Counter
import string

# read lines of file
with open(sys.argv[2]) as f_in:
    stopWords = list(line for line in (l.strip() for l in f_in) if line)
stopWords = [x.lower() for x in stopWords] # force words to lowercase if not already

url = sys.argv[1]

r = requests.get(url)
# check that connection worked
if r.status_code != 200:
    print("Failed to connect to server error code: %d" %(r.status_code))
    print("You typed '%s' is this correct?" %(url))
    sys.exit(1)

soup = BeautifulSoup(r.content, "html.parser")

# this will return only plain text and remove html stuff
for useless in soup(["script", "style"]):
    useless.extract()

mash = soup.get_text()
mash = mash.lower() # make everything lowercase to ignore case sensitivity
mash = mash.split() # split each word by spaces

# intermediary list
inter = []
for word in mash:
    inter.append("".join(l for l in word if l not in string.punctuation))
inter = list(filter(None, inter))

# final list of words to sort
final = []
for word in inter:
    if not (word in stopWords or word.isdigit()):
        final.append(word)

counts = Counter(final)

print("Top ten words")
for word, count in counts.most_common(10):
    print("%s: %d" %(word, count))
