# The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
#  An additional requirement is that the result is not to exceed 25, which is done with the break statement. 
# Fill in the blanks to complete the function to satisfy these conditions.



def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:
      result = multiplier * number
      if result > 25:
          break
      if result == (number * 5):
          print(str(number) + "x" + str(multiplier) + "=" + str(result))
      else:
          print(str(number) + "x" + str(multiplier) + "=" + str(result), end=" ")
      multiplier += 1


multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24