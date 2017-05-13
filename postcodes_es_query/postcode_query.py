import requests
from ukpostcodeutils import validation

ES_URL = 'http://127.0.0.1:9200/postcodes/postcode/_search'
def postcodeSearch(postcode):
    postcode_id = postcode.replace(' ','').upper()
    if validation.is_valid_postcode(postcode_id):
        searchQuery = {
            "query": {
                "ids" : {
                    "type" : "postcode",
                    "values" : postcode_id
                }
            }
        }
        return requests.get(ES_URL,json=searchQuery)
    else:
        return False #return false for invalid postcode