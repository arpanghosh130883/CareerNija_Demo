# Write a function to checking even numbers from list   
def even_numbers(lst):
    return [i for i in lst if i % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Write a function to checking odd numbers from list
def odd_numbers(lst):
    return [i for i in lst if i % 2 != 0]

print(odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Write a function to checking prime numbers from list
def prime_numbers(lst):
    return [i for i in lst if i > 1 and all(i % j != 0 for j in range(2, i))]

print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Write a function to add two numbers
def add_numbers(a, b):
    return a + b

