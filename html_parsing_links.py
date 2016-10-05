import urllib
from BeautifulSoup import *

url = raw_input('Enter the URL: ')

position = raw_input('Enter the Position: ')

count = raw_input('Enter the Count: ')

for i in range(0,int(count)):
    
    url_link = urllib.urlopen(url).read()

    html = BeautifulSoup(url_link)

    tags = html('a')
    
    url = tags[int(position)-1].get('href',None)
        
    print url