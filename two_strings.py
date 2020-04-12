import math
import os
import random
import re
import sys

# Complete the twoStrings function below.

#takes in two strings s1 and s2. Returns yes if there exists a common substring else, no.
#strings are alphabetic a-z lengths of s1 and s2 can be 10^5 length
#substring can be length 1
def twoStrings(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    result = set(s1).intersection(s2)
    print(result)
    if len(result) > 0:
        return "YES"
    else:
        return "NO"

def main():
    s1 = "t"
    s2 = "ab"

    print(twoStrings(s1, s2))

main()