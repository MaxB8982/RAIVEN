# https://realpython.com/python-formatted-output/
import Yearsold
url = input ("Please copy and paste the website URL so that we can check it's credibility: ")
date_grade = Yearsold.compute(url)
print("This source got a " + str(date_grade) + " out of 10. Older sources tend to be less reliable since their information may no longer be relevent.")
