import urllib.request,urllib.error,urllib.parse
import json

url='http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address=input('Enter location')
    if len(address)<1:break

    url2=url+urllib.parse.urlencode({'address':address})
    print('Retrieving',url)
    uh=urllib.request.urlopen(url2)
    data=uh.read().decode()
    print('Retrieve',len(data),'characters')
    try:
        js=json.loads(data)
    except:
        js=None
    if not js or 'status' not in  js or js['status']!='OK':
        print('===Failure to retrieve')
        print(data)
        continue

    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    print('lat: ',lat,' lng: ',lng)
    location=js['results'][0]['formatted_address']
    print(location)