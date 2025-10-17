# Remove First and Last Character
import random

LARGE_NUMBERS = [22,43,64,50,30,89]
SMALL_NUMBERS = [1,2,3,4,5,6,7,8,9] * 2

def generate_random_number(start, stop) -> int:
    num = random.randint(start, stop)
    return num

def random_large_numbers(num) -> list[int]:
    generated_large_numbers = []
    for i in range(0, num):
        generated_large_numbers.append(generate_random_number(100,999))
    return generated_large_numbers

def random_small_numbers(num) -> list[int]:
    generated_small_numbers = []
    for i in range(0,num):
        generated_small_numbers.append(generate_random_number(1,9))
    return generated_small_numbers

def generate_target_number(start,stop):
    target_number = random.randint(start,stop)
    return target_number

multi = []

def main() -> None:
    random_larges = random_large_numbers(5)
    random_smalls = random_small_numbers(5)
    sums = []
    print(random_larges)
    

if __name__ == "__main__":
    main()