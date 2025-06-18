import time

player_id = int(input("Please enter your player id: "))

while True:
    games_played = int(input("Please enter the amount of games played: "))
    if games_played < 5:
        print("Minimum = 5")
    elif games_played > 10:
        print("Maximum = 10")
    else:
        break

gameslist = []

for i in range(games_played):
    score = int(input(f"Enter score for game #{i+1} "))
    time_taken = float(input(f"Enter time taken (in minutes) for game #{i+1} "))
    gameslist.append({"score": score, "time": time_taken})

for i, data in enumerate(gameslist, 1):
    print(f"Game #{i}: Score = {data['score']}, Time Taken = {data['time']} minutes")

highest_score = max(game['score'] for game in gameslist)

total_time = sum(game['time'] for game in gameslist)
average_time = total_time / games_played if games_played > 0 else 0

output = []

output.append(f"The highest score achieved is: {highest_score}")
output.append(f"The average time spent playing is: {average_time:.2f} minutes")

filename = "game_data.txt"

with open (filename, 'W') as file:
    for line in output:
        file.write(line + "\n")

time.sleep(5)