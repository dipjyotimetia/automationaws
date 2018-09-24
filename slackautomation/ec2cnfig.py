# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonautomation')
ec2 = session.resource('ec2')
key_name = 'awsautomation'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
import os, stat
with open (key_path, 'w') as key_file:
    key_file.write(key.key_material)

os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l awsautomation.pem')
img = ec2.Image('ami-00e17d1165b9dd3ec')
img.name
ami_name = 'amzn2-ami-hvm-2.0.20180810-x86_64-gp2'
filters = [{'Name':'name', 'Values': [ami_name]}]
img
img.id
instances= ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1,InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
# look up the security group
# authorize incoming connections from public ip via ssh
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP', 'IpRanges':[{'CidrIp':'103.108.116.3/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort':80, 'ToPort':80, 'IpProtocol':'TCP', 'IpRanges':[{'0.0.0.0/0'}]}])
