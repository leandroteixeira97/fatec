c = 18644
numbers = []

while c <= 33087:
  if "2" in list(str(c)) and "7" not in list(str(c)):
    numbers.append(c)
  c = c + 1
               
print(len(numbers))