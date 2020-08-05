import requests
import json
import getpass 

# https://docs.servicenow.com/bundle/orlando-application-development/page/build/applications/concept/api-rest.html
# https://docs.servicenow.com/bundle/london-platform-administration/page/administer/reference-pages/reference/r_TablesAndClasses.html
# https://docs.servicenow.com/bundle/geneva-servicenow-platform/page/integrate/inbound_rest/reference/r_TableAPIPythonExamples.html
# https://www.servicenowelite.com/blog/2014/5/19/finding-the-sysid-of-a-record
# https://developer.servicenow.com/dev.do#!/reference/api/orlando/rest/c_TableAPI

 # Set the request parameters
url = 'https://conns.service-now.com/api/now/table/incident?sysparm_query=number=INC0650719&sysparm_fields=category,subcategory,u_work_type,assignment_group,contact_type'

user = getpass.getuser()   

try: 
    pwd = getpass.getpass("User Name : %s\nPassword: " % user)  
except Exception as error: 
    print('ERROR', error) 
 
 # Set proper headers
headers = {"Accept":"application/json"}
 
 # Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )
 
 # Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()
 
 # Decode the JSON response into a dictionary and use the data
print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())
# print('Cookies', response.cookies)

# serviceNowData = response.json()
# ticket = serviceNowData['result']

# textFile = open('IncidentPostData.txt', 'w')
# textFile.write('Incident Post Data String: \n\n')
# textFile.write(response)
# textFile.close()
# print(ticket)
# exit()