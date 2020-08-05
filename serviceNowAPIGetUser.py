import json
import requests
import getpass 


# Set the request parameters
url = 'https://conns.service-now.com/api/now/table/sys_user?sysparm_query=user_nameLIKE'#sysparm_fields=user_name,sys_id' # &sysparm_limit=10'


userName = input('Enter UserName to search: \n')

  
user = getpass.getuser()   

try: 
    pwd = getpass.getpass("User Name : %s\nPassword: " % user)  
except Exception as error: 
    print('ERROR', error) 
 
# Set proper headers
headers = {"Accept":"application/json"}

newUrl = url + str(userName) + '&sysparm_fields=user_name,sys_id,manager&sysparm_exclude_reference_link=TRUE&sysparm_display_value=TRUE'
 
# Do the HTTP request
response = requests.get(newUrl, auth=(user, pwd), headers=headers )
 
# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()
 
# Decode the JSON response into a dictionary and use the data
# print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())

serviceNowData = response.json()
users = serviceNowData['result']

for userNumber in range(0, len(users)):
	
	print(str(userNumber+1)+': '+users[userNumber]['user_name']+'('+users[userNumber]['sys_id']+')'+'('+users[userNumber]['manager']+')')

# print(type(serviceNowData))
# print(serviceNowData)


# print('Cookies', response.cookies)