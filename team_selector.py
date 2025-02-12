import random

print("Welcome to Team/Player Allocator!")

while True:
    try:
        number_of_players = int(input("How many players are there? (Max 100): "))
        if 1 <= number_of_players <= 100:
            break
        else:
            print("Please enter a number between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

players = []
for i in range(number_of_players):
    player_name = input(f"Enter name for player {i + 1}: ").strip()
    players.append(player_name) 

while True:
    response = input("\nIs it a team or individual sport?\nType 'team' or 'individual': ").strip().lower()

    if response == "team":
        random.shuffle(players)
        team1 = players[:len(players)//2]
        team2 = players[len(players)//2:]

        print("\nTeam 1 Captain: " + random.choice(team1))
        print("Team 1:")
        for player in team1:
            print(player)

        print("\nTeam 2 Captain: " + random.choice(team2))
        print("Team 2:")
        for player in team2:
            print(player)

    elif response == "individual":
        random.shuffle(players)
        for i in range(0, len(players) - 1, 2):
            print(players[i] + " vs " + players[i + 1])
            starter = random.choice([players[i], players[i + 1]])
            print(starter + " starts")

        if len(players) % 2 != 0:
            print(f"\n{players[-1]} has no opponent and will be assigned a bye round.")

    else:
        print("Invalid input. Please enter 'team' or 'individual'.")
        continue

    play_again = input("\nPick teams again? Type 'y' or 'n': ").strip().lower()
    if play_again == "n":
        break
