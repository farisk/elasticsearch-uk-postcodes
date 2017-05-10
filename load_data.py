import csv
from pprint import pprint
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch()


postcodes_index = {
  "mappings": {
    "postcode": {
      "_all": {
        "enabled": False
      },
      "properties": {
        "postcode": {
          "type":"text",
          "index":"no"
        },
        "longitude": {
          "type": "float",
          "index":"no"
        },
        "latitude": {
          "type": "float",
          "index":"no"
        }
      }
    }
  }
}

print('If it exists delete postcodes')
print(es.indices.delete(index='postcodes', ignore=[400, 404]))

print('create postcodes index')
res = es.indices.create(index = 'postcodes', body = postcodes_index)
print(res)

actions = []
total = 0
def processRow(postcode,latitude,longitude):
    global actions
    newPostcode = {
        'postcode': postcode,
        'latitude': latitude,
        'longitude': longitude
    }
    addAction = {
        "_index": "postcodes",
        "_type": "postcode",
        "_id": postcode.replace(' ', ''),
        "_source": newPostcode
    }

    actions.append(addAction)

    if len(actions) > 5000:
        postActions()


def postActions():
    global actions
    global total
    if len(actions) > 0:
        req = helpers.bulk(es, actions)
        total = total + req[0]
        print(req, "total:", total)
        actions = []

print('adding postcodes.....')
with open('data/ukpostcodes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        processRow(row['postcode'], row['latitude'], row['longitude'])

postActions()
print('Complete!')