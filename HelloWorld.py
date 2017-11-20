print ("Basic Concept\n")
str1 = "Hello World.\n"
str2 = "I am farfree\n"
print (str1 * 2 + str2)
print ("** means square. EX: 2**7 = " + str(2**7) + "\n")

print ("\nBoolean")
print ("2 > 3 is " + str(2>3))
print ("2 > 3 is " + str(2<3))

print ("\nFollowing is List")
list1 = [4, 5, 7, 9, 0xff]
print ("List = " + str(list1) + ", Length = " + str(len(list1)))
print ("List[0] = List[-4] = " + str(list1[-4]))
print ("List[4] = List[-1] = " + str(list1[-1]))

list1[2] = 10
print ("Modify list1[2] to 10 = " + str(list1[2]))

print ("\nFollowing is Dictionary")
dict1 = {"name":"Alex", "age":18, "City":"LA"}
print ("Dict = " + str(dict1) + ", Length = " + str(len(dict1)))
print ("dict1[\"name\"] = " + str(dict1["name"]))

dict1["phone"] = 123
print ("Add phone key to dict dict1[\"phone\"] = " + str(dict1["phone"]))
del dict1["age"]
print ("Del age key by \"del dict1[\"age\"]\"")
print (dict1)

if 1 > 2:
    print ("if 1 > 2:")
elif 3 > 2:
    print ("elif 3 > 2:")
else:
    print ("else:")

