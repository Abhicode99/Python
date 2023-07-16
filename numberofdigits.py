
class Numberofdigits:

    def __init__(self):
        self.str = input('What is your String')
        temp = self.count_digits_in_string(self.str)

        print(f"The number of digits in {self.str} is {temp}")

    def count_digits_in_string(self, s):
        count = 0
        for i in s:
            if i.isnumeric():
                count += 1
        return count