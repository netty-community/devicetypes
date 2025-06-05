
from pydantic import BaseModel

from .interface_type import Interface
from .platform import Platform
from .product_family import ProductFamily


class DeviceType(BaseModel):
    name: str
    abbreviation: str
    platform: Platform
    product_family: ProductFamily
    poe_supported: bool
    rated_power: int
    max_power: int
    interfaces: list[Interface]
    management_interface: Interface
    stack_interfaces: list[Interface]

    uplink_interfaces: list[Interface]
    fallback_uplink_interfaces: list[Interface]
    downlink_interfaces: list[Interface]



