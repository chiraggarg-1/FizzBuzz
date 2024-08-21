
for counting in range(1,101):
    if counting % 3 == 0 and counting % 5 == 0:
     print("FizzBuzz")
    elif counting % 3 == 0:
        print("Fizz")
    elif counting % 5 == 0:
        print("Buzz")
    else:
        print(counting)