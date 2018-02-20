import requests
import json
from base64 import b64encode

url = 'http://www.nimoz.pl/files/publications/4/loremipsum.pdf'

r = requests.get (url)

# print(r.status_code)
# print(r.headers)
# print(r.content)
# print(base64.b64decode(r.text))

b64_encoded = b64encode(r.content)

string_encoded = b64_encoded.decode()

data = {
    'pdf_content': string_encoded
}

data = json.dumps(data)

print(data)