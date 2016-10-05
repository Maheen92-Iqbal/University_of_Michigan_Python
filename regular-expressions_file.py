import re

count = 0

output = 0

#D:/python/university_of_michigan/expression2.txt

filename = raw_input('Enter the Filename: ')

input_file = open(filename, 'r')

for line in input_file:
        
    line = line.rstrip()
    
    result = map(int, re.findall('[0-9]+', line))
    
    for key in result:
    
        count = count + 1  #count for the total number of values
        
        output = output + key #sum of all these numbers that were in the list formed by findall
        
print output,count
    