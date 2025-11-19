# TASK 9 - The Open Door
Difficulty: ❄️

[Direct Link](https://hhc25-wetty-prod.holidayhackchallenge.com/?&challenge=termMSOpenDoor)

## OBJECTIVE : ##
>Help Goose Lucas in the hotel parking lot find the dangerously misconfigured Network Security Group rule that's allowing unrestricted internet access to sensitive ports like RDP or SSH.


## HINTS: ##
<details>
  <summary>Hints provided for Task 9</summary>
  
>-	This terminal has built-in hints!

</details>
 
#  

## PROCEDURE : ##

🎄 Welcome to The Open Door Challenge! 🎄
You're connected to a read-only Azure CLI session in "The Neighborhood" tenant.
Your mission: Review their network configurations and find what doesn't belong.
Connecting you now... ❄️

Welcome back! Let's start by exploring output formats.
First, let's see resource groups in JSON format (the default):
`$ az group list`
JSON format shows detailed structured data.

```
$ az group list
[
  {
    "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/theneighborhood-rg1",
    "location": "eastus",
    "managedBy": null,
    "name": "theneighborhood-rg1",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": {}
  },
  {
    "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/theneighborhood-rg2",
    "location": "westus",
    "managedBy": null,
    "name": "theneighborhood-rg2",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": {}
  }
]
```

Great! Now let's see the same data in table format for better readability 👀
`$ az group list -o table`
Notice how -o table changes the output format completely! Both commands show the same data, just formatted differently.

```
$ az group list -o table
Name                 Location    ProvisioningState
-------------------  ----------  -------------------
theneighborhood-rg1  eastus      Succeeded
theneighborhood-rg2  westus      Succeeded
```

Lets take a look at Network Security Groups (NSGs).
To do this try: `az network nsg list -o table`
This lists all NSGs across resource groups.
For more information:[https://learn.microsoft.com/en-us/cli/azure/network/nsg?view=azure-cli-latest](https://learn.microsoft.com/en-us/cli/azure/network/nsg?view=azure-cli-latest)

```
$ az network nsg list -o table
Location    Name                   ResourceGroup
----------  ---------------------  -------------------
eastus      nsg-web-eastus         theneighborhood-rg1
eastus      nsg-db-eastus          theneighborhood-rg1
eastus      nsg-dev-eastus         theneighborhood-rg2
eastus      nsg-mgmt-eastus        theneighborhood-rg2
eastus      nsg-production-eastus  theneighborhood-rg1
```

Inspect the Network Security Group (web)  🕵️
Here is the NSG and its resource group:`--name nsg-web-eastus` `--resource-group theneighborhood-rg1` 

Hint: We want to `show` the NSG details. Use `| less` to page through the output.
Documentation: [https://learn.microsoft.com/en-us/cli/azure/network/nsg?view=azure-cli-latest#az-network-nsg-show](https://learn.microsoft.com/en-us/cli/azure/network/nsg?view=azure-cli-latest#az-network-nsg-show)

```
$ az network nsg show --name nsg-web-eastus --resource-group theneighborhood-rg1 -o table
Name            ResourceGroup        Location    Tags     ProvisioningState
--------------  -------------------  ----------  -------  -------------------
nsg-web-eastus  theneighborhood-rg1  eastus      env=web  Succeeded
```

Inspect the Network Security Group (mgmt)  🕵️
Here is the NSG and its resource group:`--nsg-name nsg-mgmt-eastus` `--resource-group theneighborhood-rg2` 

Hint: We want to `list` the NSG rules
Documentation: [https://learn.microsoft.com/en-us/cli/azure/network/nsg/rule?view=azure-cli-latest#az-network-nsg-rule-list](https://learn.microsoft.com/en-us/cli/azure/network/nsg/rule?view=azure-cli-latest#az-network-nsg-rule-list)

```
$ az network nsg rule list --nsg-name nsg-mgmt-eastus --resource-group theneighborhood-rg2 -o table
Access    Direction    Name                        Priority    Protocol    NSG              SourceAddressPrefix    SourcePortRange    DestinationAddressPrefix    DestinationPortRange
--------  -----------  --------------------------  ----------  ----------  ---------------  ---------------------  -----------------  --------------------------  ----------------------
Allow     Inbound      Allow-AzureBastion          100         Tcp         nsg-mgmt-eastus  AzureBastion           *                  *                           443
Allow     Inbound      Allow-Monitoring-Inbound    110         Tcp         nsg-mgmt-eastus  AzureMonitor           *                  *                           443
Allow     Inbound      Allow-DNS-From-VNet         115         Udp         nsg-mgmt-eastus  VirtualNetwork         *                  *                           53
Deny      Inbound      Deny-All-Inbound            4096        *           nsg-mgmt-eastus  *                      *                  *                           *
Allow     Outbound     Allow-Monitoring-Outbound   200         Tcp         nsg-mgmt-eastus  *                      *                  AzureMonitor                443
Allow     Outbound     Allow-AD-Identity-Outbound  210         Tcp         nsg-mgmt-eastus  *                      *                  AzureActiveDirectory        443
Allow     Outbound     Allow-Backup-Outbound       220         Tcp         nsg-mgmt-eastus  *                      *                  AzureBackup                 443
```

Take a look at the rest of the NSG rules and examine their properties.
After enumerating the NSG rules, enter the command string to view the suspect rule and inspect its properties.
Hint: `Review` fields such as `direction`, `access`, `protocol`, `source`, `destination` and `port` settings.

Documentation: [https://learn.microsoft.com/en-us/cli/azure/network/nsg/rule?view=azure-cli-latest#az-network-nsg-rule-show](https://learn.microsoft.com/en-us/cli/azure/network/nsg/rule?view=azure-cli-latest#az-network-nsg-rule-show)


After some listing of nsg rule in the different resource groups we come across an entry for allowing RDP over the internet, which generally not a good idea.
```
$ az network nsg rule list --nsg-name nsg-production-eastus --resource-group theneighborhood-rg1 -o table
Access    Direction    Name                           Priority    Protocol    NSG                    SourceAddressPrefix    SourcePortRange    DestinationAddressPrefix    DestinationPortRange
--------  -----------  -----------------------------  ----------  ----------  ---------------------  ---------------------  -----------------  --------------------------  ----------------------
Allow     Inbound      Allow-HTTP-Inbound             100         Tcp         nsg-production-eastus  0.0.0.0/0              *                  *                           80
Allow     Inbound      Allow-HTTPS-Inbound            110         Tcp         nsg-production-eastus  0.0.0.0/0              *                  *                           443
Allow     Inbound      Allow-AppGateway-HealthProbes  115         Tcp         nsg-production-eastus  AzureLoadBalancer      *                  *                           80,443
Allow     Inbound      Allow-RDP-From-Internet        120         Tcp         nsg-production-eastus  0.0.0.0/0              *                  *                           3389
Deny      Inbound      Deny-All-Inbound               4096        *           nsg-production-eastus  *                      *                  *                           *


$ az network nsg rule show --nsg-name nsg-production-eastus --resource-group theneighborhood-rg1 --name Allow-RDP-From-Internet -o table
Name                     Priority    Access    Direction    Protocol    SourceAddressPrefix    SourcePortRange    DestinationAddressPrefix    DestinationPortRange    ProvisioningState
-----------------------  ----------  --------  -----------  ----------  ---------------------  -----------------  --------------------------  ----------------------  -------------------
Allow-RDP-From-Internet  120         Allow     Inbound      Tcp         0.0.0.0/0
```

Great, you found the NSG misconfiguration allowing RDP (port 3389) from the public internet!
Port 3389 is used by Remote Desktop Protocol — exposing it broadly allows attackers to brute-force credentials, exploit RDP vulnerabilities, and pivot within the network.

