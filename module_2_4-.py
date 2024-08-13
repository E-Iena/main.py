numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # простые числа
not_primes = []  # не простые числа
for i in range(len(numbers)):
    for j in range(2, 16):
        is_prime=True
        if (numbers[i] % j) == 0 and numbers[i] == j and numbers[i] != 1 and is_prime == True:
            primes.append(numbers[i])
            is_prime=False
        elif (numbers[i]%j)==0 and (numbers[i]) != j and numbers[i]!=1 and is_prime==True:
            not_primes.append(numbers[i])
            break
print('НЕ простые числа ', not_primes)
print('ПРОСТЫЕ числа ', primes)
