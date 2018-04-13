import json
from dateutil import parser
# ------------------------------------------------- #

def parse_webhooks(webhooks):
	"""parses testing data to extract testing states, start times, & end times
	   omits any data from a terminal state ('errored', 'failed', 'suceeded', or 'cancelled')
	   collects results in a list of tuples, where
	   tuple[0] = status
	   tuple[1] = start time (string)
	   tuple[2] = end time (string) 
	"""

	# list of terminal states we want to ignore
	terminal = ['errored', 'failed', 'succeeded', 'cancelled']

	results = []
	for w in webhooks:
	# the state information is nested under 'data'
		data = w['data']
		status = data['status']
		if status not in terminal:
			results.append((status, data['created_at'], data['updated_at']))
	return results

def convert_UTC(string):
	datetime = parser.parse(string)
	return datetime

# secs = (d2-d1).total_seconds()
# print(secs)