### EKS CLUSTER PROJECT >> PYTHON SCRIPT TO CHECK EKS CLUSTER STATUS , K8S VERSION , CLUSTER ENDPOINT 
### STEPS >> 1ST STEP IS TO CREATE EKS CLUSTER WITH TERRAFORM, 2ND STEP IS TO WRITE PYHTON PROGRAM FOR THIS. 
import boto3 
# import schedule ##its not installed locally hence showing error here, so first we need to install then import thsi py library. 

client = boto3.client('eks', region_name="eu-central-1")
clusters = client.list_clusters()['clusters']

for cluster in clusters:
    response = client.describe_cluster(
        name=cluster
    )
    cluster_info = response['cluster'] ##from documentation of boto3 
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']
    
    print(f"Cluster {cluster} status is {cluster_status}")
    print(f"Cluster endpoint is {cluster_endpoint}")
    print(f"Cluster version is {cluster_version}")
    
# schedule.every(5).seconds.do('check_instance_status')

# while True: 
#     schedule.run_pending()