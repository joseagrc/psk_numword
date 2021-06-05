# -*- coding: utf-8 -*-
from numword import numword_es

conv = numword_es.NumWordES()

data = (
    2171,
    123456,
    987654,
    21907651,
    41907631,
    821,
    21,
    221212001,
    1040040,
    1,
    5,
    51,
    100000,
    1000000,
    103000,
)

for i in data:
    print("----------------------------------------------------")
    print(i, conv.cardinal(i))
