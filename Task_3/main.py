import random
import string


if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6): "))
            if length < 6:
                print("Please enter a length of at least 6.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
            
    s = []

    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print("Your password is: "+ "".join(random.sample(s, length)))