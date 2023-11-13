""" ** """

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.keyvault.secrets._models import KeyVaultSecret


class KeyVault:
    """ Class to manage Key Vault """

    def __init__(self, key_vault_name: str):
        self._key_vault_name = key_vault_name

    def get_secret(self, secret_name: str) -> str:
        """ Get secret value """

        credential = DefaultAzureCredential()
        with SecretClient(vault_url=f"https://{self._key_vault_name}.vault.azure.net/", credential=credential) as secret_client:
            secret_password: KeyVaultSecret = secret_client.get_secret(secret_name)  # type: ignore
            if secret_password.value is None or secret_password.value == "":  # type: ignore
                raise ValueError("Snowflake password is missing")
            return secret_password.value  # type: ignore
