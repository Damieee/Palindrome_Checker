def is_palindrome(s):
    # Convert string to lowercase and remove non-alphanumeric characters
    
    
    # Set two pointers, one at the beginning of the string and the other at the end
    
    
    # Compare characters at the two pointers and move them towards the middle
    
    
    # If we reach here, return true if the string is a palindrome
    # return True

    "TODO"

def main():
    s = input("\nEnter a string: ")
    if is_palindrome(s):
        print(f"\n{s} is a palindrome\n")
    else:
        print(f"\n{s} is not a palindrome\n")

if __name__ == '__main__':
    main()
