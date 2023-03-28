import json

x = '{"name":"Anil","age":25,"city":"Butwal"}'

# parse json
y = json.loads(x)
print(y["name"])

# stringify json
j = {
    "name": "Jhon",
    "age": 30,
    "city": "New York"
}

k = json.dumps(j)
print(k)

# To json string
print(json.dumps({"name": "John", "age": 30})) #dict
print(json.dumps(["apple", "bananas"]))        #list
print(json.dumps(("apple", "bananas")))        #tuple
print(json.dumps("hello"))                     #string
print(json.dumps(42))                          #int
print(json.dumps(31.76))                       #float
print(json.dumps(True))                        #True
print(json.dumps(False))                       #False
print(json.dumps(None))                        #None

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = "))) # indent => indentation separators => relpaces , with . & : with =