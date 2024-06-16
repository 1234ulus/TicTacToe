import main
def is_a_number():
    while True:
        answer = input("Type a number: ")
        try:
            return int(answer)
        except ValueError:
            print("It is not a number!")

def verify_number(number):
    if number < 0 or number >= 20:
        raise ValueError(f"The position {number} is not in the allowed range!")
    print(f"The position {number} is OK!")

def input_side():
    while True:
        raw_input = input("Enter the side of a square in centimeters: ")
        try:
            side = float(raw_input)
        except ValueError:
            print(f"{raw_input} is not a number!")
        else:
            if side <= 0:
                print(f"{raw_input} is a negative number!")
            else:
                break
    return side
side = input_side()