import json
import collections

inputfile = open('./clientIdInfo')
outputfile = open('./clientIdInfo.out', 'w')

# {
#   "82": {
#     "clientId": 82,
#     "priceType": "free",
#     "os": "ios",
#     "formFactor": "universal",
#     "resolution": "universal",
#     "distributor": "apple",
#     "friendlyName": "iPad Mini"
#   },
#   "82": {
#     "clientId": 82,
#     "priceType": "free",
#     "os": "ios",
#     "formFactor": "universal",
#     "resolution": "universal",
#     "distributor": "apple",
#     "friendlyName": "iPad Mini"
#   }
# }

# attributes
client = ''
clientId = 0
priceType = ''
formFactor = ''
resolution = ''
distributor = ''
friendlyName = ''
counter = 0
data = collections.OrderedDict()

for line in inputfile:
	# remove newline at the end of the line
	line = line.rstrip('\n')
	remainder = counter % 8
	if remainder == 0:
		client = line
	elif remainder == 1:
		clientId = int(line)
	elif remainder == 2:
		priceType = line
	elif remainder == 3:
		formFactor = line
	elif remainder == 4:
		os = line
	elif remainder == 5:
		friendlyName = line
	elif remainder == 6:
		distributor = line
	elif remainder == 7:
		resolution = line
		data[clientId] = {'clientId':clientId, 'priceType':priceType, 'os':os, 'formFactor': formFactor, 'resolution': resolution, 'distributor': distributor, 'friendlyName': friendlyName}

	counter = counter + 1

data_string = json.dumps(data)
# data_string = json.dumps(data, sort_keys=True, indent=2)
print data_string
outputfile.writelines(data_string)

inputfile.close()
outputfile.close()
