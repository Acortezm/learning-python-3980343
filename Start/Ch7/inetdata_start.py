# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#

import urllib.request

weburl = urllib.request.urlopen("http://www.example.com")
print("result code:", weburl.getcode())

date = weburl.read()

print(date)

