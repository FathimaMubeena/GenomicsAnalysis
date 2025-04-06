import this
from collections import counter # counter is a great tool to use its quicker,easier to read & its litrelly just one line
# Variables and Some Arithmetic
a = 3
b = 5
result = a**2 + b**2
print(f'(a)^A2 + (b^A2 = {result}')

# Strings and Lists luan
wordOneStartPos = 22
wordoneEndPos = 27
wordTwoStartPos = 97
wordTwoEndPos = 102
txtStr = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhis"
# Note:end position is not inclusive, so we add 1 to capture it
print(f'{txtStr[wordOneStartPos:wordOneEndPos + 1]} {txtStr[wordTwoStartPos:wordTwoEndPos + 1]} ')

## Conditions and Loops
startPos = 100
endPos = 200
# result =  0
# for x in range(startPos, endPos + 1):
#     if x % 2 != 0:
#         result += x
# result is going to be list of values
result = sum([x for x in range(startPos,endPos + 1) if x % 2 != 0])

print(result)
# so result has to be a one single value - an integer which is accumulation of all X : slo: using built in sum function

#Working with Files
# we store in a file list because its easier to actually navigates through the list and work with list entries  
outputFile = []
with open ('village_all problem/input.txt','r') as f:
    # and we are using list comprehension and using enumerate function- it is going to return every thing a line from this file and it is going to return a second
    # value which is a position and that is what we need to make a decision if it is an odd numbered line or not
    # F. resd lines is going to read all of the lines from our file and dump them into the list as well
    outputFile = [line for pos,line in enumerate(
    f.readlines()) if pos % 2 != 0]
print(outputFile)
#instead of reading wr are opening our file with right permission so we need to write our stuff and thats even easier
# with open( 'village/out.txt',"W') as f:
#     f.write(''.join([line for line in outputFile]))


# Dictionaries
txtStr = "We tried list and we tried dicts also we tried Zen"
# Generic approach:
# we wre going to store in a dictionary, we are going to find "we" word, and we are going to write that in two dictionary as a key and value would be how many
# times it was found and we are going to keep incrementing it by one every time we find it
# wordCoutDict = {}
# # here we loop through our test string but we are using a split and splitting it by spaces
# for word in txtStr.split(' '):
#     if word in wordCoutDict:
#         wordCoutDict [word] += 1
#     else:
#         wordCoutDict [word] = 1

# we need to print out our dictionary, we are going to use for loop here as well to
# lwts go through keys and values; keys - words and values - numbers ; how may times that were found in that sentences or the list
# because we are converted that in to the list right here and when of course we will have to use items (in code) because dictionary has items which are keys and valuses
# and we are printing out
# using counter,comment this above code include word dictionary,
# ( when we run of counter so we dont need to predefined like we did here & populate the data in that dictionary
# Optimized, Pythonic approach, using collection module:
wordCoutDict = Counter(txtStr.split(' '))
for key,value in wordCoutDict. items():
    print(key, value)