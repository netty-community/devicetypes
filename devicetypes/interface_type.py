from enum import StrEnum

from pydantic import BaseModel

class InterfaceType(StrEnum):
    base_100_tx = "100base-tx"
    base_1000_t = "1000base-t"
    base_2dot5g_t = "2.5gbase-t"
    base_5g_t = "5gbase-t"
    base_10g_t = "10gbase-t"
    base_1000_x_sfp = "1000base-x-sfp"
    base_10g_x_sfpp = "10gbase-x-sfpp"
    base_10g_x_xfp = "10gbase-x-xfp"
    base_25g_x_sfp28 = "25gbase-x-sfp28"
    base_40g_x_qsfpp = "40gbase-x-qsfpp"
    base_100g_x_qspf28 = "100gbase-x-qsfp28"
    base_100g_x_cxp = "100gbase-x-cxp"
    base_200g_x_qsfp56 = "200gbase-x-qsfp56"
    base_200g_x_qsfpdd = "200gbase-x-qsfpdd"
    base_400g_x_qsfpdd = "400gbase-x-qsfpdd"
    base_800g_x_qsfpdd = "800gbase-x-qsfpdd"
    base_stack_port = "base-stack-port"


class Interface(BaseModel):
    name: str
    type: InterfaceType
    