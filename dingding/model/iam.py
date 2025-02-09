from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from dingding.model.entity import AccountId
from dingding.model.entity import StaffId
from dingding.model.entity import TenantId
from dingding.model.entity import UserId


class BindDingdingUserInput(BaseModel):
    staff_id: StaffId = Field(description='人员id')
    tenant_id: TenantId = Field(description='租户id')
    dingding_id: UserId = Field(description='钉钉人员id')
    name: Optional[str] = Field(description='钉钉人员名称')


class DingDingUserAccount(BaseModel):
    tenant_id: TenantId
    account_id: AccountId
    dingding_id: UserId
    name: Optional[str]
