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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
unique_text_rx_numbers = set()
for index in range(len(texts)):
    unique_text_rx_numbers.add(texts[index][0])
    unique_text_rx_numbers.add(texts[index][1])
for index in range(len(calls)):
    unique_text_rx_numbers.add(calls[index][1])

marketing_numbers = set()
for index in range(len(calls)):
    if calls[index][0] not in unique_text_rx_numbers:
        marketing_numbers.add(calls[index][0])


print("These numbers could be telemarketers: ")
for phone in sorted(marketing_numbers):
    print(phone)


