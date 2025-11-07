# TASK 7 - Blob Storage Challenge in the Neighborhood
Difficulty: ❄️

[Direct Link](https://hhc25-wetty-prod.holidayhackchallenge.com/?&challenge=termMSBlobstorage)

## OBJECTIVE : ##
>Help the Goose Grace near the pond find which Azure Storage account has been misconfigured to allow public blob access by analyzing the export file.

## HINTS: ##
<details>
  <summary>Hints provided for Task 7</summary>
  
>-	This terminal has built-in hints!

</details>
 
#  

## PROCEDURE : ##

You may not know this but the Azure cli help messages are very easy to access. First, try typing:
`$ az help | less`

Next, you've already been configured with credentials. 🔑
  `$ az account show | less`
  - Pipe the output to `| less` so you can scroll.
  - Press `q` to exit less.

```
$ az account show | less
{
  "environmentName": "AzureCloud",
  "id": "2b0942f3-9bca-484b-a508-abdae2db5e64",
  "isDefault": true,
  "name": "theneighborhood-sub",
  "state": "Enabled",
  "tenantId": "90a38eda-4006-4dd5-924c-6ca55cacc14d",
  "user": {
    "name": "theneighborhood@theneighborhood.invalid",
    "type": "user"
  }
}
(END)
```
Now that you've run a few commands, Let's take a look at some Azure storage accounts.
Try: `az storage account list | less`
For more information:
[https://learn.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest](https://learn.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest)

Running th esuggested command we can see that one of the returned accounts has `"allowBlobPublicAccess":true`

```
$ az storage account list | less

  {
    "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/theneighborhood-rg1/providers/Microsoft.Storage/storageAccounts/neighborhood2",
    "kind": "StorageV2",
    "location": "eastus2",
    "name": "neighborhood2",
    "properties": {
      "accessTier": "Cool",
      "allowBlobPublicAccess": true,
      "encryption": {
        "keySource": "Microsoft.Storage",
        "services": {
          "blob": {
            "enabled": false
          }
        }
      },
      "minimumTlsVersion": "TLS1_0"
    },
    "resourceGroup": "theneighborhood-rg1",
    "sku": {
      "name": "Standard_GRS"
    },
    "tags": {
      "owner": "Admin"
    }
  },
```

hmm... one of these looks suspicious 🚨, i think there may be a misconfiguration here somewhere.
Try showing the account that has a common misconfiguration: az storage account show --name xxxxxxxxxx | less

```
$ az storage account show --name neighborhood2 | less
{
  "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/theneighborhood-rg1/providers/Microsoft.Storage/storageAccounts/neighborhood2",
  "name": "neighborhood2",
  "location": "eastus2",
  "kind": "StorageV2",
  "sku": {
    "name": "Standard_GRS"
  },
  "properties": {
    "accessTier": "Cool",
    "allowBlobPublicAccess": true,
    "minimumTlsVersion": "TLS1_0",
    "encryption": {
      "services": {
        "blob": {
          "enabled": false
        }
      },
      "keySource": "Microsoft.Storage"
    }
  },
  "resourceGroup": "theneighborhood-rg1",
  "tags": {
    "owner": "Admin"
  }
}
```

Now we need to list containers in neighborhood2. After running the command what's interesting in the list?
For more information:
[https://learn.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest#az-storage-container-list](https://learn.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest#az-storage-container-list)

```
neighbor@04a904c9cbbd:~$ az storage container list --account-name neighborhood2
[
  {
    "name": "public",
    "properties": {
      "lastModified": "2024-01-15T09:00:00Z",
      "publicAccess": "Blob"
    }
  },
  {
    "name": "private",
    "properties": {
      "lastModified": "2024-02-05T11:12:00Z",
      "publicAccess": null
    }
  }
]
```

Let's take a look at the blob list in the public container for neighborhood2.
For more information:
[https://learn.microsoft.com/en-us/cli/azure/storage/blob?view=azure-cli-latest#az-storage-blob-list](https://learn.microsoft.com/en-us/cli/azure/storage/blob?view=azure-cli-latest#az-storage-blob-list)

```
neighbor@04a904c9cbbd:~$ az storage blob list --container-name public --account-name neighborhood2
[
  {
    "name": "refrigerator_inventory.pdf",
    "properties": {
      "contentLength": 45678,
      "contentType": "application/pdf",
      "metadata": {
        "created_by": "NeighborhoodWatch",
        "document_type": "inventory",
        "last_updated": "2024-12-15"
      }
    }
  },
  {
    "name": "admin_credentials.txt",
    "properties": {
      "contentLength": 1024,
      "contentType": "text/plain",
      "metadata": {
        "note": "admins only"
      }
    }
  },
  {
    "name": "network_config.json",
    "properties": {
      "contentLength": 2048,
      "contentType": "application/json",
      "metadata": {
        "encrypted": "false",
        "environment": "prod"
      }
    }
  }
]
```

Try downloading and viewing the blob file named admin_credentials.txt from the public container.
💡 hint: --file /dev/stdout should print in the terminal. Dont forget to use | less!

```
$ az storage blob download --container-name public --account-name neighborhood2 --name admin_credentials.txt --file /dev/stdout | less
# You have discovered an Azure Storage account with "allowBlobPublicAccess": true.
# This misconfiguration allows ANYONE on the internet to view and download files
# from the blob container without authentication.

# Public blob access is highly insecure when sensitive data (like admin credentials)
# is stored in these containers. Always disable public access unless absolutely required.

Azure Portal Credentials
User: azureadmin
Pass: AzUR3!P@ssw0rd#2025

Windows Server Credentials
User: administrator
Pass: W1nD0ws$Srv!@42

SQL Server Credentials
User: sa
Pass: SqL!P@55#2025$

Active Directory Domain Admin
User: corp\administrator
Pass: D0m@in#Adm!n$765

Exchange Admin Credentials
User: exchangeadmin
```
🎊 Great, you found the misconfiguration allowing public access to sensitive information!

✅ Challenge Complete! To finish, type: finish



