# file = open('MyFile.txt')
# all_lines = file.readlines()

# str_match = [s for s in all_lines if s.__contains__("aa")]
# print(str(str_match)[2:-4])


print("---Search Your Desire Phone----")
print("_______________________________________________")
print("Smartphone's Brand: ")
brand = input()

file = open('MyFile.txt')
all_lines = file.readlines()
str_match = [s for s in all_lines if s.__contains__(brand)]
print('Brand' + '\t|\t' + 'Model' + '\t|\t' + 'Price')
print("_______________________________________________")
print(*str_match, sep = "\n")

print("Model : ")
model = input()
str_match2 = [s for s in str_match if s.__contains__(model)]
print('Brand' + '\t|\t' + 'Model' + '\t|\t' + 'Price')
print("_______________________________________________")
print(*str_match2)
print("Do You Want To Buy this? : Yes/No")
ans = input()
if ans == ('Yes' or 'yes'):
    print("Make sure your payment ", str_match2[0])
if ans == ('No' or 'no'):
    print("HEllo World!")
