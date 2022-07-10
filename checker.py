# code by Savir Singh

number = int(input())
prime = 0

def checkprime(x):
    global prime
    if x != 1:
        if x != 2:
            for i in range(2, int(x**0.5)+2):
                if x % i == 0:
                    prime = 0
                    break
                else:
                    prime = 1
        else:
            prime = 4
    else:
        prime = 3
            
    if prime == 0:
        print("not prime")
    elif prime == 1:
        print("prime")

    elif prime == 3:
        print("neither prime nor composite")

    else:
        print("prime")

checkprime(number)
