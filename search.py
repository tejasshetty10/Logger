#!/opt/python-2.6-64/bin/python

import requests
import json

def search(pattern):
    ########### These fields are subject to change as per your requirements ##################
    environment = "PRD";
    application = ["HOS"];
    logTypes = ["FE"] 
    ###################################
    headers = {'content-type': 'application/json'} #Defines the type of content reverted
    instance_url = "https://loggingfacility.amadeus.com/v3/rest/search/start"
    duration = "PT2M"
    url=[]
    
    #####Trigger Search request#####
    #With multi-pattern
    for item in pattern:
        multiPattern = item[1:len(item)]
        timeStamp = item[0][0][0:10]+'T'+item[0][0][11:19]+'.000Z' #Generating time stamp
        data = json.dumps({'phase': environment, 'applications': application, "startTime":timeStamp, "duration": duration,  "complexPattern":multiPattern,  "types":logTypes})
        req = requests.post(instance_url, auth=('tshetty', 'Excalibur1@'), data=data, headers=headers) #Sending request to the URL
        search_id = int(req.json()['searchId']) #obtaining the search ID
        url.append("https://loggingfacility.amadeus.com/v3/#/log-viewer/search-id/"+str(search_id)) #Listing all the URLs
    
    
    return url