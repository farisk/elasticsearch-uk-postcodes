import postcode_query


print(postcode_query.postcodeSearch('YO607SE').json())
print(postcode_query.postcodeSearch('YO60 7SE').json())
print(postcode_query.postcodeSearch('yo60 7se').json())

print(postcode_query.postcodeSearch('S 5 7 j X ').json())