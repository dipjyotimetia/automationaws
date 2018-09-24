# PipEnv and Boto3 README

##### Pipenv https://pipenv.readthedocs.io/en/latest/

mkdir filename

cd filename

pipenv --three

pipenv install boto3

pipenv install -d ipython # '-d' indicates dev environment

# Pipfile contains the dependencies
#   - Eg boto3, ipython, os, stat

pipenv run ipython




# Boto3

#### https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

# Session is to run the aws configuration that was set and specify the profile

# Resource is a amazon resource for example:

s3 = session.resource(‘s3’)

for bucket in s3.buckets.all():
	print(bucket)

# Methods are the functions you’re calling:
	# delete_bucket()
	# create_bucket()

# Parameters are placed as part of the function (method) and is usually capitalised:

	create_bucket(Bucket=‘[bucket name here]’, CreateBucketConfiguration={‘LocationConstraint’:’as-south-2’})


# Serverless

serverless create --template aws-python3 --name slacknotification

sls deply #deploy a stack

sls invoke -f hello #invoke a function

sls logs -f hello #check the logs 
