'''highest_score = 0
result_f = open("results.txt")
for line in result_f:
    if float(line) > highest_score:
        highest_score = float(line)
result_f.close()
print("The highest score was:")
print(highest_score)'''

scores = {}

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores[score] = name
result_f.close()

print(' ')
print('-*' * 25)
print("Surf-A-Thon")
print("The higuest Scores were:")
print('-*' * 25)
print(' ')
for each_score in sorted(scores.keys(), reverse = True):
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)
    print(' ')

print("\n")
print('-*' * 25)

'''
print('-*' * 25)
print('=' * 25)
print("The higuest Scores were:")
print('=' * 25)
print(' ')
'''



