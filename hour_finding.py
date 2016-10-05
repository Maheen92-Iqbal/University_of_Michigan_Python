filename = raw_input('Enter the file: ')

openfile = open(filename,'r')

result = list()
count = dict()

for line in openfile:
    
    if line.startswith('From '):
        
        line = line.rstrip()
        words = line.split()
        
        hour = words[5].split(':')
        result.append(hour[0])
        
for key in result:
    
    count[key] = count.get(key,0) + 1

keys = count.keys()
keys.sort()

for i in keys:
    
    print i, count[i]
