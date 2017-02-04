import datetime
import re

from django.utils.html import strip_tags


# Count words in provided string
def count_words(string, is_html=True):
    if is_html:
        string = strip_tags(string)
    return len(re.findall(r'\w+', string))


# Get read time in seconds
def get_read_time(string, is_html=True):
    count = count_words(string, is_html)
    read_time_sec = (count/200.0) * 60  # assuming 200 words per minute
    return str(datetime.timedelta(seconds=read_time_sec))
