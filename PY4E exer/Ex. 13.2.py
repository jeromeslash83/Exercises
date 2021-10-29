import json
import urllib.request 
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter URL: ")
item = urllib.request.urlopen(url, context= ctx)
data = item.read()
infos = json.loads(data)

print('User count', len(infos))

total = 0
count = 0

for item in infos['comments']:
    total += int(item['count'])
    count += 1

print("Sum", total)
