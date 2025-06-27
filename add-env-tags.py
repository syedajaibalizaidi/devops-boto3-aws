###FOR THIS PROJECT WE HAVE A SCENERIO, LETS SUPPOSE WE HAVE 20 SERVERS ALLOCATED FOR PRODUCTION IN FRANKFURT REIGON AND 
### 10 SERVERS ALLOCATED FOR DEV IN PARIS REIGON , SO WOULD BE TIDIOUS TO SET THE TAGS ONE BY ONE 
### SO WE WILL AUTOMATE THIS TAG PROCESS WITH PYTHON SCRIPT 

import boto3 

ec2_client_frankfurt = boto3.client('ec2' , region_name='eu-central-1')
ec2_resource_frankfurt = boto3.resource('ec2', region_name='eu-central-1')

ec2_client_paris = boto3.client('ec2' , region_name='eu-west-3')
ec2_resource_paris = boto3.resource('ec2', region_name='eu-west-3')

instances_ids_frankfurt = []
instances_ids_paris = []

reservations_frankfurt = ec2_client_frankfurt.describe_instances()['Reservation']
for reservation in reservations_frankfurt:
    instances = reservation['instances']
    for instance in instances:
        instances_ids_frankfurt.append(instance['InstanceId'])
        

response = ec2_resource_frankfurt.create_tags(
    Resources=instances_ids_frankfurt,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)


reservations_paris = ec2_client_paris.describe_instances()['Reservation']
for reservation in reservations_paris:
    instances = reservation['instances']
    for instance in instances:
        instances_ids_paris.append(instance['InstanceId'])
        

response = ec2_resource_paris.create_tags(
    Resources=instances_ids_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)