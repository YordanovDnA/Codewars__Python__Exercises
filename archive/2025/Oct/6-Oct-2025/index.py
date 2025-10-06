
#Calculate by given operator and two integers
import operator

def basic_op(op:str, value1:int, value2: int):
    ops = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "**" : operator.pow,
        "/" : operator.truediv,
        "//": operator.floordiv,
        "%" : operator.mod
    }
    
    try:
        return ops[op](value1,value2)
    except ValueError:
        return ValueError
    
result = basic_op("+",1,1)
print(result)

#FINDING IF NUMBER IS SQUARE NUMBER
import math
def is_square(n:int):    
    try:
        if n > -1:
            return n == math.isqrt(n) ** 2
    except ValueError:
        return False

print(is_square(0))

#PRINTER ERROR COUNTER
def printer_error(s):
    colours = [chr(i) for i in range(ord("a"), ord("m") + 1)]
    counter = 0
    for char in s:
        if char not in colours:
            counter += 1
    return "{}/{}".format(counter,len(s))

print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))

#Abreviate a Two Word Name
def abbrev_name(name):
    name = name.upper().split()
    return f"{name[0][0]}.{name[1][0]}"

print(abbrev_name("John Doe"))

#Disemvowell Trolls
def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u"]
    for char in vowels:
        string_ = string_.replace(char, "")
    return string_

def best_disemvowel(string_):
    return "".join(x for x in string_ if x not in "aouei")

print(disemvowel("This website is for losers LOL!"))
print(best_disemvowel("This website is for losers LOL!"))