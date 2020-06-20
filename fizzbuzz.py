#This code is best for future use of this program
for i in range(1, 101):
    fizz = 3
    buzz = 5
    fizzbuzz = fizz * buzz
    
    if i % fizzbuzz == 0:
        print("FizzBuzz")
        continue
    elif i % fizz == 0:
        print("Fizz")
        continue
    elif i % buzz == 0:
        print("Buzz")
        continue
    else:
        print(i)

