from enum import Enum


class Source(Enum):
    FN9 = "fn9"
    MGP = "mgp"
    RCR = "rcr"


class Table(Enum):
    FRCTRC = "frctrc"
    CPTIT = "cptit"
    FACTRC = "factrc"
    TBCID = "tbcid"
    TBCLI = "tbcli"
    TBFIL = "tbfil"
    TBFOR = "tbfor"
    TBHIS = "tbhis"
    TBPRO = "tbpro"
    TBCTA = "tbcta"
