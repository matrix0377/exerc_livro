'''highest_score = 0
result_f = open("results.txt")
for line in result_f:
    if float(line) > highest_score:
        highest_score = float(line)
result_f.close()
print("The highest score was:")
print(highest_score)'''

scores = []
names = []

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
    names.append(name)
result_f.close()

scores.sort()
scores.reverse()
names.sort()
names.reverse()

print(' ')
print('-*' * 25)
print("Surf-A-Thon")
print('-*' * 25)
print('=' * 25)
print("The higuest Scores were:")
print('=' * 25)
print(' ')
print(names[0] + ' with ' + str(scores[0]))
print("\n")
print(names[1] + ' with ' + str(scores[1]))
print("\n")
print(names[2] + ' with ' + str(scores[2]))
print("\n")
print('-*' * 25)

