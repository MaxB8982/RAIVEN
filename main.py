# https://realpython.com/python-formatted-output/
# https://www.akc.org/dog-breeds/
# https://www.cnn.com/2021/01/19/politics/national-guard-removed-inauguration-duty/index.html
from bottle import route, run, request
import Yearsold
import Textfinder
import Blacklist
import TLD

# add / to localhost/8080
@route('/')
def give_main():
    #get the url of the current page
    url = request.query.url
    #grade the date the page was published
    date_grade = Yearsold.compute(url)
    #blacklist_grade = Blacklist.grade(url)
    #change this^^^^^
    #isolate the text of the page from misc. code stuff
    text_content = Textfinder.isolate(url)
    #grade the URL ending
    tld_grade = TLD.grade_url(url)
    #final_grade = empty list
    final_grade = []
    #if the grade for the publish date is greater then two...
    if (date_grade >= 2):
        #add to final_grade list
        final_grade.append(date_grade)
        #rturned_date_stuff = string
        returned_date_stuff = ("This source got a " + str(date_grade) + " out of 10 for publish date. Older sources tend to be less reliable since their information may no longer be relevent.")
    #if the date grading function returns an error...
    elif (date_grade == int(-1)):
        #returned_date_stuff = error string
        returned_date_stuff = ("Sorry, an error occurred in the grading process for the publish date.")
    #elif (blacklist_grade >= 2):
        #final_grade.append(blacklist_grade)
        #returned_blacklist_stuff = (" This source got a " + str(blacklist_grade) + " out of 10 for the amount of bias. Sources that are biased towards a certain opinion tend to be less reliable.")
    #elif (blacklist_grade == int(-1)):
        #returned_blacklist_stuff = (" Sorry, an error occurred in the grading process for bias.")
    #if the url ending grade is more or equal to 2...
    if (tld_grade >= 2):
        final_grade.append(tld_grade)
        #returned_url_stuff = string
        returned_url_stuff = ("This source got a " + str(tld_grade) + " out of 10 for it's url ending. Different url endings have varying degrees of credibility.")
    #if the bias grading returns an error...
    elif (tld_grade == int(-1)):
        #returned_url_stuff = error string
        returned_url_stuff = ("Sorry, an error occurred in the grading process for the url ending.")
    #do math to figure out the total score
    num_of_stuff = len(final_grade)
    all_stuff_added = sum(final_grade)
    Total_score = all_stuff_added/num_of_stuff
    Total_score_string = ("The total score for this source is " + str(Total_score) + ".")
    #send returned_date_stuff and returned_url_stuff back to the google extension
    return("{0} {1} {2}".format(returned_date_stuff, returned_url_stuff, Total_score_string))

#this is how the google extension accesses the stuff returned by main.py
run(host='localhost', port=8080, debug=True)