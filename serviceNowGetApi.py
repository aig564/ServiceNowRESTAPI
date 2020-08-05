#Need to install requests package for python
#sudo easy_install requests
import requests
import json
import getpass 

# Set the request parameters
url = 'https://conns.service-now.com/api/now/table/incident?sysparm_query=assigned_to.nameLIKEAlfonzo^stateIN6,7^resolved_atBETWEENjavascript:gs.beginningOfLast7Days()@javascript:gs.endOfCurrentHour()'# &sysparm_fields=number,description,short_description' # &sysparm_limit=10'

  
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
# print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())

serviceNowData = response.json()

# print(type(serviceNowData))
# print(serviceNowData)

tickets = serviceNowData['result']

textFile = open('ServiceNowTicketsResolved.txt', 'w')
textFile.write('Tickets Resolved This Week: \n\n')
# print(type(tickets))
# print(tickets)
# for ticketNumber in tickets:
for ticketNumber in range(0, len(tickets)):
	currentTicket = tickets[ticketNumber]
	# print(type(currentTicket))
	# print(currentTicket)
	textFile.write(str(ticketNumber+1)+': '+tickets[ticketNumber]['short_description']+'('+tickets[ticketNumber]['number']+')\n')
	print(str(ticketNumber+1)+': '+tickets[ticketNumber]['short_description']+'('+tickets[ticketNumber]['number']+')')
textFile.close()
# print('Cookies', response.cookies)
