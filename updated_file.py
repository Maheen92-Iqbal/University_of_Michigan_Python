filename = raw_input('Enter the filename:')

openfile = open(filename, 'r')

count = 0
values = 0

for line in openfile:
    
    if line.startswith('X-DSPAM-Confidence:'):
        
        count = count + 1
        
        pos1 = line.find(':')
        value = line[pos1+1:]
        values = values + float(value)
        
print 'Average spam confidence:' + ' ' + str(float(values)/count)
        