# coding=UTF-8
#Numeric type - int, long, float, bool, complex
#String type
#Container type - list, set, dict, tuple


#Numeric
print ("Numberic\n")
print (type(1))
#print (type(1L))
print (type(1111111111111111111111111111))
print (type(3.14))
print (type(True))
print (type(3 + 4j))
print (3 + 4j)
print (type( 2** 100))

print (10 / 3)
print (10 // 3)
print (10 / 3.0)
print (10 // 3.0)

print (1.0 - 0.8)
print (str(1.0 - 0.8))

import decimal

a = decimal.Decimal('1.0')
b = decimal.Decimal('0.8')
print (a - b)


print ("\nString\n")

str1 = "1234567890"
print (str1)
print (str1[1:5])
print (str1[3:])
print (str1[:7])
print (str1[::2])
print (str1[::3])
print (str1[::-1])
print (str1[::-2])

import sys
print (sys.platform)
print ('My platform is {pc.platform}'.format(pc = sys))
