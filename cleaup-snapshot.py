### PROJECT >>> AUTOMATING THE CLEAN UP BACKUP SNAPSHOT PROCESS ,,, CODE THAT CLEANS ALL OLD SNAPSHOTS AND KEEPS THE RECENT TWO.
### IF SCHEDULER RUNS EVERYDAY WE WILL END UP WITH LOTS OF VOLUME SNAPSHOTS WHICH WILL INCREASE THE BILL SIGNIFICANTLY.

import boto3 
from operator import itemgetter ### itemgetter is the function of module operator.

### Creating ec2 client for our region
ec2_client = boto3.client('ec2' , region_name='eu-central-1')


volumes = ec2_client.describe_volumes(
    Filters=[
        {
               'Name': 'tag:Name',
               'Values': ['prod']
        }
    ]
)


for volume in volumes['Volumes']:
### Fetching our snapshots 
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
               'Name': 'volume-id',
               'Values': [volume['VolumeId']]
            }
        ]
    )

### Sorting of the snapshot list by startTime in descending order so that we have the most recent snapshots on top and remaining at bottom to delete them.
    sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

### Code for deleting all snapshots starting from 3rd item.
    for snapshot in sorted_by_date[2:]:
        response = ec2_client.delete_snapshot(
        SnapshotId=snapshot['SnapshotId']
    )
        print(response)


