"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


DEFINITION = """
fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query CloudflareAccountRole {
  cloudflare_account_roles:	cloudflare_account_role_v1 {
    name
    roles
    access_roles {
      users {
        cloudflare_user
        org_username
      }
    }
    account {
      name
      providerVersion
      apiCredentials {
        ... VaultSecret
      }
      terraformStateAccount {
        name
        automationToken {
          ... VaultSecret
        }
        terraformState {
          provider
          bucket
          region
          integrations {
            integration
            key
          }
        }
      }
      enforceTwofactor
      type
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class UserV1(ConfiguredBaseModel):
    cloudflare_user: Optional[str] = Field(..., alias="cloudflare_user")
    org_username: str = Field(..., alias="org_username")


class RoleV1(ConfiguredBaseModel):
    users: list[UserV1] = Field(..., alias="users")


class AWSTerraformStateIntegrationsV1(ConfiguredBaseModel):
    integration: str = Field(..., alias="integration")
    key: str = Field(..., alias="key")


class TerraformStateAWSV1(ConfiguredBaseModel):
    provider: str = Field(..., alias="provider")
    bucket: str = Field(..., alias="bucket")
    region: str = Field(..., alias="region")
    integrations: list[AWSTerraformStateIntegrationsV1] = Field(..., alias="integrations")


class AWSAccountV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    automation_token: VaultSecret = Field(..., alias="automationToken")
    terraform_state: Optional[TerraformStateAWSV1] = Field(..., alias="terraformState")


class CloudflareAccountV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    provider_version: str = Field(..., alias="providerVersion")
    api_credentials: VaultSecret = Field(..., alias="apiCredentials")
    terraform_state_account: AWSAccountV1 = Field(..., alias="terraformStateAccount")
    enforce_twofactor: Optional[bool] = Field(..., alias="enforceTwofactor")
    q_type: Optional[str] = Field(..., alias="type")


class CloudflareAccountRoleV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    roles: list[str] = Field(..., alias="roles")
    access_roles: Optional[list[RoleV1]] = Field(..., alias="access_roles")
    account: CloudflareAccountV1 = Field(..., alias="account")


class CloudflareAccountRoleQueryData(ConfiguredBaseModel):
    cloudflare_account_roles: Optional[list[CloudflareAccountRoleV1]] = Field(..., alias="cloudflare_account_roles")


def query(query_func: Callable, **kwargs: Any) -> CloudflareAccountRoleQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        CloudflareAccountRoleQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return CloudflareAccountRoleQueryData(**raw_data)
