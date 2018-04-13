###Test Status Timer

## Getting Started

    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python server.py

Servers runs on: http://localhost:8080/

##Launch
`curl -X POST http://localhost:8080/runs -H "Content-Type: application/json" -d @test-runs.json`

Replace 'test-runs.json' with any json webhooks data

##Built With
Python3


## File structure

    .
    ├── server.py                # Flask RESTful web API
    ├── helpers.py          	 # Helper functions to parse and convert data Defines requirements
    └── test-runs.json           # Test webhooks data