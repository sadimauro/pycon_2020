#!/usr/bin/env python3
"""
version: 0.0
"""

from scipy.stats import chisquare
from typing import List
from random import randint

def chi2_from_freqs_pval(
        f_obs: List[int],
        ) -> float:
    if len(f_obs) != 256:
        raise Exception("list of observations must be len 256")
    return chisquare(f_obs)[1]

def chi2_from_freqs_is_random(
        f_obs: List[int], 
        alpha: int=0.05,
        ) -> bool:
    """
    Return true if the p-value calculated from the observed frequencies is greater than the indicated alpha value (defaults to 0.05, i.e. if the null hypothesis should be accepted, and so we likely have random data.
    """
    return chi2_from_freqs_pval(f_obs) > alpha 

def chi2_is_random(
        data: bytes, 
        alpha: int=0.05,
        unit_size_bits: int=8, 
        ) -> bool:
    """
    Return true if the p-value calculated from the given data is greater than the indicated alpha value (defaults to 0.05, i.e. if the null hypothesis should be accepted, and so we likely have random data.

    Each observation is extracted from data and is unit_size_bits long.  Default is 8 (observations are bytes).
    """
    # Build frequency table
    f_obs = []
    for i in range(2**unit_size_bits):
        f_obs.append(0)
    if unit_size_bits == 8:
        for i in range(len(data)):
            f_obs[data[i]] += 1
    else:
        raise Exception(f"unit_size_bits = {unit_size_bits} not yet implemented")
    
    return chi2_from_freqs_pval(f_obs) > alpha 

# testing
data = bytes([randint(0, 255) for i in range(1000)])
print(f"{chi2_is_random(data)=}")

f_obs = []
for i in range(256):
    f_obs.append(0)
for i in range(len(data)):
    f_obs[data[i]] += 1
print(chi2_from_freqs_pval(f_obs))
print(chi2_from_freqs_is_random(f_obs))

