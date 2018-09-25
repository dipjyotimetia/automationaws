import boto3
session = boto3.Session(profile_name='pythonautomation')
as_client = session.client('autoscaling')
as_client.execute_policy(AutoScalingGroupName='slackautomationasg', PolicyName='slackautomationasg', MetricValue=59, BreachThreshold=59)
