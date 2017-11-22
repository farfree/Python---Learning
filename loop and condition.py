from sys import argv
if len(argv) > 1:
    print('Hello,', argv[1])
else:
    print('Hello, Guest')

from sys import argv
print('Hello,', argv[1] if len(argv) > 1 else 'Guest')

numbers = [10, 20, 30]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)

print([number ** 2 for number in numbers])

numbers = [11, 2, 45, 1, 6, 3, 7, 8, 9]
print([number for number in numbers if number % 2 != 0])

#當你使用 [] 包圍住 for 包含式（comprehension） 時，會建立 list 實例，如果使用 {} 的話，可以建立 set 實例
lts = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1,4,7]]
print([ele for lt in lts for ele in lt])
print({ele for lt in lts for ele in lt})

m = 1000
n = 500
while n != 0:
   r = m % n
   m = n
   n = r
print('GCD: {0}'.format(m))

numbers = []
for number in range(20):
    numbers.append(str(number))
print(numbers)
print(", ".join(numbers))

print(", ".join([str(number) for number in range(20)]))
