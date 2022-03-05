# Recursive Countdown

def countdown(i):
    print(i)
    if i <= 0: # Base Case
        return
    else:
        countdown(i-1) # Recursive Case

#countdown(5)

# The Call Stack (like a to-do list)

# pushes most recent function to top and continues to do so until one resolves
# once resolved it pops the function off the top and then resolves them down the ways

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(10))