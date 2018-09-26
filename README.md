# Automation with AWS


### Summary
Notifications will be sent to Slack when changes are made to an AWS account. Specifically, when an instance is launched as part of an auto-scaling group a notification will be sent to a test slack channel.

### Components:
- EC2 configuration (Boto3 with iPython)
- Auto Scaling Group + Policies (AWS Console)
- Slack Channel and Webhook (Slack App)
- Serverless Infra (Serverless)
- Lambda POST function based on cloudwatch events (AWS Console)
- AWS account with a default VPC - all EC2 configuration assumes there's a default VPC (AWS Console)


### EC2 Configuration (Optional - Exploring the use of boto3)
You can just configure an EC2 instance via your prefered channels. In this instance it was done using Boto3 as a once off configuration, with no intent to automate the process.

You'd need to edit the following with the name of your aws key:
key_name = 'awsautomation'



