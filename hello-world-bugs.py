# Hello World Bugs

import requests
import httplib

def Test():
    taint = requests.get('example.com').text
    http = httplib.HTTP(host='host', port='port', strict='strict')
    http.putheader(taint)

response = requests.get('https://gmail.com', verify=False) # BAD_CERT_VERIFICATION defect here

name = input("What is your name?\n")
print("Hello, ", name)

def my_bad_evil_func():
    print("This function does something really bad and should not be called\n")

my_bad_evil_func()
