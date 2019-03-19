#Serialization => json
#Python provides built-in JSON libraries to encode and decode JSON.
#Encoding
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

#dumps() method converts dictionary object of python into JSON string data format.
x = {
  "name": "Ken",
  "age": 45,
  "married": True,
  "children": ("Alice","Bob"),
  "pets": ['Dog'],
  "cars": [
    {"model": "Audi A1", "mpg": 15.1},
    {"model": "Zeep Compass", "mpg": 18.1}
  ]
}
# sorting result in asscending order by keys:
sorted_string = json.dumps(x, indent=4, sort_keys=True)
print(sorted_string)

#'marshal' and 'pickle' external modules of Python maintain a version of JSON library.
#Python supports a Python proprietary data serialization method called pickle (and a faster alternative called cPickle).
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

'''
dumps()	encoding to JSON objects
dump()	encoded string writing on file
loads()	Decode the JSON string
load()	Decode while JSON file read
'''
person_data = {"person": {"name": "Kenn", "sex": "male", "age": 28}}
# here we create new data_file.json file with write mode using file i/o operation 
with open('json_file.json', "w") as file_write:
# write json data into file
    json.dump(person_data, file_write)

#Decoding
# json data string
person_data = '{  "person":  { "name":  "Kenn",  "sex":  "male",  "age":  28}}'
# Decoding or converting JSON format in dictionary using loads()
dict_obj = json.loads(person_data)
print(dict_obj)
# check type of dict_obj
print("Type of dict_obj", type(dict_obj))
# get human object details
print("Person......",  dict_obj.get('person'))

with open('json_file.json') as file_object:
        # store file data in object
        data = json.load(file_object)
print(data)

'''
Encode
default(o) – Implemented in the subclass and return serialize object for o object.
encode(o) – Same as json.dumps() method return JSON string of Python data structure.
iterencode(o) – Represent string one by one and encode object o.

Decode
default(o) – Implemented in the subclass and return deserialized object o object.
decode(o) – Same as json.loads() method return Python data structure of JSON string or data.
raw_decode(o) – Represent Python dictionary one by one and decode object o.
'''

#Decoding JSON data from URL: Real Life Example
import json
import requests

# get JSON string data from CityBike NYC using web requests library
json_response= requests.get("https://feeds.citibikenyc.com/stations/stations.json")
# check type of json_response object
print(type(json_response.text))
# load data in loads() function of json library
bike_dict = json.loads(json_response.text)
#check type of news_dict
print(type(bike_dict))
# now get stationBeanList key data from dict
print(bike_dict['stationBeanList'][0]) 

#example
import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])