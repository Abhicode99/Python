
class Palindrome:

    def __init__(self):
        self.str = input('What is the String to be checked? ')
        if self.validate_str(self.str) :
            self.check_palindrome(self.str)
        else:
            print("It is not a String")
    def check_palindrome(self, str):
        s=str.lower()
        if s[::-1] == s:
            print('Yes!!!!!!! It is a palindrome')
        else:
            print('Nope!! Not a palindrome')
    def validate_str(self,str):
        return str.isalpha()
