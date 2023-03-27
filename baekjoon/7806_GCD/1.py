import math 
from math import gcd
import sys
# gcd(n!,k)
sys.stdin = open("input.txt")
n, k = map(int,input().split())
a = math.factorial(n)
print(gcd(a,k))