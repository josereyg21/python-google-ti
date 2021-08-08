# The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be 
# equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. 
# Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even".
#  Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

def is_palindrome(input_string):
    x = list(input_string.lower())
    x = list(filter(lambda i: i != " ", x))
    y,z = x , x
    z = z[::-1]
    d = z == y

    return d

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True