# from dateutil import parser

# ds1 = "2018-02-08T19:54:30Z"
# ds2 = "2018-02-08T19:54:31Z"
# d1 = parser.parse(ds1)
# d2 = parser.parse(ds2)

# secs = (d2-d1).total_seconds()
# print(secs)
import json

def parse_webhooks(json_file):
	"""parses testing data to extract testing states, start times, & end times
	   omits any data from a terminal state ('errored', 'failed', 'suceeded', or 'cancelled')
	   collects results in a list of tuples, where
	   tuple[0] = status
	   tuple[1] = start time (string)
	   tuple[2] = end time (string) 
	"""

	with open(json_file) as f:
		webhooks = json.loads(f.read())
		# list of terminal states we want ot ignore
		terminal = ['errored', 'failed', 'succeeded', 'cancelled']
		results = []
		for w in webhooks:
		# the state information is nested under 'data'
			data = w['data']
			status = data['status']
			if status not in terminal:
				results.append((status, data['created_at'], data['updated_at']))

		return results

print(parse_webhooks('test-runs.json'))