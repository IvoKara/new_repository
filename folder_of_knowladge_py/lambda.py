f = (lambda x: x * x)(5)
print(f)

f = lambda x: x % 3 != 0 and x % 5 == 0
print(f(20))
print(f(15))

print([elem for elem  in range(1000) if f(elem) == True])

print([i for i in range(1000) if (lambda x: x % 3 != 0 and x % 5 == 0)(i)])

print([i for i in [j for j in range(1001) if j % 5 == 0]if i % 3 != 0])

print([i for i in range(1000) if i % 5 == 0 if i % 3 != 0])

x = None
x = 5
if (x != None and x + 5 > 8):
    print(x)
#не се проверява второто ако първото е грешно

