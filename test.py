level = int(input("level: "))

if level == 19:
    number = 20
else:
    number = level

for num in range(4, number+1, 4):
    print(num)
print(len(range(4, number+1, 4)))