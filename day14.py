day_14_content = int("074501")
scores = [3, 7]
elf1 = 0
elf2 = 1
while(len(scores) < day_14_content+10):
    #print(elf1, elf2, scores)
    elf1score = scores[elf1]
    elf2score = scores[elf2]
    new = str(elf1score + elf2score)
    for num in new:
        scores.append(int(num))
    elf1 += 1 + elf1score
    elf2 += 1 + elf2score
    scorelen = len(scores)
    if elf1 >= scorelen:
        multiplier = int(elf1/scorelen)
        elf1 -= multiplier*scorelen
    if elf2 >= scorelen:
        multiplier = int(elf2/scorelen)
        elf2 -= multiplier*scorelen
print(''.join(str(x) for x in scores[-10:]))

for i in range(25000000):
    #print(elf1, elf2, scores)
    elf1score = scores[elf1]
    elf2score = scores[elf2]
    new = str(elf1score + elf2score)
    for num in new:
        scores.append(int(num))
    elf1 += 1 + elf1score
    elf2 += 1 + elf2score
    scorelen = len(scores)
    if elf1 >= scorelen:
        multiplier = int(elf1/scorelen)
        elf1 -= multiplier*scorelen
    if elf2 >= scorelen:
        multiplier = int(elf2/scorelen)
        elf2 -= multiplier*scorelen
#print(''.join(str(x) for x in scores))
print(''.join(str(x) for x in scores).find("074501"))
