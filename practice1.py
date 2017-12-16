names = ['Justin', 'caterpillar', 'openhome']

for idx in range(0,3,1):
    print("{0},{1}".format(idx, names[idx]))

print ("\n")

a = zip([1,2,3], names)
print (*a)


print(list(filter(lambda ele: len(ele) > 6, names)))
print(list(filter(lambda ele: 'i' in ele, names)))
print(list(map(lambda ele: ele.upper(), names)))
print(list(map(lambda ele: len(ele), names)))

print("\n")

print([ele for ele in names if len(ele) > 6])
print([ele for ele in names if 'i' in ele])
print([ele.upper() for ele in names])
print([len(ele) for ele in names])

print("\n")
print((ele for ele in names if len(ele) > 6))
print((ele for ele in names if 'i' in ele))
print((ele.upper() for ele in names))
print((len(ele) for ele in names))
