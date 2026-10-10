def average(*numbers):
    sum = 0
    for i in numbers:
     sum =   sum + i
    return sum / len(numbers) 

sum = average(1, 2, 3, 4, 5)
print(sum)