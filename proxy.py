#import utf-8
import requests
import urllib.parse

url = "https://score.hsborges.dev/api/score"

response = requests.get(url)

print(response.text)