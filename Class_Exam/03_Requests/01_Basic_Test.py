import requests
import re   # Regular Expression

data = {
    'name': 'TuringGu',
    'age': 20
}

r1 = requests.get('http://httpbin.org/get', params=data)

r2 = requests.get('https://static1.scrape.cuiqingcai.com/')
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
titles = re.findall(pattern, r2.text)

r3 = requests.post("http://httpbin.org/post", data=data)


# Get Json type data
print("Raw data r1 output:")
print(r1.text)
print("Json type r1 output:")   
print(type(r1.text))
print(r1.json())     # Return result should be json type, otherwise get error info
print(type(r1.json()))

# Print Title of r2
print("\n\nThe title of r2")
print(titles)

# Print Post of r3
print("\n\nPost data of r3")
print(r3.text)