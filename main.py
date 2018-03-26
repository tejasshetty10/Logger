#!/opt/python-2.6-64/bin/python

from pattern_generator import generator
from search import search
hosted=open('temp_file','r') #Temp file contains the data from Hosted
pattern=[]
for row in hosted:
    pattern.append(generator(row.rstrip('\r\n'))) #Variable 'pattern' contains the search patterns for all the suspicious bookings
    
hosted.close()
url=search(pattern)
hos_u=open('hosted_URL','w')
for item in url:
    item.rstrip('\r')
    hos_u.write(item+'\n')

hos_u.close()