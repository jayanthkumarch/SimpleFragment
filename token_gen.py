import subprocess
import requests
import re
import time
import json
import httplib
import ssl
import datetime
#Added comment

conn = httplib.HTTPSConnection("www-test-ngp-cp.csp.infoblox.com",context=ssl._create_unverified_context())
request_header = {'Content-Type':'application/json','Accept': 'application/json'}
url ='/users/sign_in/'
fields ='{"user": {"password": "Cto-bonfire1*", "email": "rcmacauto_10_10@infoblox.com"}}'
conn.request("POST",url,fields, request_header)
response = conn.getresponse();
print "response",response.status
print "response read",response.read()

