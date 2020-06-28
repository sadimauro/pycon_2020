#!/usr/bin/env python3

from scipy.stats import chisquare
from typing import List
from random import randint

def chi2_pval_bytes(f_obs: List[int]) -> float:
    if len(f_obs) != 256:
        raise Exception("f_obs must be len 256")
    return chisquare(f_obs)[1]

f_obs = []
n_obs = 1000

for i in range(256):
    f_obs.append(0)
for i in range(1000):
    f_obs[randint(0, 255)] += 1
print(chi2_pval_bytes(f_obs))

