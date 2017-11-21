# coding=UTF-8

import API
import sys

#filename = input('檔名:')

print (len(sys.argv))

file = open("Hello_CHT", 'r', encoding='UTF-8')
content = file.read()
file.close()


print (content)
#print(content.encode('UTF-8'))
#print(content.encode('UTF-8').decode('UTF-8'))

file.write("test")
file.close()

file = open("Hello_CHT", 'r', encoding='UTF-8')
while True:
    line = file.readline()
    if not line: break
    print (line)

file.close()

for line in open("Hello_CHT", 'r', encoding='UTF-8'):
    print (line)
