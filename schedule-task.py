import boto3
import schedule ##its not installed locally hence showing error here, so first we need to install then import thsi py library. 

ec2_client = boto3.client('ec2', reigon_name='eu-west-3')
ec2_resource = boto3.resource('ec2', reigon_name="eu-west-3")


def check_instance_status(): 
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatus']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['State']['Name']
        print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")
    print("#######################\n")
    
schedule.every(5).seconds.do('check_instance_status')

while True: 
    schedule.run_pending()
    