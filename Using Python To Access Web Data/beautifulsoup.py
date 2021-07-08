import urllib.request,urllib.parse,urllib.error
import beautifulsoup

url='http://en.wikipedia.org/wiki/Python_(programming_language)'

html=urllib.request.urlopen(url).read()
soup=beautifulsoup(html,'html.parse')

tags=soup('a')
for tag in tags:
    print(tag.get('href',None))
