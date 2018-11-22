#!/usr/bin/python3

import re
import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

stock = input("Enter the stock name: ")
url = "https://www.google.com/search?tbm=fin&ei=dLH2W_K2O4L_rQGfhaqACA&q=" + stock


req = urllib.request.Request(url=url, headers=headers)
html = urllib.request.urlopen(req).read()

data = html.decode("utf-8")

data1 = re.search("zJFzKq8ukm8", data)

start = data1.end() + 2
end = start + 10

data2 = data[start:end]

m = re.search("<", data2)

start = 0
end = m.start()

final = data2[start:end]
print("Stock value of " +stock+ " is " +final)
