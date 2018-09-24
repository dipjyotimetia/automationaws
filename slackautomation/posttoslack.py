# coding: utf-8
import requests
url='https://hooks.slack.com/services/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'
data = {"text":"Hello World"}
requests.post(url, json=data)
