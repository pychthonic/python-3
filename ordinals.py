class OrdinalNumber:
    """Take any integer theoretically up to infinity and convert it to an
    ordinal number.

    For example, if 1256 is input, output will be 'one thousand two hundred
    fifty-sixth'. It will take any number up to as large as your computer 
    will handle.

    Seven lists of number name variables are used to make the conversion.

    Sidenote, as I pep8ify this code and make it object-oriented, I cannot
    believe I wrote this thing in Vim... my index and middle finger had
    to take turns on the mouse wheel moving the file view up and down
    as I made it work over the course of five days. When I started the
    project I thought it would take a few hours. Next thing I knew it was
    5 days later and I was still working on it. But it works! And it's a 
    beast. It handles page-long numbers like Joel Embiid handles disrespect.
    Only thing it doesn't do is tweet shittalk at the numbers after it 
    converts them.

    Throughout the script, "num" and "string" are used as local variables
    inside specific functions.
    """
    nums_1_to_19 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
                    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
                    'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                    'eighteen', 'nineteen']

    nums_tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
                 'seventy', 'eighty', 'ninety']

    place_values_1 = ['', 'thousand', 'million', 'billion', 'trillion',
                      'quadrillion', 'quintillion', 'sextillion', 'septillion',
                      'octillion', 'nonillion', 'decillion']

    place_values_2 = ['', 'un', 'duo', 'tre', 'quattuor', 'quin', 'sex',
                      'septen', 'octo', 'novem']

    place_values_3 = ['tillion', 'decillion', 'vigintillion', 'trigintillion',
                      'quadragintillion', 'quinquagintillion',
                      'sexagintillion', 'septuagintillion', 'octogintillion',
                      'nonagintillion']

    place_values_4 = ['', 'cen', 'duocen', 'trecen', 'quadringen', 'quingen',
                      'sescen', 'septingen', 'octingen', 'nongen']

    place_values_5 = ['', 'dec', 'vigin', 'trigin', 'quadragin', 'quinquagin',
                      'sexagin', 'septuagin', 'octogin', 'nonagin']

    def __init__(self, number):
        """Initializes and completes the process of converting an
        integer to an ordinal number.
        """
        self.number = number
        self.ord_num = self.get_ord_number()

    def get_post_millia_string(self, place_value):
        """Return ordinal number string for numbers greater than one
        millia.
        """
        millias_number_local = 0
        place_value -= 1
        while place_value:
            relevant_place_value = ((place_value) % 1000)
            if (millias_number_local == 0):
                string = self.get_0_to_1000_power_string(relevant_place_value)
                if (str(place_value)[:-3] != ''):
                    place_value = int(str(place_value)[:-3])
                else:
                    place_value = 0
                millias_number_local += 1
            else:
                new_string = (
                    self.place_values_4[relevant_place_value // 100]
                    + self.place_values_2[(relevant_place_value) % 10]
                    + self.place_values_5[(relevant_place_value % 100) // 10]
                    )
                if new_string:
                    string = (
                        new_string
                        + ("millia" * millias_number_local)
                        + string
                        )
                if (str(place_value)[:-3] != ''):
                    place_value = int(str(place_value)[:-3])
                else:
                    place_value = 0
                millias_number_local += 1
        if string[:8] == 'unmillia':
            string = string[2:]
        return string

    def get_0_to_1000_power_string(self, place_value):
        """Return ordinal number string for numbers larger than one millia
        that are powers of 0 to 1000.
        """
        if (place_value == 0):
            return_number = (
                self.place_values_4[place_value // 100]
                + self.place_values_2[place_value % 10]
                + self.place_values_3[(place_value % 100) // 10]
                )
        elif (place_value < 10):
            return_number = self.place_values_2[place_value] + 'tillion'
        elif (place_value < 100):
            return_number = (
                self.place_values_2[(place_value) % 10]
                + self.place_values_3[((place_value) // 10)]
                )
        elif (place_value < 1000):
            return_number = (
                self.place_values_4[(place_value) // 100]
                + self.place_values_2[(place_value) % 10]
                + self.place_values_3[((place_value) % 100) // 10]
                )
        return return_number

    def make_ordinal(self, num_str):
        """ Handle last word of the final_number string."""
        if num_str[-3:] == 'one':
            num_str = num_str[:-3] + 'first'
        elif num_str[-3:] == 'two':
            num_str = num_str[:-3] + 'second'
        elif num_str[-5:] == 'three':
            num_str = num_str[:-5] + 'third'
        elif num_str[-4:] == 'four':
            num_str = num_str[:-4] + 'forth'
        elif num_str[-4:] == 'five':
            num_str = num_str[:-4] + 'fifth'
        elif num_str[-5:] == 'eight':
            num_str += 'h'
        elif num_str[-7:] == 'twelve':
            num_str = num_str[:-7] + 'twelfth'
        elif num_str[-2:] == 'ty':
            num_str = num_str[:-2] + 'tieth'
        else:
            num_str = num_str + 'th'
        return num_str

    def get_two_digit_number(self, two_digit_number):
        """Take a two-digit integer and return it as an ordinal
        number string.
        """
        if two_digit_number < 20:
            num = self.nums_1_to_19[two_digit_number]
        else:
            num = self.nums_tens[two_digit_number // 10]
            if (two_digit_number % 10 == 0):
                return num
            else:
                num += '-' + self.nums_1_to_19[two_digit_number % 10]
        return num

    def get_three_digit_number(self, three_digit_number):
        """Take a three-digit integer and return it was an ordinal
        number string.
        """
        if three_digit_number < 100:
            num = self.get_two_digit_number(three_digit_number)
        else:
            if (three_digit_number % 100 == 0):
                num = (
                    self.nums_1_to_19[three_digit_number // 100]
                    + ' hundred'
                    )
            else:
                num = (
                    self.nums_1_to_19[three_digit_number // 100]
                    + ' hundred '
                    + self.get_two_digit_number(three_digit_number % 100)
                    )
        return num

    def get_100_to_1000_power_str(self, place_value):
        """Return ordinal number string for numbers in the range of
        powers of 100 to 1000.
        """
        if (place_value % 100 > 0) and (place_value % 100 <= 10):
            string = (
                self.place_values_4[(place_value - 1) // 100]
                + self.place_values_2[(place_value - 1) % 10]
                + 'tillion'
                )
        else:
            string = (
                self.place_values_4[(place_value - 1) // 100]
                + self.place_values_2[(place_value - 1) % 10]
                + self.place_values_3[((place_value - 1) % 100) // 10]
                )
        return string

    def get_ord_number(self):
        self.place_value_position = 0
        self.final_number = ""
        while (self.number):
            self.number = str(self.number)
            three_digit_number = int(self.number[-3:])
            three_digit_number = self.get_three_digit_number(
                                                            three_digit_number)
            if (self.place_value_position > 0) and (
                    three_digit_number == 'zero'):
                three_zeros = True
            elif (self.place_value_position > 0) and (
                    self.place_value_position < 12):
                self.final_number = (
                    three_digit_number
                    + ' '
                    + self.place_values_1[self.place_value_position]
                    + ' '
                    + self.final_number
                    )
            elif (self.place_value_position > 0) and (
                    self.place_value_position < 101):
                self.final_number = (
                    three_digit_number
                    + ' '
                    + self.place_values_2[self.place_value_position % 10 - 1]
                    + self.place_values_3[(
                        self.place_value_position - 1) // 10]
                    + ' '
                    + self.final_number
                    )
            elif (self.place_value_position > 0) and (
                    self.place_value_position < 1001):
                self.final_number = (
                    three_digit_number
                    + ' '
                    + self.get_100_to_1000_power_str(self.place_value_position)
                    + ' '
                    + self.final_number
                    )
            elif (self.place_value_position > 1000):
                self.final_number = (
                    three_digit_number
                    + ' '
                    + self.get_post_millia_string(self.place_value_position)
                    + ' '
                    + self.final_number
                    )
            else:
                self.final_number = three_digit_number
            self.place_value_position += 1
            if self.final_number[-4:] == 'zero':
                self.final_number = self.final_number[:-4]
            if self.final_number[-1:] == ' ':
                self.final_number = self.final_number[:-1]
            self.number = self.number[:-3]
            if self.number != '':
                self.number = int(self.number)
            else:
                num = 0
        self.final_number = self.make_ordinal(self.final_number)
        return self.final_number


if __name__ == "__main__":
    number = input("Enter a number to ordinalize: ")
    ord_number = OrdinalNumber(number)
    print("\n{}:\n\n{}\n".format(number, ord_number.ord_num))
