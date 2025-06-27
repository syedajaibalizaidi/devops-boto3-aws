import boto3 

ec2_client = boto3.client('ec2' , reigon_name="eu-west-3")
ec2-resource = boto3.resource('ec2' , reigon_name="eu-west-3")

### for checking the state of instances either they running terminated shutdown initializing..,commented out it bcz below we can sum up this in a line this only for reservation understanding.
# reservations = ec2_client.describe_instances()
# for reservation in reservations['Reservations']:
#     instances = reservation['instances']
#     for instance in instances:
#         print(f"Instance {instance['InstanceId']} is {instance['State'], ['Name']}")
        
### for checking the status of the ec2 instances , done with the help of boto3 documentation 
statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStauses']:
    ins_status = status['InstanceStatus']['Status']
    sys_status = status['SystemStatus']['Status'] 
    state = status['InstanceState']['Name']
    print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")