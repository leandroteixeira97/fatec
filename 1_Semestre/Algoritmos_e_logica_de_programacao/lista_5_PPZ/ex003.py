n = 1067
numbers = []

while n <= 3627:
    if n % 2 == 0:
        if n % 7 == 0:
            numbers.append(n)
    n = n + 1
   
print(len(numbers))