from flask import Flask
from helpers import parse_webhooks, convert_UTC

# ------------------------------------------------- #

app = Flask(__name__)

@app.route("/runs", methods=['POST'])
def time_states(webhooks):
	"""Takes in state changes data of a test run 
		and returns time spent on each state.
		>>> time_states('test-runs.json')
		{ "pending_seconds": 3,
		  "creating_seconds": 7,
		  "building_seconds": 10,
		  "running_seconds": 2
		}
	"""
	# the parser returns a list of tuples where:
	# tuple[0] = status
	# tuple[1] = start time
	# tuple[2] = end time
	data = parse_webhooks(webhooks)
	state_times = {}
	for d in data:
		status = d[0]
		time = (convert_UTC(d[2]) - convert_UTC(d[1])).total_seconds()
		if status == 'pending':
			state_times['pending_seconds'] += time
		elif status == 'creating':
			state_times['creating_seconds'] += time
		elif status == 'building':
			state_times['building_seconds'] += time
		elif status == 'running':
			state_times['running_seconds'] += time
		else:
			return 'error, status not found'
	return status_times

# ------------------------------------------------- #

app.listen(port=8080)