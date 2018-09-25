import boto3
session = boto3.Session(profile_name='pythonautomation')
as_client = session.client('autoscaling')
as_client.execute_policy(AutoScalingGroupName='slackautomationasg', PolicyName='slackautomation scale down', MetricValue=19, BreachThreshold=19)
