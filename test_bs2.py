'''
Created on 2016-5-5

@author: hys mac
'''
from bs4 import BeautifulSoup
import re

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
soup = BeautifulSoup(''.join(doc))

print (soup.prettify())

print ( )
soup.contents[0].name
# u'html'
print ( )
soup.contents[0].contents[0].name
# u'head'
print ( )
head = soup.contents[0].contents[0]
head.parent.name
# u'html'
print ( )
head.next
# <title>Page title</title>
print ( )
head.nextSibling.name
# u'body'
print ( )
head.nextSibling.contents[0]
# <p id="firstpara" align="center">This is paragraph <b>one</b>.</p>
print ( )
head.nextSibling.contents[0].nextSibling
# <p id="secondpara" align="blah">This is paragraph <b>two</b>.</p>