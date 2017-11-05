print(5&3)
##0101(dec 5)
##      AND
##0011(dec 3)
##-----------
##0001(dec 1)

print(5|3)
##0101 (decimal 5)
##        OR
##0011 (decimal 3)
##------------
##0111 (decimal 7)

print(5^3)
##0101 (decimal 5)
##        XOR
##0011 (decimal 3)
##-------------
##1000 (decimal 6)

a=5
b=3
print(int(a&b) + int(a^b) == int(a|b))
