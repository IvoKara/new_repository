for i in range(10):
    if i == 45:
        break
else:           #if the loop is not 'broken'
    print("Unbroken1")
i = 0
while i < 10:
    if i == 5:
        break
    i+=1
    
else:
    print("Unbroken@")

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:   # if no err in try
   print(5)

try:
   print(1)
except ZeroDivisionError:
   print(4)
else:
   print(5)
