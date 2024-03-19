import re
import requests

endpoint_url = 'https://4danimals.com/wp-json/wp/v2/posts/'

params = {'search': 'users'}

response = requests.get(endpoint_url, params=params)


if response.status_code == 200:
    
    json_data = response.json()
    
    if json_data:
        
        content = json_data[0]['content']['rendered']
        
        
        json_matches = re.findall(r'\{.*?\}', content)
        
        
        for match in json_matches:
            print(match)
    else:
        print("No posts with the title 'users' found.")
else:
    print('Error:', response.status_code)
