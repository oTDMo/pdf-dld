import requests
import json
from base64 import b64encode

url = 'http://www.nimoz.pl/files/publications/4/loremipsum.pdf'

r = requests.get (url)

err = "Something went wrong :("

# print(r.status_code)
# print(r.headers)
# print(r.content)
# print(base64.b64decode(r.text))

if r.status_code != 200:
    data = {
        'pdf_content': err
    }
else:    
    b64_encoded = b64encode(r.content)
    
    string_encoded = b64_encoded.decode()
    
    data = {
        'pdf_content': string_encoded
    }

data = json.dumps(data)

# use data as payload to push pdf into database via another api call

# print(data)