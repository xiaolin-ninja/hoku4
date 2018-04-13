# from dateutil import parser

# ds1 = "2018-02-08T19:54:30Z"
# ds2 = "2018-02-08T19:54:31Z"
# d1 = parser.parse(ds1)
# d2 = parser.parse(ds2)
# secs = (d2-d1).total_seconds()
# print(secs)
import json

def load_webhooks_data(json_file):
	with open(json_file) as f:
		webhooks = json.loads(f.read())
		for w in webhooks:
			print w.keys()
			# print('status', w['status'])
			# print('start', w['created_at'])
			# print('end', w['updated_at'])

load_webhooks_data('test-runs.json')