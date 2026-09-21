from collections.abc import Hashable
from typing import Any
from enum import Enum
a = dict[Any,int]

b:a={1:1}

class myEnum(Enum):
    VAL1=1
    VAL2=2

c:a={myEnum.VAL1:1}


from dataclasses import dataclass

@dataclass
class MyClass:
    my_dict:a

myclass=MyClass(my_dict={1:1})
other = MyClass(my_dict={myEnum.VAL1:1})