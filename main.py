import boto3

ec2_client = boto3.client('ec2' , reigon_name="eu-west-3") ### Name parameters to get or assign a certain value. plus is more low level whereas resource is high level.
ec2_resource = boto3.resource('ec2' , reigon_name="eu-west-3") ## resource is more high level. DONT NEED TO SPECIFY THE VPCID HERE WHEREAS IN CLIENT WE NEED TO SPECIFY THE ID.


new_vpc = ec2_resource.create_vpc(
    CidrBlock = "10.0.0.0/16"
)

all_available_vpcs = ec2_client.describe_vpcs()
vpcs = all_available_vpcs["Vpcs"]

new_vpc.create_subnet(
    CidrBlock ="10.0.1.0/24"
)

new_vpc.create_subnet(
    CidrBlock = "10.0.2.0/24"
)

### in case if we want to name the vpc by reading the documentation we use the keyword of tags for this naming purpose.
new_vpc.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-vpc'
        },
    ]
)

for vpc in vpcs: 
    print(vpc["VpcId"])
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_assoc_sets:
        print(assoc_set["CidrBlockState"]) ## level by level code to get the desired values we want 