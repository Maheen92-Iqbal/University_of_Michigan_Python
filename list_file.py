filename = raw_input('Enter the filename:')

openfile = open(filename, 'r')

lst = list()
for line in openfile:
    
    line = line.rstrip()
    words = line.split()
    for i in words:
      if i not in lst:
        lst.append(i)
        lst.sort()

print lst
