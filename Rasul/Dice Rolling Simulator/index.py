import random

def roll_dice():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

def main():
    print("Dice Rolling Simulator")

    while True:
        input("Press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"The dice rolled: {dice_value}")

        play_again = input("Do you want to roll again? (y/n): ")
        if play_again.lower() != "y":
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()

