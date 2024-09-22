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
TELEMARKETER_PREFIX = "140"

def texters(texts):
    texters = set()
    for text in texts:
        texters.add(text[0])
        texters.add(text[1])
    return texters


def not_called(calls):
    callers = set()
    textingers=texters(texts)
    for call in calls:
        num1 = call[0]
        if not num1.startswith(TELEMARKETER_PREFIX):
              if num1 not in textingers:
                callers.add(num1)
    for call in calls:
        num2=call[1]
        if num2 in callers:
          callers.remove(num2)
    
    return callers

print("These numbers could be telemarketers: ")
print ("\n".join(sorted(not_called(calls))))