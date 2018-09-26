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

### Prerequisits
- install python 3.6 or 2.7 (to be compatible with Serverless)
- install pipenv (virtual environment)

### Setting up your virtual environment
I used Pipenv ( https://pipenv.readthedocs.io/en/latest/)
``` $ brew install pipenv
``` 
The make a new project directory and launch your virtual environment using the following
``` pipenv --three (Python version 3)
 pipenv --two (Python version 2)
 ``` 
Then install boto3 (AWS SDK and you can configure your EC2 instance using this) and iPython (Juypiter Notebooks for your command line)
``` pipenv install boto3
 pipenv install -d ipython 
 ```
 '-d' indicates dev environment
 
 ### iPython
 I used iPython as it immediately validates your code, so you can fix things quicker and best for learning. 
 [iPython](https://ipython.org/) website has more info....and to run iPython in your pipenv...

```pipenv run ipython
```


### EC2 Configuration (Optional - Exploring the use of boto3)
You can just configure an EC2 instance via your prefered channels. In this instance it was done using Boto3 as a once off configuration, with no intent to automate the process.

#### https://github.com/francalovescakes/automationaws/blob/master/slackautomation/ec2cnfig.py

You'd need to edit the following with the name of your aws key:
``` key_name = 'awsautomation'
``` 

The following lines get the AMI id, which you'll need to do if you intend to launch an instance in more than one Region:
``` img = ec2.Image('ami-00e17d1165b9dd3ec') # t2.micro
 img.name #shows the image id to be used
 ami_name = 'amzn2-ami-hvm-2.0.20180810-x86_64-gp2' 
 ``` 

### Auto Scaling Groups in AWS
Set up a simple ASG based on CPU Utilization - scale up and scale down policy. You can execute these policies via the console or using boto3.

#### Examples of scale up and scale down policies:
- scale up: https://github.com/francalovescakes/automationaws/blob/master/slackautomation/scaleup.py 
- scale down: https://github.com/francalovescakes/automationaws/blob/master/slackautomation/scaledown.py



