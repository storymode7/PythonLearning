#!/usr/bin/env python3
#This program checks if google's doodle has changed
#And reports current doodle, if any 
import requests
from re import finditer
req=requests.get('https://www.google.com')
if req.status_code == 404 :
    print('Error accesing www.google.com')
    exit()
#with open('gcont','rb') as fobj :
 #   google=fobj.read()  
google=req.content
position=[]
try :
    for m in finditer(b'meta content=',google ) :
        position.append((m.start(),m.end()))
    for m in finditer(b'"',google) :
        if m.start() > position[2][1] :
            meta_end=m.start()
            break
except :
    print('Cannot detect any event')
    exit()
meta_content=google[position[2][1]+1:meta_end]
event=meta_content.replace(b'&#8217;',b'\'' )
event=event.decode('utf-8')
print("Google's doodle changed \n {} \n Today !" .format(event) )

