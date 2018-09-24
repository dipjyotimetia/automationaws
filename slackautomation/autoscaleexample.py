# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonautomation')
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
as_client.describe_auto_scaling_policy()
as_client.describe_policies()
as_client.execute_policy(AutoScalingGroupName='slackautomationasg', PolicyName='slackautomationasg', MetricValue=59, BreachThreshold=59)
as_client.execute_policy(AutoScalingGroupName='slackautomationasg', PolicyName='slackautomation scale down', MetricValue=19, BreachThreshold=19)
as_client.describe_autoscaling_activities(AutoScalingGroupName='slackautomationasg')
as_client.describe_scaling_activities(AutoScalingGroupName='slackautomationasg')
