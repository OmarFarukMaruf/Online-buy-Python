from re import search
from password import password
class Customer:

    def search():
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


    def show():
        a_file = open("MyFile.txt")

        lines = a_file.readlines()
        print('Brand' + '\t|\t' + 'Model' + '\t|\t' + 'Price')
        print("_______________________________________________")
        for line in lines:
           print(line)
        a_file.close()



class Seller:

    def search(self):
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


    def show(self):
        a_file = open("MyFile.txt")

        lines = a_file.readlines()
        print('Brand' + '\t|\t' + 'Model' + '\t|\t' + 'Price')
        print("_______________________________________________")
        for line in lines:
           print(line)
        a_file.close()
    def update(self):
        print("Under Construction!")

    def delete(self):
        print("Under Construction!")

    def add(self):
        print("Product Name : ")
        num = input()
        print("Product Model : ")
        model = input()
        print("Price : ")
        price = input()
        with open("MyFile.txt", 'a') as a:
           x = a.write(num + '\t \t' + model + '\t \t' + price+ '\n')
        print(" 1 - ADD MORE..... ")
        print(" 2 - Save and exit")
        s = int(input())
        if s == 1:
            self.add()
        if s == 2:
            exit()



password()


def display1():
    print("1 - Search items")
    print("2 - Show Product")
    a = int(input())
    buy = Customer
    if a == 1:
        buy.search()
    if a == 2:
        buy.show()

def display2():
    print("1 - Search items")
    print("2 - Show Product")
    print("3 - Update items")
    print("4 - Delete Product")
    print("5 - Add items")
    print("6 - Save Product")
    sell = Seller()
    a = int(input())
    i = 1
    while (i<5):
        if a == 1:
            sell.search()
        if a == 2:
            sell.show()
        if a == 3:
            sell.search()
        if a == 4:
            sell.show()
        if a == 5:
            sell.add()

sell = Seller()
print("1 - Customer Profile")
print("2 - Seller Profile")
a = int(input())
if a == 1:
    display1()
if a == 2:
    display2()