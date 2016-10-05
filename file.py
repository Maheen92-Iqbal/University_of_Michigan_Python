filename = raw_input('Enter the name of the file: ')

openfile = open(filename, 'r')

count = 0

for line in openfile:
    
    line = line.rstrip()
    count = count + 1
    
    print line
    
print 'The no of lines are' + ' ' + str(count)