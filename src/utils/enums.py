from enum import Enum


class Source(Enum):
    FN9 = "fn9"
    MGP = "mgp"
    RCR = "rcr"


class Schema(Enum):
    SILVER = "silver"
    GOLD = "gold"


class Table(Enum):
    FRCTRC = "FRCTRC"
    CPTIT = "CPTIT"
    FACTRC = "FACTRC"
    TBCID = "TBCID"
    TBCLI = "TBCLI"
    TBFIL = "TBFIL"
    TBFOR = "TBFOR"
    TBHIS = "TBHIS"
    TBPRO = "TBPRO"
    TBCTA = "TBCTA"
