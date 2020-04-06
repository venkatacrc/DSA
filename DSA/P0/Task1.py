"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_numbers = set()

for index in range(len(texts)):
    unique_numbers.add(texts[index][0])
    unique_numbers.add(texts[index][1])
for index in range(len(calls)):
    unique_numbers.add(calls[index][0])
    unique_numbers.add(calls[index][1])

print(f"There are {len(unique_numbers)} different telephone numbers in the records.")

print(len(texts))
print(len(calls))