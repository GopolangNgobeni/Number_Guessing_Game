import sys
import random


def get_hints(number):
    hints = {1:"\n**Hint: I am the start of everything, the simplest number you can see.",
             2:"\n**Hint I am what you need to make a pair.",
             3:"\n**Hint I am the count of the wise men who followed the star.",
             4:"\n**Hint Think of the four seasons in a year.",
             5:"\n**Hint Think of the number of points on a star.",
             6:"\n**Hint I am half a dozen.",
             7:"\n**Hint: am often considered a lucky number.",
             8:"\n**Hint: Think of the two circles stacked together.",
             9:"\n**Hint: I am the number of lives a cat is said to have.",
             10:"\n**Hint: I am the number of fingers on both hands combined."}
    
    return hints.get(number,"No hints found.")

def run_game():
    while True:
        computer_number = random.randint(1,10)
        attempts = 0
        
        while attempts < 5:
            player_guess = input("\nEnter a number from 1 - 10: ")
            if player_guess == "exit".lower():
                print("Goodbye..")
                sys.exit()
            try:
                player_guess = int(player_guess)
                if not (1 <= player_guess <= 10):
                    print("Invalid input out of range ,enter a number from 1 - 10")
                    continue
            except ValueError:
                print("Invalid input, Please enter a number from 1 to 10.")  
                continue
                
            if player_guess == computer_number:
                attempts += 1
                print(f"Guess Corrext! , after {attempts} attempts , You are awesome.!")
                print("\nKeep playing enter a number again!")
                break
            else:
                print("Your Guess is wrong..")
                print(get_hints(computer_number))
                attempts +=1

                
                
        if attempts == 5:
            print(f"You Loose!..\nThe number was {computer_number}") 
            while True: 
                responce = input("\npress enter to play again or exit to exit the game: ")   
                if responce == "exit".lower():
                    print("Goodbye!..")
                    sys.exit()
                if responce == "":
                    print("lets play again!")
                    break                           
                else:
                    print("ivalid input please press enter to play again or exit to exit the game..")


if __name__ == "__main__":
    print("Welcome to the number Guessing Game..") 
    print("Guess a number from 1 - 10 ")
    print("\nYou have 5 attempts to guess the correct number.")
    print("If you fail to guess correctly within these attempts, you'll lose the round.")
    print("enter exit if you want to exit the Game.")  
    
    run_game()               