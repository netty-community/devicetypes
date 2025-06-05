from enum import Enum, StrEnum


class FiberModuleType(Enum):
    """ISO 11801"""

    SFP = ("sfp", "1Gps", "LC", "常见1Gbps接口")
    SFP_PLUS = ("sfp+", "10Gps", "LC", "常见10G模块")
    XFP = ("xfp", "10Gps", "LC", "10G模块")
    QSFP_PLUS = ("qsfp+", "40Gps", "MPO", "40G SR4，4通道并行传输")
    QSFP28 = ("qsfp28", "100Gps", "LC/MPO", "100G，MPO（并行）或 LC（串行，CWDM）")
    QSFP_DD = (
        "qsfp-dd",
        "200Gps/400Gps",
        "MPO/CS/SN",
        "200G/400G 高速模块，高密度接口方案",
    )

    def __init__(self, type: str, speed: str, interface: str, description: str):
        self._type = type
        self._speed = speed
        self._interface = interface
        self._description = description
    
    @property
    def type(self) -> str:
        return self._type

    @property
    def speed(self) -> str:
        return self._speed

    @property
    def interface(self) -> str:
        return self._interface

    @property
    def description(self) -> str:
        return self._description

    @classmethod
    def to_views(cls) -> list[dict[str, str]]:
        return [
            {
                "type": member.type,
                "speed": member.speed,
                "interface": member.interface,
                "description": member.description,
            }
            for member in cls
        ]


class FiberClassType(Enum):
    """ISO 11801"""

    OM3 = (
        "OM3",
        "MM",
        "LC",
        "适用于数据中心短距离，激光优化",
        "10G/40G/100G",
        "300m@10G",
    )
    OM4 = ("OM4", "MM", "LC", "比OM3更优，适用于高速以太网", "10G/40G/100G", "550m@10G")
    OM5 = ("OM5", "MM", "LC", "支持短波WDM，未来可扩展性强", "100G+", "150m+")
    OS2 = ("OS2", "SM", "LC", "适用于长距离传输", "10G/100G/400G", "10km~100km")

    def __init__(
        self,
        type: str,
        mode: str,
        interface: str,
        description: str,
        speeds: str,
        distance: str,
    ):
        self._type = type
        self._mode = mode
        self._interface = interface
        self._description = description
        self._speeds = speeds
        self._distance = distance

    @property
    def type(self) -> str:
        return self._type

    @property
    def mode(self) -> str:
        return self._mode

    @property
    def interface(self) -> str:
        return self._interface

    @property
    def description(self) -> str:
        return self._description

    @property
    def speeds(self) -> str:
        return self._speeds

    @property
    def distance(self) -> str:
        return self._distance

    @classmethod
    def to_views(cls) -> list[dict[str, str]]:
        return [
            {
                "type": member.type,
                "mode": member.mode,
                "interface": member.interface,
                "description": member.description,
                "speeds": member.speeds,
                "distance": member.distance,
            }
            for member in cls
        ]


class CopperType(Enum):
    CAT5E = (
        "cat5e",
        "100MHz",
        "1Gbps",
        "100m",
        "PoE+",
        "UTP/STP",
        "基础家用千兆",
        "最常见入门级网线\n无屏蔽\n前兆以太网",
    )
    CAT6 = (
        "cat6",
        "250MHz",
        "10Gbps",
        "10G:55m 1G:100m",
        "PoE++",
        "STP",
        "企业级千兆",
        "千兆标准升级版\n屏蔽性能更强\10G传输距离受限",
    )
    CAT6A = (
        "cat6a",
        "500MHz",
        "10Gbps",
        "10G:55m 1G:100m",
        "PoE++",
        "STP",
        "企业级千/万兆",
        "支持完整100米的10GBASE-T\n带屏蔽，更粗更硬，适合工程布线\n发热更小，稳定支持高功率供电",
    )
    CAT7 = (
        "cat7",
        "600MHz",
        "10Gbps",
        "100m",
        "PoE+",
        "S/FTP",
        "数据中心",
        "强屏蔽（每对线和总线都有）\n价格贵，RJ45 和 GG45 接头混用\n不是正式 TIA/EIA 标准，但常用于高要求环境,不常用",
    )
    CAT8 = (
        "cat8",
        "2000MHz",
        "25 Gbps / 40 Gbps",
        "30m",
        "N/A",
        "S/FTP",
        "数据中心",
        "据中心专用，10/25/40G 高速短距连接, 30米，不常用",
    )

    def __init__(
        self,
        type: str,
        frequency: str,
        speed: str,
        distance: str,
        power: str,
        interface: str,
        use_case: str,
        description: str,
    ):
        self._type = type
        self._frequency = frequency
        self._speed = speed
        self._distance = distance
        self._power = power
        self._interface = interface
        self.use_case = use_case
        self._description = description

    @property
    def type(self) -> str:
        return self._type

    @property
    def frequency(self) -> str:
        return self._frequency

    @property
    def speed(self) -> str:
        return self._speed

    @property
    def distance(self) -> str:
        return self._distance

    @property
    def power(self) -> str:
        return self._power

    @property
    def interface(self) -> str:
        return self._interface

    @property
    def description(self) -> str:
        return self._description

    @classmethod
    def to_views(cls) -> list[dict[str, str]]:
        return [
            {
                "type": member.type,
                "frequency": member.frequency,
                "speed": member.speed,
                "distance": member.distance,
                "power": member.power,
                "interface": member.interface,
                "use_case": member.use_case,
                "description": member.description,
            }
            for member in cls
        ]

class CableType(StrEnum):
    MM_FIBER_1G = "mm_fiber_1g"
    MM_FIBER_10G = "mm_fiber_10g"
    MM_FIBER_25G = "mm_fiber_25g"
    MM_FIBER_40G = "mm_fiber_40g"
    MM_FIBER_100G = "mm_fiber_100g"
    SM_FIBER_1G = "sm_fiber_1g"
    SM_FIBER_10G = "sm_fiber_10g"
    SM_FIBER_25G = "sm_fiber_25g"
    SM_FIBER_40G = "sm_fiber_40g"
    SM_FIBER_100G = "sm_fiber_100g"
    