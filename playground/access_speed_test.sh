#!/bin/bash
set -e

echo "Creating various classes and dicts with a property of 'var'."
echo "timing the creation step, and the attribute access (of 'var') speed."
echo ""
python --version

echo -e "\ndict"
echo "----"
echo -n "instantiation    "
python -m timeit -n 10000000 "{'var': 1}"
echo -n "attribute access "
python -m timeit -n 10000000 -s "d = {'var': 1}" "a = d['var']"


echo -e "\npython class with slots"
echo "-----------------------"
echo -n "instantiation    "
python -m timeit -n 10000000 -s  "class A:" -s "    __slots__=('var',)" -s "    def __init__(self,var):"  -s "        self.var=var", "A(1)"
echo -n "attribute access "
python -m timeit -n 10000000 -s  "class A:" -s "    __slots__=('var',)" -s "    def __init__(self,var):"  -s "        self.var=var", -s "d=A(1)" "a=d.var"


echo -e "\ndataclass"
echo "---------"
echo -n "instantiation    "
python -m timeit -n 10000000 -s "from dataclasses import dataclass" -s "@dataclass" -s "class A: var: int" "A(1)"
echo -n "attribute access "
python -m timeit -n 10000000 -s "from dataclasses import dataclass" -s "@dataclass" -s "class A: var: int" -s "d = A(1)" "a=d.var" 

echo -e "\ndataclass with slot"
echo "-------------------"
echo -n "instantiation    "
python -m timeit -n 10000000 -s "from dataclasses import dataclass" -s "@dataclass(slots=True)" -s "class A: var: int" "A(1)" 
echo -n "attribute access "
python -m timeit -n 10000000 -s "from dataclasses import dataclass" -s "@dataclass(slots=True)" -s "class A: var: int" -s "d = A(1)" "a=d.var"
