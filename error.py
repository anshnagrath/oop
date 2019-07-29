import requests
from json import JSONDecodeError
num = input("Enter a number :")

try:
    print(int(num)*2)
except  ValueError:
      print("Please enter a proper number")  


r =  requests.get('http://text-processing.com/api/sentiments',data={'text':'hello world'})
try:
    label = r.json()['label']
    print(label);    
except JSONDecodeError:
    print('unable to decode json')
except KeyError:
    print('unable to find label key')       