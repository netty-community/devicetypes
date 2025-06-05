from enum import StrEnum


class ProductFamily(StrEnum):
    SWITCH = "switch"
    ROUTER = "router"
    FIREWALL = "firewall"
    WLC = "wlc"
    AP = "ap"
