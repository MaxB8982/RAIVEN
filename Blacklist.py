# Imports Textfinder (very subtle, I know)
import Textfinder
# Imports "regular expression", it allows us to compare strings
import re
def grade (url):
  # Turns blacklist.txt into a list of each word in the file
  blacklistFile = open("blacklist.txt", 'r')
  blacklistRaw = blacklistFile.readlines()
  blacklist = []
  for i in blacklistRaw:
    blacklist.append(i.strip())
  # Calls upon the body of a website
  body = Textfinder.isolate(url)
  count = 0
  # Goes through the entire body of the paragraph for each word in blacklist, counting eachtime a blacklisted word pops up
  for i in blacklist:
    a = re.split(r'\W', body)
    count += a.count(i)
  # gives a number for the amount of blacklisted words compared to the length of the website
  grade = len(a) / count
  # Grades the body based on the grade (Subject to change, blacklist needs to be worked on)
  if grade <= 1:
    return 10 # A
  elif grade <= 1.5:
    return 8 # B
  elif grade <= 2:
    return 6 # C
  elif grade <= 2.5:
    return 4 # D
  elif grade > 2.5:
    return 2 # F
  else:
    return int(-1) # Something messed up