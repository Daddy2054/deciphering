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

def longest_time(calls):
    total = {}
    for call in calls:
        num1 = call[0]
        num2 = call[1]
        time = int(call[3])
        if num1 in total:
            total[num1] += time
        else:
            total[num1] = time
        if num2 in total:
            total[num2] += time
        else:
            total[num2] = time
    longest_num = max(total, key=total.get)
    longest_time = total[longest_num]
    return longest_num, longest_time

print("{} spent the longest time, {} seconds, on the phone during September 2016."
      .format(longest_time()[0], longest_time()[1]))