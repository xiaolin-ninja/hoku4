from dateutil import parser
# ------------------------------------------------- #

def parse_webhooks(webhooks):
	"""parses testing data to extract testing states and start/end times of each instance of the state
	   omits any data from a terminal state ('errored', 'failed', 'suceeded', or 'cancelled')
	   collects results in a list of tuples, where
	   tuple[0] = status
	   tuple[1] = start time (UTC string)
	   tuple[2] = end time (UTC string) 
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

	# I first did this with a list comprehension, but decided it was too hard to read
	# results = [(w['data']['status'], w['data']['created_at'], w['data']['updated_at']) 
	# 		  	for w in webhooks
	# 		  	if w['data']['status'] not in terminal]

def convert_UTC(string):
	"""converts UTC string to datetime object
	>>> convert_UTC('2018-02-08T19:54:30Z')
	2018-02-08 19:54:30+00:00
	"""
	datetime = parser.parse(string)
	return datetime