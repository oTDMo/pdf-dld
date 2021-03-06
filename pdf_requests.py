import requests
import json
from base64 import b64encode

source_url = 'http://www.nimoz.pl/files/publications/4/loremipsum.pdf'

r_get = requests.get (source_url)

err = "Something went wrong :("

# print(r.status_code)
# print(r.headers)
# print(r.content)
# print(base64.b64decode(r.text))

if r_get.status_code != 200:
    data = {
        'pdf_content': err
    }
else:    
    b64_encoded = b64encode(r_get.content)
    
    string_encoded = b64_encoded.decode()
    
    data = {
        'pdf_content': string_encoded
    }

data = json.dumps(data)

target_url = ''

headers = {
    'Content': 'application/json'
    # whatever else e.g. auth
}

r_post = requests.post (target_url, headers, json = data)

# use data as payload to push pdf into database via another api call

# print(data)