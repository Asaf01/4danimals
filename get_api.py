import requests

endpoint_url = 'https://4danimals.com/wp-json/wp/v2/posts/'


response = requests.get(endpoint_url)


if response.status_code == 200:
    
    json_data = response.json()
    
    
    print(json_data)
else:
    
    print('Error:', response.status_code)

print (response.status_code)
