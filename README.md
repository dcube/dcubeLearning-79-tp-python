## Authentification Azure

az login
az account set --subscription "dcube - development"

## Add user policy to key vault

USER_ID=$(az ad user show --id nicolas.bailly@dcube.fr --query id -o tsv)
az keyvault set-policy --name kv-learning-dev-01 --object-id $USER_ID --secret-permissions GET
