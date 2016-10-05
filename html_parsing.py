import urllib
from BeautifulSoup import *

count = 0
total = 0
url = raw_input('Enter the URL: ')

url_link = urllib.urlopen(url).read()

html = BeautifulSoup(url_link)

numbers = html('span')

for num in numbers:
    
    digits = int(num.contents[0])
    total = total + 1
    count = count + digits
    
    
print count
print total