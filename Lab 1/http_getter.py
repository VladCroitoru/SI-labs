from urllib2 import urlopen


url = 'http://agora.md/categorii/actual'
response = urlopen(url)
#data = str(response.read())
#print(data)
print(str(response.read())