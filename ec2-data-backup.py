### VOLUMES ARE AWS STORAGE COMPONENTS = STORES EC2 INSTANCE DATA ,,, ### VOLUME SNAPSHOT >> COPY OF VOLUME, FOR DATA BACKUP OR RECOVERY.
### PROJECT DATA BACKUP, AUTOMATING DATA BACKUP OF EC2 INSTANCES 

import boto3 
import schedule

ec2_client = boto3.client('ec2' , region_name="eu-central-1")

def create_volume_snapshots():
   volumes = ec2_client.describe_volumes(
       Filters=[
           {
               'Name': 'tag:Name',
               'Values': ['prod']
           }
       ]
   )
   for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
        VolumeId=volume['VolumeId']
    )
        print(new_snapshot)
        
schedule.every(20).seconds.do('create_volume_snapshot')

while True: 
    schedule.run_pending()
 