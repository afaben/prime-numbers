number = int(input("Please type a number and I will tell you if it is a prime: "))

def prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return(str(number) + " is not a prime number. It is divisible by " + str(i))
            else:
                return(str(number) + " is a prime number.")

print(prime(number))
