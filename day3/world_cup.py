import random
def play_offs(teams, round_name):
    results = {}
    print(f"\n{round_name} Matches")
    for i in range(0, len(teams), 2):
        team1 = teams[i]
        team2 = teams[i + 1]
        score1 = random.randint(0, 3)
        score2 = random.randint(0, 3)
        if score1 > score2:
            print(f"{team1} {score1} - {score2} {team2}")
            results[team1] = score1
        elif score2 > score1:
            print(f"{team1} {score1} - {score2} {team2}")
            results[team2] = score2
        else:
            while score1 == score2:
                print(f"Draw {team1} {score1} - {score2} {team2}")
                score1 = random.randint(0, 3)
                score2 = random.randint(0, 3)
                if score1 > score2:
                    results[team1] = score1
                    print(f"{team1} {score1} - {score2} {team2}")
                elif score2 > score1:
                     results[team2] = score2
                     print(f"{team1} {score1} - {score2} {team2}")
                else:
                    continue
    return list(results.keys()) 


group_A = {
    "USA" : 0,
    "Mexico" : 0,
    "England" : 0,
    "Iran" : 0
}
group_B = {
    "Wales" : 0,
    "Ghana" : 0,
    "Argentina" : 0,
    "Saudi Arabia" : 0
}
group_C = {
    "Poland" : 0,
    "Nigeria" : 0,
    "Congo" : 0,
    "Portugal" : 0
}
group_D = {
    "France" : 0,
    "Denmark" : 0,
    "Tunisia" : 0,
    "Australia" : 0
}
group_E = {
    "Spain" : 0,
    "Germany" : 0,
    "Japan" : 0,
    "Costa Rica" : 0
}
group_F = {
    "Belgium" : 0,
    "Croatia" : 0,
    "Morocco" : 0,
    "Canada" : 0
}
group_G = {
    "Brazil" : 0,
    "Switzerland" : 0,
    "Cameroon" : 0,
    "Serbia" : 0
}
group_H = {
    "Netherlands" : 0,
    "South Korea" : 0,
    "Ecuador" : 0,
    "Qatar" : 0
}

groups = [group_A, group_B, group_C, group_D, group_E, group_F, group_G, group_H]
print("World Cup Groups")
for group in groups:
    print(f"Group : {groups.index(group) + 1}")
    for team in group:
        print(team)

print("Round 1")
for group in groups:
    print(f"Group : {groups.index(group) + 1}")
    teams = list(group.keys())
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            team1 = teams[i]
            team2 = teams[j]
            score1 = random.randint(0, 5)
            score2 = random.randint(0, 5)
            print(f"{team1} {score1} - {score2} {team2}")
            if score1 > score2:
                group[team1] += 3
            elif score2 > score1:
                group[team2] += 3
            else:
                group[team1] += 1
                group[team2] += 1
        print()

print("\nRound 1 Results")
for group in groups:
    print(f"Group : {groups.index(group) + 1}")
    for team in group:
        print(f"  {team} : {group[team]} points")

qualified_teams = []
for group in groups:
    sorted_teams = sorted(group.items(), key=lambda x: x[1], reverse=True)
    qualified_teams.append(sorted_teams[0][0]) 
    qualified_teams.append(sorted_teams[1][0])

print("\nQualified Teams for Round of 16")
for team in qualified_teams:
    print(f"  {team}")

round_of_16 = {}
results_16 = {}
print("\nRound of 16 Matches")
quarter_final = play_offs(qualified_teams, "Round of 16")

print("\nTeams qualified for Quarter-finals")
for team in quarter_final:
    print(team)

semi_final = play_offs(quarter_final, "Quarter-finals")
print("\nTeams qualified for semi-finals")
for team in semi_final:
    print(team)

finalists = play_offs(semi_final, "Semi-finals")
print("\nTeams qualified for finals")
for team in finalists:
    print(team)

champion = play_offs(finalists, "Finals")
print("\nWorld Cup Champion")
print(f"Congratulations {champion[0]}!")

       


