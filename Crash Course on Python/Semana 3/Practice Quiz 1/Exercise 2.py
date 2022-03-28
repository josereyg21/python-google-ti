
# Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. 
# A prime factor is a number that is prime and divides another without a remainder.



def print_prime_factors(number):
  factor = 2
  while factor <= number:
    if number % factor == 0:
      print(factor)
      number = number / factor
    else:
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5