import json
from werkzeug.wrappers import Request, Response

with open('outputFile.json') as disha:
 data = json.load(disha)
print(data)
print(data['address'])