#!/usr/bin/env python3

import json
import yaml
import csv

# filename
file = 'people.csv'

# Convert the list into an list of dictionaries
with open(file) as f:
    reader = csv.DictReader(f,delimiter=",")
    people = list(reader)


# create the json file
with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

# to load people again with json structure
with open('people.json', 'r') as f:
    people = json.load(f)

# create the yaml filename
with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml) # dump command also works
