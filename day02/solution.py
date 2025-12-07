

import math

def find_all_factors_optimized(num):
    """
    Finds all factors of a given number using an optimized iteration up to the square root.
    """
    factors = set()  # Using a set to automatically handle duplicates and maintain uniqueness
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return sorted(list(factors))  # Convert to list and sort for ordered output


def repeat_checker(x):
    x_str = str(x)
    factors=find_all_factors_optimized(len(x_str))[:-1]
    for fact in factors:
        
        candidate=x_str[0:fact]
        failed= False 
        for i in range(0,len(x_str),len(candidate)):
            if candidate!=x_str[i:i+len(candidate)]:
                failed=True
        if not failed:
            return True 
    return False 

def repeat_twice_checker(x):
    x_str = str(x)
    if len(x_str) %2 !=0:
        return False
    half=len(x_str)//2 
    return x_str[0:half]==x_str[half:]
 
with open('input.txt', 'r') as f:

   ranges = f.readline().strip().split(',')
#ranges='11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'.split(',')
ids=[r.split('-') for r in ranges]
invalids=0
invalids_part2=0
for id in ids:
    for i in range(int(id[0]),int(id[1])+1):
        if repeat_twice_checker(i):
            invalids+= i
        if repeat_checker(i):
            invalids_part2+=i
print(invalids)
print(invalids_part2)
