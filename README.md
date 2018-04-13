###Test Status Timer

##Setup

`pip install -r requirements.txt`
`python server.py`

Servers runs on: http://localhost:8080/

##Technologies
Python3

##Usage
`curl -X POST http://localhost:8080/runs -H "Content-Type: application/json" -d @test-runs.json`
Replace 'test-runs.json' with any json webhooks data

##Content