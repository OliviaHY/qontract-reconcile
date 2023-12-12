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


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class ResourceRequestsRequirementsV1(ConfiguredBaseModel):
    cpu: str = Field(..., alias="cpu")
    memory: str = Field(..., alias="memory")


class ResourceLimitsRequirementsV1(ConfiguredBaseModel):
    cpu: Optional[str] = Field(..., alias="cpu")
    memory: str = Field(..., alias="memory")


class DeployResourcesFields(ConfiguredBaseModel):
    requests: ResourceRequestsRequirementsV1 = Field(..., alias="requests")
    limits: ResourceLimitsRequirementsV1 = Field(..., alias="limits")
