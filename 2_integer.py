# each Roman symbol convert to integer
def value(x):
    if (x == 'I'):
        return 1
    if (x == 'V'):
        return 5
    if (x == 'X'):
        return 10
    return 0
 
# function to convert Roman symbol to integer
def roman_To_int(string:str):
    res = 0
    i = 0
 
    while (i < len(string)):
        s1 = value(string[i])
        if (i + 1 < len(string)):
            s2 = value(string[i + 1])
            if (s1 >= s2):
                # Value of current symbol is greater or equal to the next symbol
                res = res + s1
                i += 1
            else:
                # Value of current symbol is greater or equal to the next symbol
                res = res + s2 - s1
                i += 2
        else:
            res += s1
            i += 1
 
    return res # is a int

# function to check if there is letter in string (if there is, return True)
def letter(string):
    for i in string:
        if i.isalpha():
            return True
    return False


# class
class Integer:
    def __init__(self, value):
        self.value = value
    
    @classmethod
    def from_float(cls, value):
        if type(value) == float:
            # create a new instance
            value = int(value * value)
            return cls(value)
        else:
            return "value is not a float"
    
    @classmethod
    def from_roman(cls, roman:str):
        if any(char not in "VIX" for char in roman):
            return "wrong type"
        else:
            return cls(roman_To_int(roman))

    @classmethod
    def from_string(cls, string:str):
        if type(string) == str and letter(string) == False:
            return cls(int(string))
        else:
            return "wrong type"

    def add(self, integer):
        if type(integer) == Integer:
            self.value += integer.value
            return self.value
        else:
            print("number should be an Integer instance")


first_num = Integer(10)
second_num = Integer.from_roman("IV")
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))
        
