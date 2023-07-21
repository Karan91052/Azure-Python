import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
# Replace with your Azure subscription ID
subscription_id = 'bfa711a5-2a46-4ae9-b13f-cfc3648d8f94'
# Set the environment variables with your Azure credentials
os.environ["AZURE_CLIENT_ID"] = "cd51b742-dfda-470b-8f10-1fdf59ec271b"
os.environ["AZURE_TENANT_ID"] = "fb9886a0-c37e-4427-82a5-a40305272af6"
os.environ["AZURE_CLIENT_SECRET"] = "1Ih8Q~pnEJsTrHKVwswid1h3N5b.vVAVx6HJza5o"
# Authenticate using your Azure credentials
credential = DefaultAzureCredential()
# Create the resource management client
resource_client = ResourceManagementClient(credential, subscription_id)
# Fetch a list of all resource groups
resource_groups = resource_client.resource_groups.list()
# Iterate through the resource groups
for resource_group in resource_groups:
    # Get the name of the resource group
    resource_group_name = resource_group.name
    print(f'resource group name {resource_group_name}:')

    # fetch the resource 
    resources_name=resource_client.resources.list_by_resource_group(resource_group_name)
    #iterate through the resources
    for resources_name in resources_name:
        res_name=resources_name.name
        print(f'fetch the resources {res_name}')
# Fetch the tags for the resource group
    tags = resource_group.tags
        # Print the tags
    print(f'Tags for resource group {tags}:')