"""
RA = int(input("Rating A?"))
RB = int(input("Rating B?"))
SA = 0
SB = 1

ExpScoreA = (1 / (1 + (10 ** ((RB - RA) / 400))))
ExpScoreB = (1 / (1 + (10 ** ((RA-RB) / 400))))

print(ExpScoreA, ExpScoreB)

ques = input("Who won (A or B)?")

if ques.lower() == "a":
    SA = 1
    SB = 0
else :
    SB = 1
    SA = 0
K = 50

RatA = RA + K*(SA - ExpScoreA)
RatB = RB + K*(SB - ExpScoreB)

print(f"A's rating is {RatA}, and B's is {RatB}")
"""


# Original Rating
Rating = 10

# Maximum gain or loss
K = 5

players = []
set = []
rat = []

# Create array of player names
abc = int(input("How many players are there?"))
for x in range(abc):
    players.append(str(input(f"Name of player {x+1}?")))

# 2D array,, each player has an array of all other players assigned to them
for x in range(len(players)):
    set.append(players.copy())

# Create an array for the original ratings of all the players
for x in range(len(players)):
    rat.append(Rating)

for a in range(len(players)):
    for b in range(a+1, len(players)):
        ExpScoreA = (1 / (1 + (10 ** ((rat[b] - rat[a]) / 400))))
        ExpScoreB = (1 / (1 + (10 ** ((rat[a] - rat[b]) / 400))))
        ques = input(f"Who won ({players[a]} or {players[b]})?")

        if ques.lower() == players[a].lower():
            SA = 1
            SB = 0
        else:
            SB = 1
            SA = 0

        rat[a] = rat[a] + K * (SA - ExpScoreA)
        rat[b] = rat[b] + K * (SB - ExpScoreB)

        print(f"{players[a]}'s rating is {rat[a]}, and {players[b]}'s is {rat[b]}")

for x in range(len(players)):
    print(f"{players[x]} has a rating of {round(rat[x], 2)}")
