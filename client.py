'''
/*
 * @Author: Pasindu Akalpa 
 * @Date: 2021-01-24 19:38:00 
 * @Last Modified by: Pasindu Akalpa
 * @Last Modified time: 2021-01-24 19:45:21
 */
'''
import requests
import json
import numpy as np

url = 'http://0.0.0.0:5000/api/'#change to '0.0.0.0' your IPv4 address same address used in api.py

data = [[6.9,3.1,5.1,2.3]]
j_data = json.dumps(data)
print(j_data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
result = eval(r.text).partition('.')
print(result[0])