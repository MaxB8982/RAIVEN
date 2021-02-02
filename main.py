# https://realpython.com/python-formatted-output/
# https://www.akc.org/dog-breeds/
# https://www.cnn.com/2021/01/19/politics/national-guard-removed-inauguration-duty/index.html
from bottle import route, run, request
import Yearsold
import Textfinder
import Blacklist

@route('/')
def give_main():
    url = request.query.url
    date_grade = Yearsold.compute(url)
    #blacklist_grade = Blacklist.grade(url)
    text_content = Textfinder.isolate(url)
    final_grade = []
    if (date_grade >= 2):
        final_grade.append(date_grade)
        returned_date_stuff = ("This source got a " + str(date_grade) + " out of 10. Older sources tend to be less reliable since their information may no longer be relevent.")
    elif (date_grade == int(-1)):
        returned_date_stuff = ("Sorry, an error occurred.")
    #elif (blacklist_grade >= 2):
        #final_grade.append(blacklist_grade)
        #returned_blacklist_stuff = (" This source got a " + str(blacklist_grade) + " out of 10. Sources that are biased towards a certain opinion tend to be less reliable.")
    #elif (blacklist_grade == int(-1)):
        #returned_blacklist_stuff = (" Sorry, an error occurred.")
    return(returned_date_stuff)

run(host='localhost', port=8080, debug=True)