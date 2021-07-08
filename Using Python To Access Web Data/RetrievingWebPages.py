import urllib.request, urllib.error,urllib.parse

fhand=urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
for lines in fhand:
    print(lines.decode())
