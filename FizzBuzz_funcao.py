def fizzbuzz(num):
    if (num % 5) == 0 and (num % 3) == 0:
        return "FizzBuzz"
    elif (num % 3) == 0:
        return "Fizz"
    elif (num % 5) == 0:
        return "Buzz"
    else:
        return num

numero = int(input("Digite um número:"))

print (fizzbuzz(numero))







   