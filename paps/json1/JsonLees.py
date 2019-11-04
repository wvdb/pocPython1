import json

file = open('EventThomasVermaelen.json')

totalString = ''

for line in file:
    totalString += line

event = json.loads(totalString)

print("documentType =", event["documentType"])
print("scope =", event["document"]["contestEvent"]["primaryIds"][0]["scope"])
