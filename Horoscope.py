import requests
sign = input("Please enter your zodiac sign")
day = input("Please enter the horoscope day (today, tomorrow, yesterday)")

params = (
('sign', sign),
('day' , day )    
)
response = requests.post('https://aztro.sameerkumar.website/',params=params )

json = response.json()
##print(response.json())

print("Horoscope for",json.get('current_date'),"\n ")
print(json.get('description'),"\n")
print('Compatibility:',json.get('compatibility'))
print('mood:',json.get('mood'))
print('color:',json.get('color'))
print('lucky number:',json.get('lucky_number'))
print('Lucky time:',json.get('lucky_time'), "\n")