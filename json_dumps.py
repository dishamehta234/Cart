import json

data={
   "firstName": "Disha",
   "lastName": "Mehta",
   "gender": "Female",
   "age": 22,
   "address": {
       "streetAddress": "Madhapar",
       "city": "Bhuj",
       "state": "Gujarat",
       "postalCode": "380020"
   },
   "phoneNumbers": [
       { "type": "home", "number": "156342789" }
   ]
}

output= open('outputFile.json', 'w')
json.dump(data, output)