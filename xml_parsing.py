import xml.etree.ElementTree as ET
import urllib

total = 0

url = raw_input('Enter the URL: ')

url_link = urllib.urlopen(url).read()

tree = ET.fromstring(url_link)

tags = tree.findall('comments/comment') #finding all the name and count tags

for num in tags:
    
    number = num.find('count').text #just try to extract the count tag value
    
    total = total + int(number)
    
print total
