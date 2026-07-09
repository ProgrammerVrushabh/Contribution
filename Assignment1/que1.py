integers = []
prime_list = []
for i in range(20):
    number = int(input("Enter an integer: ")) #user input
    integers.append(number)
for number in integers:
    if number > 1:        # 1 is always prime
        is_prime = True
        for i in range(2, number):         # condition for other than 1 if prime or not
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(number)
print("\nList of Numbers:", integers)    #result
print("Prime Numbers:", prime_list)
print("Total Prime Numbers:", len(prime_list))