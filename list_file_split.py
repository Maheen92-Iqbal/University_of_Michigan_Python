filename = raw_input('Enter the filename:')

openfile = open(filename, 'r')
count = 0

for line in openfile:
    
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print words[1]
        count = count + 1
        
print "There were", count, "lines in the file with From as the first word"