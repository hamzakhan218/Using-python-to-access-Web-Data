import xml.etree.ElementTree as ET
data='''<person>
<name>Hamza</name>
<phone type="intl">
+92 335 4551667
</phone>
<email hide="yes" />
</person>'''

tree=ET.fromstring(data)
print('Name: ',tree.find('name').text)
print('ATTR: ',tree.find('email').get('hide'))