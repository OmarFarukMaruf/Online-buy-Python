import collections
# cubes = [i**3 for i in range(5)]
# print(cubes)


# a = 'this is some text'
# b = a.split()
# ave = sum(len(i) for i in b)
# print(ave)
num = {
    1 : "Apple",
    "Orange" : [2,4,6],
    True : False,
    12 : "True"
}
print(num.get("Orange"))
print(num.get(7, 42))
print(num.get(12345, "Not Found"))