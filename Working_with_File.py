"""
with open("MyFile.txt", 'a') as a:
    x = a.write("HI! I am Omar Faruk Maruf")
print(x)
a.close()

______________________

a = 'I am mad!'
b = a.split()
print(b[0])
"""



with open("MyFile.txt", 'r') as a:
    x = a.read()
    y = x.split()
    for i in y:
        i

