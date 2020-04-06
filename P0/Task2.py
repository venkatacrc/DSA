"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from collections import defaultdict
import operator

numbers_dict = defaultdict(int)

for index in range(len(calls)):
    call_dutation = int(calls[index][3])
    numbers_dict[calls[index][0]] += call_dutation
    numbers_dict[calls[index][1]] += call_dutation

telephone_number = max(numbers_dict.items(), key=operator.itemgetter(1))[0]
total_time = numbers_dict[telephone_number]

print(f"{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")