import os
import requests

def post_to_slack(event, context):
    print(event)
    slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']
    slack_message= "Testing" #From {} at {details[StartTime]}: detail{[Description]}".format(**event)
    data = {"text": slack_message}
    requests.post(slack_webhook_url, json=data)
    print(slack_webhook_url)
    return
