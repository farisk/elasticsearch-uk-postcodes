import postcode_query

def displayResult(res):
    if not res:
        print('postcode not valid!')
    else:
        print(res.json())

displayResult(postcode_query.postcodeSearch('YO607SE'))
displayResult(postcode_query.postcodeSearch('YO60 7SE'))
displayResult(postcode_query.postcodeSearch('yo60 7se'))

displayResult(postcode_query.postcodeSearch('S 5 7 j X '))

displayResult(postcode_query.postcodeSearch('ZQTPD'))