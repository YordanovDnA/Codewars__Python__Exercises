#Calculate how many beef burgers for days consumed
# > How many days to caluclate for?
# > How many burgers a day you will consume?



def calculate_burgers(burgers, days):
    return burgers * days

def main():
    print("Hello User!")
    burgers = int(input("> How many days to caluclate for? "))
    days = int(input("> How many burgers a day you will consume? "))
    print(f'You will need {calculate_burgers(burgers,days)} burgers.')
if __name__ == "__main__":
    main()

