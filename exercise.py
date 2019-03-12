import ipdb
import operator

ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold': 'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

contestant_scores = {}

for voter in ballots:
    for tier, contestant in voter.items():
        if tier == 'gold' and contestant in contestant_scores:
            contestant_scores[contestant] += 3
        elif tier == 'gold' and contestant not in contestant_scores:
            contestant_scores[contestant] = 3
        elif tier == 'silver' and contestant in contestant_scores:
            contestant_scores[contestant] += 2
        elif tier == 'silver' and contestant not in contestant_scores:
            contestant_scores[contestant] = 2
        elif tier == 'bronze' and contestant in contestant_scores:
            contestant_scores[contestant] += 1
        elif tier == 'bronze' and contestant not in contestant_scores:
            contestant_scores[contestant] = 1
print(contestant_scores)


winner = None
highest_so_far = 0

for i, scores in contestant_scores.items():
    if scores > highest_so_far:
        highest_so_far = scores
        winner = i

print("The winner is: {}".format(winner))
