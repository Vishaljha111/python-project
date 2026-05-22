import random  # Add this line

option = ("rock", "paper", "scissors")
player = None 
computer = random.choice(option)
player = input("Enter your choice (rock, paper, scissors): ")

print(f"Computer chose: {computer}")
print(f"Player chose: {player}")