import urllib
import json


url = 'http://python-data.dr-chuck.net/geojson?'

while True:
    
    address = raw_input('Enter an address: ')
    
    if len(address) < 1: 
        
        break
        
    updated_url = url + urllib.urlencode({'sensor': 'false', 'address': address})
    
    print updated_url
    
    json_data = urllib.urlopen(updated_url).read()
    
    print 'Retrieved' , len(json_data) , 'characters'
    
    parse_json = json.loads(str(json_data))
    
    if 'status' not in parse_json or parse_json['status'] != 'OK':
        
        print '**********Failure in retreving the data**************'
        continue
    
    print json.dumps(parse_json, indent=4)
    
    print '\n'
    
    print 'Place_ID: ' + parse_json['results'][0]['place_id']
    
    