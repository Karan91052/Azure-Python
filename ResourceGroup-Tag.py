import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Set the environment variables with your Azure credentials
os.environ["AZURE_CLIENT_ID"] = "cd51b742-dfda-470b-8f10-1fdf59ec271b"
os.environ["AZURE_TENANT_ID"] = "fb9886a0-c37e-4427-82a5-a40305272af6"
os.environ["AZURE_CLIENT_SECRET"] = "1Ih8Q~pnEJsTrHKVwswid1h3N5b.vVAVx6HJza5o"

# Replace with your Azure subscription ID
subscription_id = 'bfa711a5-2a46-4ae9-b13f-cfc3648d8f94'

# Authenticate using your Azure credentials from environment variables
credential = DefaultAzureCredential()

# Create the resource management client
resource_client = ResourceManagementClient(credential, subscription_id)

# Fetch a list of all resource groups
resource_groups = resource_client.resource_groups.list()

# Iterate through the resource groups
for resource_group in resource_groups:
    # Get the name of the resource group
    resource_group_name = resource_group.name
    print(f'Tags for resource group {resource_group_name}:')
    # Fetch the tags for the resource group
    tags = resource_group.tags
    print(tags)
