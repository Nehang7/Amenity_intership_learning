def gmean(a, b):
    mean = (a * b) / (a + b)
    return mean


def compare(a, b):
    if a > b:
        print("A IS GRATER THAN B")
    elif a < b:
        print("B IS GRATER THAN A")
    elif a == b:
        print("A IS EQUAL TO B")
    else:
        print("INVALID INPUT")


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
gmean(a, b)
compare(a, b)
