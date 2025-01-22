f = open("C:/python/py-language/python file handling/sample.txt", "w")
f.write("Learn Python Programming")
f.close()

f = open("C:/python/py-language/python file handling/sample.txt", "r")
read = f.read()
print(read)
f.close()