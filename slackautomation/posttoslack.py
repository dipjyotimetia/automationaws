# coding: utf-8
import requests
url='' #webhook removed
data = {"text":"Hello World"}
requests.post(url, json=data)
