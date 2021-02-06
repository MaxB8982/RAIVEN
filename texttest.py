import Textfinder
import re

url = 'https://www.cnn.com/2021/01/19/politics/national-guard-removed-inauguration-duty/index.html'
the_text = Textfinder.isolate(url)
position = the_text.find('Updated', 0, 200)
after_updated = the_text[position+7:]
is_month = r"jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec"

matches = re.search(is_month, after_updated[:40], re.MULTILINE | re.IGNORECASE)
print(matches)