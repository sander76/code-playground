from enum import IntEnum

class MyEnum(IntEnum):
    VAL1=1
    VAL2=2

def go(val:IntEnum)->dict[IntEnum,int]:
    return {val:val.value*2}

res=go(MyEnum.VAL1)
