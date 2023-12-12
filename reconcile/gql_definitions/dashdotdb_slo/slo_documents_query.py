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

query SLODocuments {
  slo_documents: slo_document_v1 {
    name
    namespaces {
      prometheusAccess {
         url
         username {
         ... VaultSecret
         }
         password {
           ... VaultSecret
         }
      }
      namespace {
        name
        app {
          name
        }
        cluster {
          name
          automationToken {
          ... VaultSecret
          }
          prometheusUrl
          spec {
            private
          }
        }
      }
      SLONamespace {
        name
      }
    }
    slos {
      name
      expr
      SLIType
      SLOParameters {
        window
      }
      SLOTarget
      SLOTargetUnit
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class SLOExternalPrometheusAccessV1(ConfiguredBaseModel):
    url: str = Field(..., alias="url")
    username: VaultSecret = Field(..., alias="username")
    password: VaultSecret = Field(..., alias="password")


class AppV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class ClusterSpecV1(ConfiguredBaseModel):
    private: bool = Field(..., alias="private")


class ClusterV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    automation_token: Optional[VaultSecret] = Field(..., alias="automationToken")
    prometheus_url: str = Field(..., alias="prometheusUrl")
    spec: Optional[ClusterSpecV1] = Field(..., alias="spec")


class NamespaceV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    app: AppV1 = Field(..., alias="app")
    cluster: ClusterV1 = Field(..., alias="cluster")


class SLONamespacesV1_NamespaceV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class SLONamespacesV1(ConfiguredBaseModel):
    prometheus_access: Optional[SLOExternalPrometheusAccessV1] = Field(..., alias="prometheusAccess")
    namespace: NamespaceV1 = Field(..., alias="namespace")
    slo_namespace: Optional[SLONamespacesV1_NamespaceV1] = Field(..., alias="SLONamespace")


class SLODocumentSLOSLOParametersV1(ConfiguredBaseModel):
    window: str = Field(..., alias="window")


class SLODocumentSLOV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    expr: str = Field(..., alias="expr")
    sli_type: str = Field(..., alias="SLIType")
    slo_parameters: SLODocumentSLOSLOParametersV1 = Field(..., alias="SLOParameters")
    slo_target: float = Field(..., alias="SLOTarget")
    slo_target_unit: str = Field(..., alias="SLOTargetUnit")


class SLODocumentV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    namespaces: list[SLONamespacesV1] = Field(..., alias="namespaces")
    slos: Optional[list[SLODocumentSLOV1]] = Field(..., alias="slos")


class SLODocumentsQueryData(ConfiguredBaseModel):
    slo_documents: Optional[list[SLODocumentV1]] = Field(..., alias="slo_documents")


def query(query_func: Callable, **kwargs: Any) -> SLODocumentsQueryData:
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
        SLODocumentsQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return SLODocumentsQueryData(**raw_data)
