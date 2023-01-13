#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(array):
    dictionary = {}
    
    for element in array:
        dictionary[element] = 1 if dictionary.get(element) == None else dictionary[element] + 1
        
    keys = sorted(dictionary.keys())
    length = len(keys)
    maximumLength = dictionary[keys[0]]
    
    for i in range(1,length):
        if maximumLength < dictionary[keys[i]]:
            maximumLength = dictionary[keys[i]]
        if keys[i] - keys[i-1] <= 1 and maximumLength < dictionary[keys[i]] + dictionary[keys[i-1]]:
            maximumLength = dictionary[keys[i]] + dictionary[keys[i-1]]
    
    return maximumLength
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
