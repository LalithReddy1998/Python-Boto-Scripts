# crearing a function

if __name__ == "__main__":

# create credentials

	from azure.common.credentials import ServicePrincipalCredentials
	from azure.mgmt.resource import ResourceManagementClient
	from azure.mgmt.compute import ComputeManagementClient
	from azure.mgmt.network import NetworkManagementClient
	from azure.mgmt.compute.models import DiskCreateOption


	sub-id = 'subscription-id'
	group-name = 'Lalith'
	location = 'westus'
	VM-name = 'lalith_vm'





	def get_credentials():
		credentials = ServicePrincipalCredentials(
        		client_id = "application-id",
        		secret = "authentication-key",
        		tenant = "tenant-id"
    		)

    		return credentials


# calling function


credentials = get_credentials()


# create resources

resource_group_client = ResourceManagementClient(
    credentials,
    sub-id
)
network_client = NetworkManagementClient(
    credentials,
    sub-id
)
compute_client = ComputeManagementClient(
    credentials,
    sub-id
)


# create vm

def create_resource_group(resource_group_client):
    resource_group_params = { "location":LOCATION }
    resource_group_result = resource_group_client.resource_groups.create_or_update(
        group-name, 
        resource_group_params
    )

create_resource_group(resource_group_client)
input("resource group created. press enter to continue ")


# resize vm


 def update_vm(compute_client):
    vm = compute_client.virtual_machines.get(group-name, VM-name)
    vm.hardware_profile.vm_size = 'Standard_DS3'
    update_result = compute_client.virtual_machines.create_or_update(
        group-name, 
        VM-name, 
        vm
    )

return update_result.result()
