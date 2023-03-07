# Palindrome Checker using Python

## What is a Palindrome?
A Palindrome is a word, phrase, or sequence of characters that reads the same way forwards and backward. In other words, a palindrome remains the same even if the order of its letters is reversed. Examples of palindromes include "racecar," "level," "deified," and "mom."

## Using Python to Check for Palindromes:
In this project, you are tasked with writing a Python program to check if a given string is a palindrome or not. You will be given a function called "is_palindrome" that takes a string as input and returns true if the string is a palindrome, false otherwise.

## What You Stand to Gain:

Writing this program will help you improve your skills in Python programming, string manipulation, and algorithm development. It will also help you better understand concepts such as pointers, loops, and conditional statements.

## Task:

Your task is to complete the implementation of the "is_palindrome" function. The function currently has no implementation and all test cases fail. Your implementation should follow the steps outlined in the function comments.

## Hints:

### Convert the string to lowercase using the lower() method:
Before comparing the characters, it's a good idea to convert the input string to lowercase to avoid any case-sensitivity issues. You can do this by calling the lower() method on the input string.

### Remove non-alphanumeric characters using the isalnum() method:
Palindromes are typically only composed of letters and numbers. To remove any non-alphanumeric characters, you can loop through the input string and use the isalnum() method to check if each character is alphanumeric. If a character is alphanumeric, add it to a new string. Otherwise, skip it.

### Use two pointers to compare characters:
To check if a string is a palindrome, you need to compare the characters at the beginning and end of the string, and then move inward. You can use two pointers to keep track of the characters you are comparing. One pointer can start at the beginning of the string, and the other can start at the end.

### Use a while loop to move the pointers towards the middle:
You can use a while loop to compare the characters at the beginning and end of the string. Inside the loop, you can compare the characters at the two pointers. If they are not equal, return False because the string is not a palindrome. If they are equal, move the pointers towards the middle of the string and continue the loop.

### Return True if the string is a palindrome:
If the loop completes without finding any non-matching characters, that means the string is a palindrome. You can return True to indicate this.

## Testing your implementation:

After writing the code, you should test your implementation by:

#### 1. Running the main() function:
The main() function prompts the user to enter a string and then calls the is_palindrome() function to check if the string is a palindrome or not. You can try out different input strings to see if your implementation works correctly.

#### 2. Running the palindrome_test.py to confirm that all test passed.

Good luck and have fun coding!
