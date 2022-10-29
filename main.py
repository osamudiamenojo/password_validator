import sys
special_characters = ['&', '#', '$', '!', '?', '"', '(', ')', '.']

alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
                                                                                                                          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeric_characters=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Define fixed values here
MIN_LENGTH = 6
MAX_LENGTH=12
regular_character_count, special_characters_count=0, 0

# Write your code here
print("Enter a password for validation.")
print(" The password should meet the following criteria: ")
print(" 1) Length is between (6, 12)")
print(" 2) Value has at least 5 regular characters")
print(" 3) Value has at least 3 special characters")

password =input("Your Password: ")
if (MIN_LENGTH <=len(password) <=MAX_LENGTH):
    for character in password:
        if (character in alphabetic_characters) or (character in numeric_characters):
            regular_character_count+=1  
        if character in special_characters:
            special_characters_count+=1
    if (regular_character_count<5 ):
        print("Validation Failed: You need to have a minimum of 5 regular characters.")
        sys.exit(0)
    else:
        if special_characters_count<3:
            print("Validation Failed: You need to have a minimum of 3 special characters. ")
            sys.exit(0)
        else:
            print("Validation Succeeded!") 
            sys.exit(0)
else:
    print("Validation Failed: Your password should contain a minimum of 6 and maximum of 12 characters.")
