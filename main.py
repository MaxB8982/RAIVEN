# https://realpython.com/python-formatted-output/
# https://www.akc.org/dog-breeds/
#The error it returns on a failed request "InvalidStateError"
from bottle import route, run, request
import Yearsold
import Textfinder

@route('/')
def give_main():
    url = request.query.url
    date_grade = Yearsold.compute(url)
    find_text = Textfinder.isolate(url)
    return("This source got a " + str(date_grade) + " out of 10. Older sources tend to be less reliable since their information may no longer be relevent.")

run(host='localhost', port=8080, debug=True)