from enum import StrEnum

from manufacturer import Manufacturer


class Platform(StrEnum):
    cisco_ios = "cisco_ios"
    cisco_nxos = "cisco_nxos"
    cisco_xr = "cisco_xr"
    cisco_xe = "cisco_xe"
    huawei_vrp = "huawei_vrp"
    huawei_ce = "huawei_ce"
    aruba_os = "aruba_os"
    fortinet = "fortinet"
    juniper_junos = "juniper_junos"
    hp_comware = "hp_comware"
    ruijie_os = "ruijie_os"
    paloalto = "paloalto"

    @property
    def manufacturer(self) -> Manufacturer:
        mapping = {
            Platform.cisco_xe: Manufacturer.CISCO,
            Platform.cisco_nxos: Manufacturer.CISCO,
            Platform.huawei_vrp: Manufacturer.HUAWEI,
            Platform.huawei_ce: Manufacturer.HUAWEI,
            Platform.juniper_junos: Manufacturer.JUNIPER,
            Platform.hp_comware: Manufacturer.H3C,
            Platform.ruijie_os: Manufacturer.RUIJIE,
            Platform.aruba_os: Manufacturer.HPE,
            Platform.fortinet: Manufacturer.FORTINET,
            Platform.paloalto: Manufacturer.PALO_ALTO,
        }
        manufacturer = mapping.get(self)
        if manufacturer is None:
            msg = f"Unknown platform: {self}"
            raise ValueError(msg)
        return manufacturer

    @property
    def netmiko_driver(self) -> str:
        mapping = {
            Platform.cisco_ios: "cisco_ios",
            Platform.cisco_nxos: "cisco_nxos",
            Platform.cisco_xr: "cisco_xr",
            Platform.cisco_xe: "cisco_xe",
            Platform.huawei_vrp: "huawei_vrp",
            Platform.huawei_ce: "huawei_ce",
            Platform.aruba_os: "aruba_os",
            Platform.fortinet: "fortinet",
            Platform.juniper_junos: "juniper_junos",
            Platform.hp_comware: "hp_comware",
            Platform.ruijie_os: "ruijie_os",
            Platform.paloalto: "paloalto",
        }
        driver = mapping.get(self)
        if driver is None:
            msg = f"Unknown platform: {self}"
            raise ValueError(msg)
        return driver

    @property
    def port_channel_prefix(self) -> str:
        mapping = {
            Platform.cisco_ios: "Po",
            Platform.cisco_nxos: "Po",
            Platform.cisco_xr: "Po",
            Platform.cisco_xe: "Po",
            Platform.huawei_vrp: "Eth",
            Platform.huawei_ce: "Eth",
            Platform.aruba_os: "Po",
            Platform.fortinet: "",
            Platform.juniper_junos: "ae",
            Platform.hp_comware: "Eth",
            Platform.ruijie_os: "Agg",
            Platform.paloalto: "AE",
        }
        prefix = mapping.get(self)
        if prefix is None:
            msg = f"Unknown platform: {self}"
            raise ValueError(msg)
        return prefix

    @classmethod
    def to_views(cls) -> list[dict[str, str]]:
        return [
            {
                "platform": member.name,
                "manufacturer": member.manufacturer,
                "netmiko_driver": member.netmiko_driver,
                "port_channel_prefix": member.port_channel_prefix,
            }
            for member in cls
        ]
