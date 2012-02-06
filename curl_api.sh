#!/bin/sh

curl http://localhost:6767/todo/ | python -mjson.tool

curl -H "content-type: application/json" -f -X POST -d '{"id": "111b4bb7-55f5-441b-ba25-c7a4fd99442c", "text": "Watch more bsg", "order": 1}' http://localhost:6767/todo/111b4bb7-55f5-441b-ba25-c7a4fd99442c/ | python -m json.tool

curl -H "content-type: application/json" -f -X POST -d '{"id": "222b4bb7-55f5-441b-ba25-c7a4fd994421", "text": "Watch Blade Runner", "order": 2}' http://localhost:6767/todo/222b4bb7-55f5-441b-ba25-c7a4fd994421/ | python -m json.tool

curl http://localhost:6767/todo/ | python -mjson.tool

curl http://localhost:6767/todo/222b4bb7-55f5-441b-ba25-c7a4fd994421/ | python -mjson.tool

curl -H "content-type: application/json" -f -X DELETE http://localhost:6767/todo/222b4bb7-55f5-441b-ba25-c7a4fd994421/ 

curl http://localhost:6767/todo/ | python -mjson.tool

curl -H "content-type: application/json" -f -X POST -d '[{"id": "333b4bb7-55f5-441b-ba25-c7a4fd99442c", "text": "Write more Brubeck code", "order": 3},{"id": "444b4bb7-55f5-441b-ba25-c7a4fd994421", "text": "Drink coffee", "order": 4}]' http://localhost:6767/todo/ | python -m json.tool

curl http://localhost:6767/todo/ | python -mjson.tool

curl -H "content-type: application/json" -f -X POST -d '{"id": "b4bb7-55f5-441b-ba25-c7a4fd994421", "text": "Watch Blade Runner", "order": 2}' http://localhost:6767/todo/222b4bb7-55f5-441b-ba25-c7a4fd994421/ | python -m json.tool

curl -H "content-type: application/json" -f -X POST -d '{"id": "b4bb7-55f5-441b-ba25-c7a4fd994421", "text": "Watch Blade Runner", "order": 2}' http://localhost:6767/todo/b4bb7-55f5-441b-ba25-c7a4fd994421/ | python -m json.tool
