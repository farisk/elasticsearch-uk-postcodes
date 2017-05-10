import requests
ES_URL = 'http://127.0.0.1:9200/postcodes/postcode/_search'
def postcodeSearch(postcode):
    postcode_id = postcode.replace(' ','').upper()
    searchQuery = {
        "query": {
            "ids" : {
                "type" : "postcode",
                "values" : postcode_id
            }
        }
    }
    return requests.get(ES_URL,json=searchQuery)