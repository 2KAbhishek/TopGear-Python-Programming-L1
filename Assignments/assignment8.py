#!/usr/bin/env python

import xml.etree.ElementTree as xml

e = xml.parse('bookstore.xml').getroot()

data = {}
for i in e.findall('book'):
    data[i.attrib['category']] = {
        'title': i[0].text, 'author': i[1].text, 'year': i[2].text, 'price': i[3].text}

print('Children category book Title:', data['CHILDREN']['title'])
print('Web category book Author:', data['WEB']['author'])
print('Cooking category book Price:', data['WEB']['price'])
