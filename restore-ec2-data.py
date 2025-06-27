#### PROJECT OVERVIEW >>> NEW VOLUME CREARTION WITH SNAPSHOT 

import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name='eu-central-1')
ec2_resource = boto3.resource('ec2', region_name='eu-central-1')

instance_id = "i-094783y634yhrhy11" ### we write instance id from aws thats just random.

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment-instance-id',
            'Values': [instance_id]
        }
    ]
)

instance_volume = volumes['Volumes'][0]


snapshots = ec2_client.describe_volumes(
    OwnerIds=['self'],
    Filters=[
        {
               'Name': 'volume-id',
               'Values': [instance_volume['VolumeId']]
        }
    ]
)

latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]
print(latest_snapshot['StartTime'])

new_volume = ec2_client.create_volume(
    SnapshotId=latest_snapshot['SnapshotId'],
    AvailabilityZone="eu-central-1",
    TagsSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'prod'
                }
            ]
        }
    ]
)


### SNAPSHOTS VOLUME IS ATTACHED TO THE INSTANCE 
while True: 
    vol = ec2_resource.Volume(new_volume['VolumeId'])
    print(vol.state)
    if vol.state == 'available':
        ec2_resource.Instance(instance_id).attach_volume(
            VolumeId=new_volume['Volume_Id'],
            Device='/dev/xvda'
        )
        break
