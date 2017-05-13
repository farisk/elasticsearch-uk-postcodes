import postcode_query

def displayResult(res):
    if not res:
        print('postcode not valid!')
    else:
        print('RAW',res)
        print('PARSED', postcode_query.parseResult(res))

postcodeSearcher = postcode_query.createPostcodeSearcher('127.0.0.1',9200)
displayResult(postcodeSearcher('YO607SE'))
displayResult(postcodeSearcher('YO60 7SE'))
displayResult(postcodeSearcher('yo60 7se'))

displayResult(postcodeSearcher('S 5 7 j X '))

displayResult(postcodeSearcher('ZQTPD'))
displayResult(postcodeSearcher('s6 7Sz'))