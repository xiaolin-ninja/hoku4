from flask import Flask
from dateutil import parser
import json
# ------------------------------------------------- #

app = Flask(__name__)
app.secret_key = 'supertopsecret'

@app.route("/runs", methods=['POST'])
def time_states():
	"""Takes in state changes data of a test run 
		and returns time spent on each state.
		>>> time_states()
		{ "pending_seconds": 3,
		  "creating_seconds": 7,
		  "building_seconds": 10,
		  "running_seconds": 2
		}
	"""
	
1. collect all statuses
2. measure time of status

for x in list:
	x['status']
	pending
	creating 
	building 
	running 

	** ignore 
	errored
	failed
	succeeded
	cancelled
	x['created_at']
	x['updated_at']

def load_webhooks(json_file):
	for w in json_file:


def load_webhooks_data(json_file):
	with open(json_file) as f:
		webhooks = json.loads(f.read())
		return webhooks

# ------------------------------------------------- #

app.run(port=8080)