import requests

url = 'http://www.orimi.com/pdf-test.pdf'

r = requests.get (url)

print(r.status_code)
# print(r.headers)

file = open('test.pdf', "wb")

file.write(r.content)

file.close()