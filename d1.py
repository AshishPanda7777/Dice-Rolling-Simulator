import random

def roll_die(sides=6):
    """Simulate rolling a single die with a given number of sides."""
    return random.randint(1, sides)

def roll_dice(num_dice, sides=6):
    """Simulate rolling multiple dice with a given number of sides."""
    rolls = [roll_die(sides) for _ in range(num_dice)]
    return rolls

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            sides = int(input("Enter the number of sides on each die (e.g., 6 for D6, 20 for D20): "))
            
            if num_dice <= 0 or sides <= 0:
                print("Please enter positive integers for the number of dice and sides.")
                continue
            
            rolls = roll_dice(num_dice, sides)
            print(f"You rolled: {rolls}")
            print(f"Total: {sum(rolls)}")
            
            another_roll = input("Do you want to roll again? (yes/no): ").strip().lower()
            if another_roll != 'yes':
                break
        
        except ValueError:
            print("Invalid input. Please enter valid integers.")
    
    print("Thank you for using the Dice Rolling Simulator! Goodbye.")

if __name__ == "__main__":
    main()
