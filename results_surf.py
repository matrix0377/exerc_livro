'''highest_score = 0
result_f = open("results.txt")
for line in result_f:
    if float(line) > highest_score:
        highest_score = float(line)
result_f.close()
print("The highest score was:")
print(highest_score)'''

scores = []

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
result_f.close()

scores.sort()
scores.reverse()

print(' ')
print('-*' * 25)
print("Surf-A-Thon")
print('-*' * 25)
print('=' * 25)
print("The TOP Scores were:")
print('=' * 25)
print(' ')
print(scores[0])
print("\n")
print(scores[1])
print("\n")
print(scores[2])
print("\n")
print('-*' * 25)

