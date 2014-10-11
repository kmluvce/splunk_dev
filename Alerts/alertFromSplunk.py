#alertFromSplunk.py

import sys
import urllib2
import json
from subprocess import call

# store params passed Splunk as optional alert properties
details = {
   "numberOfEvents":sys.argv[1],
   "terms":sys.argv[2],
   "query":sys.argv[3],
   "url":sys.argv[6],
   "reason":sys.argv[5],
   "searchName":sys.argv[4]
}
# populate the map that contains alert properties
alertProps = {
   "customerKey":"8983defb-784c-4e3d-a850-1865e5897367",
   "message":sys.argv[5],
   "recipients":"recepients name",
   "source":"Splunk",
   "details":details
}
jdata = json.dumps(alertProps)
response = urllib2.urlopen("https://api.opsgenie.com/v1/json/alert", jdata)

perlfile="filenamewithcompletepath"

call("perl " + perlfile, shell=True)

