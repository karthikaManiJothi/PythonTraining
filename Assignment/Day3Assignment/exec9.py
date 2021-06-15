# product of list of rational numbers

from fractions import Fraction

list1=[1/2,3/4,1/2,3/4,5/6,2/3]
mul=1
for i in list1:
    mul*=i

print("fractional value:",Fraction(mul))