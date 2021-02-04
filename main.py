# https://realpython.com/python-formatted-output/
# https://www.akc.org/dog-breeds/
# https://www.cnn.com/2021/01/19/politics/national-guard-removed-inauguration-duty/index.html
from bottle import route, run, request
import Yearsold
import Textfinder
import Blacklist

# add / to localhost/8080
@route('/')
def give_main():
    #get the url of the current page
    url = request.query.url
    #grade the date the page was published
    date_grade = Yearsold.compute(url)
    #blacklist_grade = Blacklist.grade(url)
    #isolate the text of the page from misc. code stuff
    text_content = Textfinder.isolate(url)
    #final_grade = empty list
    final_grade = []
    #if the grade for the publish date is greater then two...
    if (date_grade >= 2):
        #add to final_grade list
        final_grade.append(date_grade)
        #rturned_date_stuff = string
        returned_date_stuff = ("This source got a " + str(date_grade) + " out of 10. Older sources tend to be less reliable since their information may no longer be relevent.")
    #if the date grading function returns an error...
    elif (date_grade == int(-1)):
        #returned_date_stuff = string
        returned_date_stuff = ("Sorry, an error occurred.")
    #elif (blacklist_grade >= 2):
        #final_grade.append(blacklist_grade)
        #returned_blacklist_stuff = (" This source got a " + str(blacklist_grade) + " out of 10. Sources that are biased towards a certain opinion tend to be less reliable.")
    #elif (blacklist_grade == int(-1)):
        #returned_blacklist_stuff = (" Sorry, an error occurred.")
    #send this back to the google extension:
    return(returned_date_stuff)

#this is how the google extension accesses the stuff returned by main.py
run(host='localhost', port=8080, debug=True)