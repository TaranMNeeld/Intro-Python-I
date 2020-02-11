import math

def get_prime_numbers(max_num):
    # make an array with all numbers between 2 and the input number
    numbers = [int(i) for i in range(2, max_num)]

    # loop through each number between 2 and the input number
    for num in range(2, max_num):

        numSqrt = math.sqrt(num)

        # loop through every number from 2 to the sqrt of current num
        for i in range(2, math.ceil(numSqrt)):

            # test if each number between 2 and the input number is divisible by any number between 2 and (itself - 1)
            if num % i == 0:

                # remove a number from the array if it is prime
                numbers.remove(num)

                # break so the loop can move on now that the number was removed
                break

    print(numbers)

enter_num = input('Please enter a number:')

get_prime_numbers(int(enter_num) + 1)