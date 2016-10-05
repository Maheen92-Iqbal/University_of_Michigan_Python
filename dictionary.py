filename = raw_input('Enter the filename: ');
openfile = open(filename, 'r');

person = list()
count = dict()
maxi = 0

for line in openfile:
    
    line = line.rstrip()
    if line.startswith('From '):
        
        words = line.split()
        person.append(words[1])

      
for key in person:
    
    count[key] = count.get(key,0) + 1

for maximum in count:
    
    if count[maximum] > maxi:
        
        maxi = count[maximum]
        name = maximum
        
print name,':',maxi