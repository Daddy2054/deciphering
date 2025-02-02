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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

BANGALORE_AREA_CODE = "(080)"
FIXED_LINE_PREFIX = "("
MOBILE_PREFIX = ("7","8","9")
TELEMARKETER_PREFIX = "140"

def from_bangalore(phone_number):
    return phone_number.startswith(BANGALORE_AREA_CODE)

# part A
def called_by_080(calls):
    called = []
    for call in calls:
        num1 = call[0]
        num2 = call[1]
        if from_bangalore(num1):
            if num2.startswith(FIXED_LINE_PREFIX):
                called.append(num2[1:4])
            elif num2.startswith(MOBILE_PREFIX):
                called.append(num2[:5])
            elif num2.startswith(TELEMARKETER_PREFIX):
                called.append(TELEMARKETER_PREFIX)
    return sorted(list(set(called)))

print ("The numbers called by people in Bangalore have codes:")
for number in called_by_080(calls):
    print(number)

# part B
def local_calls_080(calls):
    local = 0
    for call in calls:
        num1 = call[0]
        num2 = call[1]
        if from_bangalore(num1) and from_bangalore(num2):
            local += 1
    return local



print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
      .format(local_calls_080(calls)/len(calls)*100))