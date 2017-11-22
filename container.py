print ("\nContainer\n")

#list 是有序且可變群集（Collection）
print ("List")

L = [1,2,3,4,]
print (L)
L = L * 3
print (L)

print (list('test'))

#set 型態是無序群集, 管理的元素不會重複而且必須是 hashable
print("\nSet")
admins = {'Justin', 'caterpillar'}  # 建立 set
users = {'momor', 'hamini', 'Justin'}
print(admins)
print(users)
print('Justin' in admins)  # 是否在站長群？
print(admins & users)      # 同時是站長群也是使用者群的？
print(admins | users)      # 是站長群或是使用者群的？
print(admins - users)      # 站長群但不使用者群的？
print(admins ^ users)      # XOR
print(admins > users)
print(admins < users)


#dict 型態. 鍵（Key）值（Value）對應的物件，鍵物件必須是 hashable
print("\nDict")
passwords = {'Justin' : 123456, 'caterpillar' : 933933}
print(passwords['Justin'])
passwords['Hamimi'] = 970221
print(passwords)
del passwords['caterpillar']
print(passwords)
print(passwords.items())
print(passwords.keys())
print(passwords.values())

#tuple 型態作用類似 list，不過 tuple 實例是不可變（Immutable），也就是一旦建立，無法對其增減元素。
#除了增減元素個數之外，tuple 與 list 操作上類似，事實上，循序結構的物件（像是字串、list、tuple 等），
#在 Python 中共享某些操作方式。管理物件時該使用可變物件還是不可變物件？不可變物件在某些情況下，會擁有較好的效能，
#之後還會談到更多有關不可變物件的好處。
