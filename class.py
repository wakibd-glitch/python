country_code = {
    'india' : '09711',
    'australia' : '124142',
    'nepal' : '768678'

}

print("country code for india: ")
print(country_code.get("india", 'not found'))

print("country code for japan: ")
print(country_code.get("japan", 'not found'))