# Slackbot for AWS EC2 instances


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
``` 
$ brew install pipenv
``` 
The make a new project directory and launch your virtual environment using the following
``` 
pipenv --three (Python version 3)
pipenv --two (Python version 2)
 ``` 
Then install boto3 (AWS SDK and you can configure your EC2 instance using this) and iPython (Juypiter Notebooks for your command line)
``` 
pipenv install boto3
pipenv install -d ipython 
 ```
 '-d' indicates dev environment
 
 ### iPython
 I used iPython as it immediately validates your code, so you can fix things quicker and best for learning. 
 [iPython](https://ipython.org/) website has more info....and to run iPython in your pipenv...

```pipenv run ipython
```


### EC2/Security Group Configuration and Creation (Optional - Exploring the use of boto3)
You can just configure an EC2 instance via your prefered channels. In this instance it was done using Boto3 as a once off configuration, with no intent to automate the process. This boto3 code also sets the security group policy to allow ssh and http (in this instance it's to my specific IP).

[Here's the code] (https://github.com/francalovescakes/automationaws/blob/master/slackautomation/ec2cnfig.py)

You'd need to edit the following with the name of your aws key:
``` 
key_name = 'awsautomation'
``` 

The following lines get the AMI id, which you'll need to do if you intend to launch an instance in more than one Region:
``` 
img = ec2.Image('ami-00e17d1165b9dd3ec')
img.name #shows the image id to be used
ami_name = 'amzn2-ami-hvm-2.0.20180810-x86_64-gp2' 
 ``` 
My example is just a linux AMI t2.micro, so you'd need to update this you require another instance.


### Auto Scaling Groups in AWS
Set up a simple ASG based on CPU Utilization - scale up and scale down policy. You can execute these policies via the console or using boto3.

#### Examples of scale up and scale down policies to execute using boto3 (Towards the end I had issues with Python versions and ended up executing via the console to test that my slack function worked):
- [scale up] (https://github.com/francalovescakes/automationaws/blob/master/slackautomation/scaleup.py) 
- [scale down] (https://github.com/francalovescakes/automationaws/blob/master/slackautomation/scaledown.py)

You'll need to ensure your instance can serve web traffic (to be able to integrate with a Webhook later) - sudo yum update and install httpd or your prefered web server.


### Lambda
Create a new lambda from scratch. The lambda function it'self is to post a notification to Slack via a Webhook as per [handler.py](https://github.com/francalovescakes/automationaws/blob/master/slackautomation/notifier/handler.py) 

### Rules
Create a rule via the console under Cloudwatch Management and attached it as a trigger to Lambda. The rule is based on a successful launch.

### Serverless
Serverless allows you to build and deploy serverless applications. Includes a fully managed service including autoscaling. Their website is a good resource for more information: [Serverless.com](https://serverless.com/)
- To install
``` 
npm install -g serverless
```
- To create a template
``` 
serverless create --template aws-python3 --name slacknotification
```
- To deploy a stack
```
sls deploy
```
You get two files from this inlcuding [serverless.yaml](https://github.com/francalovescakes/automationaws/blob/master/slackautomation/notifier/serverless.yml) (serverless config file) and [handler.py](https://github.com/francalovescakes/automationaws/blob/master/slackautomation/notifier/handler.py)

