# inspired by https://github.com/Fadi88/AoC/blob/master/2021/day21/code.py


from itertools import product


'''

def part1():
    pos = [4,2]

    scores = [0] * 2
    dice = 0
    while True:
        p1 = 3 * dice + 6
        p2 = 3 * dice + 15

        dice += 3
        pos[0] = (pos[0] + p1 - 1) % 10 + 1
        scores[0] += pos[0]
        if scores[0] >= 1000:
            break

        dice += 3
        pos[1] = (pos[1] + p2 - 1) % 10 + 1
        scores[1] += pos[1]
        if scores[1] >= 1000:
            break

    print(min(scores) * dice)
'''

def play_driac(p1, p2, s1=0, s2=0, player=0, cache={}):

    if (p1, p2, s1, s2, player) in cache:
        return cache[(p1, p2, s1, s2, player)]

    wins = [0, 0]
    rolls = [r1 + r2 + r3 for r1, r2, r3 in product([1, 2, 3], repeat=3)]   

    for r in rolls:
        pos = [p1, p2]
        score = [s1, s2]

        pos[player] = (pos[player] + r - 1) % 10 + 1
        score[player] += pos[player]

        if score[player] >= 21:
            wins[player] += 1
        else:
            w1, w2 = play_driac(
                pos[0], pos[1], score[0], score[1], 1 if player == 0 else 0
            )

            wins[0] += w1
            wins[1] += w2

    cache[(p1, p2, s1, s2, player)] = wins
    # cache[(p2, p1, s2, s1, 1 if player == 0 else 0)] = wins[::-1]  ### What 
    return wins



def part2():

    print(max(play_driac(4, 8)))


if __name__ == "__main__":
    print("Part 2")
    part2()


# Part 2
# 444356092776315