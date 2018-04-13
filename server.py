from flask import Flask, request, json, jsonify
from helpers import parse_webhooks, convert_UTC
from collections import OrderedDict

# ------------------------------------------------- #

app = Flask(__name__)

@app.route("/runs", methods=['POST'])
def status_timer():
	"""Takes in state changes data of a test run 
		and returns time spent on each state.
		>>> time_states('test-runs.json')
		{ "pending_seconds": 3,
		  "creating_seconds": 7,
		  "building_seconds": 10,
		  "running_seconds": 2
		}
	"""

	if request.headers['Content-Type'] != 'application/json':
		return 'Error, please pass webhooks data as json'

	# the parser returns a list of tuples where:
	# tuple[0] = status, tuple[1] = start time, tuple[2] = end time
	data = parse_webhooks(request.json)
	# since OrderedDict always returns it in the order of input
	# I decided to go through the extra step of making the dictionary
	# separately instead of within the for loop.
	state_times = OrderedDict({
				  'pending_seconds': 0,
				  'creating_seconds': 0,
				  'building_seconds': 0,
				  'running_seconds': 0
				  })

	# loop through each tuple
	for d in data:
		# d[0] is the status message
		status = d[0]
		# convert to integer to match formatting of sample answer
		time = int((convert_UTC(d[2]) - convert_UTC(d[1])).total_seconds())
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
	return jsonify(state_times)

# ------------------------------------------------- #

app.run(port=8080)