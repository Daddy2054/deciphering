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
def different_numbers(texts, calls):
    different_numbers = set()
    for text in texts:
        different_numbers.add(text[0])
        different_numbers.add(text[1])
    for call in calls:
        different_numbers.add(call[0])
        different_numbers.add(call[1])
    return len(different_numbers)

print("There are {} different telephone numbers in the records.".format(different_numbers(texts, calls)))