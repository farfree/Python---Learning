#filename = input('檔名:')


file = open("Hello_CHT", 'r', encoding='UTF-8')
content = file.read()
file.close()

print (content)
print(content.encode('UTF-8'))
#print(content.encode('UTF-8').decode('UTF-8'))
