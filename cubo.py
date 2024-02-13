x = input(int())
y = input(int())
z = input(int())
lista = [x, y, z]
for i in lista.pop(2):
    print(int(i))

for j in lista.pop(1):
    print(int(j))
for k in lista.pop(0):
    print(int(k))

sum = i + j + k
print(sum)
