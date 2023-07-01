from math import sqrt

def diagonal():
    diagonal = sqrt(side_length_a ** 2 + side_length_b ** 2)
    print("Diagonal:", diagonal)

def perimeter():
    perimeter = side_length_a * 2 + side_length_b * 2
    print("Perimeter:", perimeter)

def area():
    area = side_length_a * side_length_b
    print("Area:", area)

print("Rectangle Calculator by Deo Developer")

while True:
    side_length_a = int(input("\nSide length A: "))
    side_length_b = int(input("Side length B: "))
    print("\nResults\n")
    diagonal()
    perimeter()
    area()
    ctn = input("\nDo you want to continue? (y/n): ")
    if ctn == "y" or ctn == "Y":
        continue
    elif ctn == "n" or ctn == "N":
        print("Thank you")
        break