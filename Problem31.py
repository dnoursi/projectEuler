#!/usr/bin/env python3

# Coins of size 200, 100, 50, 20, 10, 5, 2, 1
# Want each distinct way to make 200
# Create possbilities recursively, sequence is always decreasing or constant Lft -> Rght

choices = [200, 100, 50, 20, 10, 5, 2, 1]

def nPossibs(stub):
    stubSize = sum(stub)
    #print(stubSize)
    if stubSize == 200:
        return 1
    elif stubSize < 200:
        result = 0

        startFrom = 0
        if stub:
            startFrom = choices.index(stub[-1])

        for choice in choices[startFrom:]:
            if choice + stubSize <= 200:
                result += nPossibs(stub + [choice])
        return result

    elif stubSize > 200:
        print("Whoops")
        return 0
    print("nooo", stubSize)


print(nPossibs([]))

