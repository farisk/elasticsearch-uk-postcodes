import requests
from ukpostcodeutils import validation


#Given elasticsearch server address and port, return a function for querying postcode index
#Does validation on postcode before making the request.
#Returns false if invalid postcode, otherwise returns json of request 
def createPostcodeSearcher(elasticSearchAddress = '127.0.0.1', port=9200):
    ES_URL = 'http://' + elasticSearchAddress + ':' + str(port) + '/postcodes/postcode/_search'
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
            return requests.get(ES_URL,json=searchQuery).json()
        else:
            return False #return false for invalid postcode
    return postcodeSearch

#return actual document if postcode was found, else return false.
def parseResult(result):
    results = result['hits']['hits']
    if (len(results) > 0):
        return results[0]['_source']
    return False