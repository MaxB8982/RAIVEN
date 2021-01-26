# https://realpython.com/python-formatted-output/
# https://www.akc.org/dog-breeds/
# https://www.cnn.com/2021/01/19/politics/national-guard-removed-inauguration-duty/index.html
from bottle import route, run, request
import Yearsold
import Textfinder

@route('/')
def give_main():
    url = request.query.url
    date_grade = Yearsold.compute(url)
    find_text = Textfinder.isolate(url)
    final_grade = []
    if (date_grade >= 2):
        final_grade.append(date_grade)
        returned_date_stuff = ("This source got a " + str(date_grade) + " out of 10. Older sources tend to be less reliable since their information may no longer be relevent.")
    elif (date_grade == -1):
        returned_date_stuff = ("Sorry, we cannot find the publish date.")
    return(returned_date_stuff)

run(host='localhost', port=8080, debug=True)